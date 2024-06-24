from typing import List, Dict
import sys

"""
    It creates a set of files for a specific "object", with appropriate structures and pointers.
    The benefits are:
    - public instance and constructor.
    - public vtable for methods via pointers
    - hidden internal instance data per object
    - unit tests
    - requirements:
        - arena object for the constructor
        - string_builder object for the "to_string()" method
        - ???? for unit tests
    
    It'd be lovely if we could have an "add-method" action!
    
"""
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







class Method:
    def __init__(self, name, ret, args) -> None:
        self.name = name
        self.ret = ret
        self.args = args

class Object:
    def __init__(self, name: str, ctor_args: List[str], methods: List[Method]) -> None:
        self.name = name
        self.ctor_args = ctor_args
        self.methods = methods
        self.lname = name.lower()
        self.uname = name.upper()

def create_c_object_ver2(name: str): 
    methods: List[Method] = [
        Method('hash', 'int', []),
        Method('equals', 'int', [name + ' *other']),
        Method('to_string', 'void', ['string_builder *sb']),
        Method('serialize', 'void', ['string_builder *sb']),
        Method('unserialize', 'void', ['char *buffer', 'int *position']),
        Method('destroy', 'void', []),
    ]
    obj = Object(name, [], methods)




if __name__ == "__main__":
    print(sys.argv)
    # if len(sys.argv) < 2:
    #     print("syntax: {} <obj-name>".format(sys.argv[0]))
    # else:
    #     create_c_object_ver1(sys.argv[1])
    # create_c_object_ver1('list')
    create_c_object_ver1('LinkedList')
