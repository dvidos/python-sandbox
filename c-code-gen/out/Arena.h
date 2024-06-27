#ifndef _ARENA_H
#define _ARENA_H

typedef struct Arena Arena;
typedef struct Arena_vtable Arena_vtable;

struct Arena {
    Arena_vtable *vt;
};

struct Arena_vtable {
    void *(*allocate)(Arena *instance, int size);
};

Arena *new_Arena(Arena *a);
    

#endif // _ARENA_H
