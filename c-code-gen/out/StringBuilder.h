#ifndef _STRINGBUILDER_H
#define _STRINGBUILDER_H

#include "Arena.h"

typedef struct StringBuilder StringBuilder;
typedef struct StringBuilder_vtable StringBuilder_vtable;

struct StringBuilder {
    StringBuilder_vtable *vt;
};

struct StringBuilder_vtable {
    void (*append)(StringBuilder *instance, const char *format, ...);
};

StringBuilder *new_StringBuilder(Arena *a);
    

#endif // _STRINGBUILDER_H
