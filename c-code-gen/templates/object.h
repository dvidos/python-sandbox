#ifndef _[UNAME]_H
#define _[UNAME]_H

#include "string_builder.h"
#include "arena.h"

typedef struct [LNAME] [LNAME];
typedef struct [LNAME]_vtable [LNAME]_vtable;

struct [LNAME] {
    [LNAME]_vtable *vt;
};

struct [LNAME]_vtable {
    int (*get_length)([LNAME] *instance);
    void (*set_length)([LNAME] *instance, int length);
    char *(*func3)([LNAME] *instance, char *arg1);

    int (*equals)([LNAME] *instance, [LNAME] *other);
    void (*to_string)([LNAME] *instance, string_builder *sb);
    unsigned (*hash)([LNAME] *instance);
    void (*destroy)([LNAME] *instance);
};

[LNAME] *new_[LNAME](arena *arena);

#endif // _[UNAME]_H
