#ifndef _LINKEDLIST_H
#define _LINKEDLIST_H

#include "string_builder.h"
#include "arena.h"

typedef struct linkedlist linkedlist;
typedef struct linkedlist_vtable linkedlist_vtable;

struct linkedlist {
    linkedlist_vtable *vt;
};

struct linkedlist_vtable {
    int (*get_length)(linkedlist *instance);
    void (*set_length)(linkedlist *instance, int length);
    char *(*func3)(linkedlist *instance, char *arg1);

    int (*equals)(linkedlist *instance, linkedlist *other);
    void (*to_string)(linkedlist *instance, string_builder *sb);
    unsigned (*hash)(linkedlist *instance);
    void (*destroy)(linkedlist *instance);
};

linkedlist *new_linkedlist(arena *arena);

#endif // _LINKEDLIST_H
