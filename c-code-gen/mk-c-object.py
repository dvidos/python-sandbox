from typing import List, Dict
import sys
import os

"""
    It creates a set of files for a specific "object", with appropriate structures and pointers.
    The benefits are:
    - public instance and constructor.
    - public vtable for methods via pointers
    - hidden internal instance data per object
    - unit tests
    - requirements:
        - Arena object for the constructor
        - StringBuilder object for the "to_string()" method
        - ???? for unit tests
    
    It'd be lovely if we could have an "add-method" action!
    
"""
def tab() -> str:
    return '    '

def load(filename):
    with open(filename, 'r') as f:
        text = f.read()
    return text

def save(filename, text):
    with open(filename, 'w') as f:
        f.write(text)

def subst(template: str, variables: Dict[str, str]):
    text = template
    for varname in variables:
        placeholder = '[' + varname + ']'
        text = text.replace(placeholder, variables[varname])
    return text

def create_c_object_ver1(name: str): 
    # from template, create both header and source file.
    print("creating object '{}'".format(name))
    vars = {
        'UNAME': name.upper(),
        'LNAME' : name.lower(),
    }
    fn = name.lower()
    save('out/{}.h'.format(fn), subst(load('templates/object.h'), vars))
    save('out/{}.c'.format(fn), subst(load('templates/object.c'), vars))
    save('out/{}_tests.h'.format(fn), subst(load('templates/object_tests.h'), vars))
    save('out/{}_tests.c'.format(fn), subst(load('templates/object_tests.c'), vars))





class Stereotypes:
    def ifdef(symbol: str):
        return '#ifdef {}'.format(symbol.upper())
    def ifndef(symbol: str):
        return '#ifndef {}'.format(symbol.upper())
    def define(symbol: str):
        return '#define {}'.format(symbol.upper())
    def endif(symbol: str):
        return '#endif // {}'.format(symbol.upper())
    def include(filename: str):
        return '#include "{}.h"'.format(filename)
    def include_lib(filename: str):
        return '#include <{}.h>'.format(filename)
    def typedef_struct(name: str):
        return 'typedef struct {} {};'.format(name, name)
    def header_file_guard(name: str, lines: List[str]):
        lines.insert(0, "#ifndef _{}_H".format(name))
        lines.insert(1, "#define _{}_H".format(name))
        lines.insert(2, '')
        lines.append('')
        lines.append("#endif // _{}_H".format(name))
        return lines
    def bracketed_block(prefix: str, lines: List[str], ending = None):
        return prefix + " {\n    " + "\n    ".join(lines) + "\n}" + ('' if ending is None else ending)



class Method:
    def __init__(self, ret: str, name, args: List[str]) -> None:
        self.name = name
        self.ret = ret
        self.ret_space = '' if self.ret.endswith('*') else ' '
        self.args = args
        self.args_preamble = ', ' if len(self.args) > 0 else ''
        self.obj_name = ''
        if self.ret == 'int':
            self.ret_error = ' -1'
        elif self.ret.endswith('*'):
            self.ret_error = ' NULL'
        elif self.ret == 'bool':
            self.ret_error = ' false'
        else:
            self.ret_error = ''

    def set_obj_name(self, obj_name: str):
        self.obj_name = obj_name

    def vtable_member_declaration(self) -> str:
        return "{}{}(*{})({} *instance{}{});".format(
            self.ret, 
            self.ret_space,
            self.name,
            self.obj_name,
            self.args_preamble,
            ", ".join(self.args)
        )

    def vtable_member_initialization(self) -> str:
        return '.{} = {}__{},'.format(self.name, self.obj_name, self.name)

    def static_forward_declaration(self) -> str:
        return 'static {}{}{}__{}({} *instance{}{});'.format(
            self.ret,
            self.ret_space,
            self.obj_name,
            self.name,
            self.obj_name,
            self.args_preamble,
            ", ".join(self.args)
        )
    
    def static_implementation(self) -> str:
        lines = [
            'static {}{}{}__{}({} *instance{}{}) {{'.format(
                self.ret,
                self.ret_space,
                self.obj_name,
                self.name,
                self.obj_name,
                self.args_preamble,
                ", ".join(self.args)
            ),
            '    if (instance == NULL)',
            '        return;',
            '    {}_private_data *data = ({}_private_data *)(instance + 1);'.format(self.obj_name, self.obj_name, self.obj_name),
            '    if (data == NULL)',
            '        return;',
            '',
            '    // do work here...',
            '',
            '    return;',
            '}'
        ]
        return "\n".join(lines) + "\n"

    def test_implementation(self) -> str:
        lines = [
            "static void test_{}_{}(Arena *a) {{".format(self.obj_name, self.name),
            "    {} *instance = new_{}(a);".format(self.obj_name, self.obj_name),
            "    instance->vt->{}(instance);".format(self.name),
            "    assert(1);",
            "}"
        ]
        return "\n".join(lines) + "\n"

    def test_implementation_call(self) -> str:
        return "    test_{}_{}(a);".format(self.obj_name, self.name)



