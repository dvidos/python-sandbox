#ifndef _LINKEDLIST_H
#define _LINKEDLIST_H

#include "Arena.h"
#include "StringBuilder.h"

typedef struct LinkedList LinkedList;
typedef struct LinkedList_vtable LinkedList_vtable;

struct LinkedList {
    LinkedList_vtable *vt;
};

struct LinkedList_vtable {
    int (*hash)(LinkedList *instance);
    int (*equals)(LinkedList *instance, LinkedList *other);
    void (*to_string)(LinkedList *instance, StringBuilder *sb);
    void (*serialize)(LinkedList *instance, StringBuilder *sb);
    void (*unserialize)(LinkedList *instance, char *buffer, int *position);
    void (*destroy)(LinkedList *instance);
};

LinkedList *new_LinkedList(Arena *a);


#endif // _LINKEDLIST_H