class CObject:
    def __init__(self, name: str, ctor_args: List[str], methods: List[Method]) -> None:
        self.name = name
        self.ctor_args = ctor_args
        self.methods = methods
        self.lname = name.lower()
        self.uname = name.upper()
        for method in methods:
            method.set_obj_name(self.name)

    def header_file_content(self) -> List[str]:
        lines = [
            Stereotypes.include("Arena"),
            Stereotypes.include("StringBuilder"),
            '',
            Stereotypes.typedef_struct(self.name),
            Stereotypes.typedef_struct(self.name + '_vtable'),
            '',
            Stereotypes.bracketed_block('struct {}'.format(self.name), [
                "{}_vtable *vt;".format(self.name)
            ], ';'),
            '',
            Stereotypes.bracketed_block('struct {}_vtable'.format(self.name), [
                m.vtable_member_declaration() for m in self.methods
            ], ';'),
            '',
            self.constructor_declaration(),
            ''
        ]
        return Stereotypes.header_file_guard(self.uname, lines)

    def source_file_content(self) -> List[str]:
        lines = []
        lines.append(Stereotypes.include(self.name))
        lines.append('')
        lines.append(Stereotypes.typedef_struct('{}_private_data'.format(self.name)))
        lines.append('')
        lines.append(Stereotypes.bracketed_block('struct {}_private_data'.format(self.name), [
            'Arena *arena;'
        ], ';'))
        lines.append('')
        lines.extend([m.static_forward_declaration() for m in self.methods])
        lines.append('')
        lines.append(Stereotypes.bracketed_block('static {}_vtable vtable = '.format(self.name), [
            m.vtable_member_initialization() for m in self.methods
        ], ';'))
        lines.append('')
        lines.append(self.constructor_implementation())
        lines.extend([m.static_implementation() for m in self.methods])
        return lines

    def tests_header_file_content(self) -> str:
        lines = []
        lines.append(Stereotypes.include("Arena"))
        lines.append('')
        lines.append('void test_{}(Arena *a);'.format(self.name))
        lines.append('')
        return Stereotypes.header_file_guard(self.uname + '_TESTS', lines)

    def tests_source_file_content(self) -> List[str]:
        lines = ['']
        lines.append(Stereotypes.include(self.name))
        lines.append('')
        lines.append(self.constructor_test_implementation())
        lines.extend([m.test_implementation() for m in self.methods])
        lines.append('void test_{}(Arena *a) {{'.format(self.name))
        lines.append('    test_{}_constructor(a);'.format(self.name))
        for method in self.methods:
            lines.append(method.test_implementation_call())
        lines.append('}')
        return lines

    def constructor_declaration(self):
        return "{} *new_{}(Arena *a);".format(self.name, self.name)
    
    def constructor_implementation(self) -> str:
        lines = [
            "{} *new_{}(Arena *a) {{".format(self.name, self.name),
            "    void *p = a->vt->allocate(a, sizeof({}) + sizeof({}_private_data));".format(self.name, self.name),
            "    if (p == NULL)",
            "        return NULL;",
            "    {} *instance = ({} *)p;".format(self.name, self.name),
            "    {}_private_data *data = ({} *)(p + sizeof({}));".format(self.name, self.name, self.name),
            "",
            "    instance->vt = &vtable;",
            "",
            "    data->arena = a;",
            "",
            "    return instance;",
            "}",
        ]
        return "\n".join(lines) + "\n"

    def constructor_test_implementation(self) -> str:
        lines = []
        lines.append('static void test_{}_constructor(Arena *a) {{'.format(self.name))
        lines.append('    {} *instance = new_{}(a);'.format(self.name, self.name))
        lines.append('    assert(instance);')
        lines.append('}')
        return "\n".join(lines) + "\n"




def create_c_object_ver2(name: str): 
    methods: List[Method] = [
        Method('int', 'hash', []),
        Method('int', 'equals', [name + ' *other']),
        Method('void', 'to_string', ['StringBuilder *sb']),
        Method('void', 'serialize', ['StringBuilder *sb']),
        Method('void', 'unserialize', ['char *buffer', 'int *position']),
        Method('void', 'destroy', []),
    ]
    obj = CObject(name, [], methods)
    fn = name
    save("out/{}.h".format(fn),       "\n".join(obj.header_file_content()) + "\n")
    save("out/{}.c".format(fn),       "\n".join(obj.source_file_content()) + "\n")
    save("out/{}_tests.h".format(fn), "\n".join(obj.tests_header_file_content()) + "\n")
    save("out/{}_tests.c".format(fn), "\n".join(obj.tests_source_file_content()) + "\n")



if __name__ == "__main__":
    os.chdir('c-code-gen')
    # if len(sys.argv) < 2:
    #     print("syntax: {} <obj-name>".format(sys.argv[0]))
    # else:
    #     create_c_object_ver1(sys.argv[1])
    # create_c_object_ver1('list')
    create_c_object_ver2('LinkedList')
    os.chdir('..')

