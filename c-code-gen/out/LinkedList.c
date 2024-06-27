#include "LinkedList.h"

typedef struct LinkedList_private_data LinkedList_private_data;

struct LinkedList_private_data {
    Arena *arena;
};

static int LinkedList__hash(LinkedList *instance);
static int LinkedList__equals(LinkedList *instance, LinkedList *other);
static void LinkedList__to_string(LinkedList *instance, StringBuilder *sb);
static void LinkedList__serialize(LinkedList *instance, StringBuilder *sb);
static void LinkedList__unserialize(LinkedList *instance, char *buffer, int *position);
static void LinkedList__destroy(LinkedList *instance);

static LinkedList_vtable vtable =  {
    .hash = LinkedList__hash,
    .equals = LinkedList__equals,
    .to_string = LinkedList__to_string,
    .serialize = LinkedList__serialize,
    .unserialize = LinkedList__unserialize,
    .destroy = LinkedList__destroy,
};

LinkedList *new_LinkedList(Arena *a) {
    void *p = a->vt->allocate(a, sizeof(LinkedList) + sizeof(LinkedList_private_data));
    if (p == NULL)
        return NULL;
    LinkedList *instance = (LinkedList *)p;
    LinkedList_private_data *data = (LinkedList *)(p + sizeof(LinkedList));

    instance->vt = &vtable;

    data->arena = a;

    return instance;
}

static int LinkedList__hash(LinkedList *instance) {
    if (instance == NULL)
        return;
    LinkedList_private_data *data = (LinkedList_private_data *)(instance + 1);
    if (data == NULL)
        return;

    // do work here...

    return;
}

static int LinkedList__equals(LinkedList *instance, LinkedList *other) {
    if (instance == NULL)
        return;
    LinkedList_private_data *data = (LinkedList_private_data *)(instance + 1);
    if (data == NULL)
        return;

    // do work here...

    return;
}

static void LinkedList__to_string(LinkedList *instance, StringBuilder *sb) {
    if (instance == NULL)
        return;
    LinkedList_private_data *data = (LinkedList_private_data *)(instance + 1);
    if (data == NULL)
        return;

    // do work here...

    return;
}

static void LinkedList__serialize(LinkedList *instance, StringBuilder *sb) {
    if (instance == NULL)
        return;
    LinkedList_private_data *data = (LinkedList_private_data *)(instance + 1);
    if (data == NULL)
        return;

    // do work here...

    return;
}

static void LinkedList__unserialize(LinkedList *instance, char *buffer, int *position) {
    if (instance == NULL)
        return;
    LinkedList_private_data *data = (LinkedList_private_data *)(instance + 1);
    if (data == NULL)
        return;

    // do work here...

    return;
}

static void LinkedList__destroy(LinkedList *instance) {
    if (instance == NULL)
        return;
    LinkedList_private_data *data = (LinkedList_private_data *)(instance + 1);
    if (data == NULL)
        return;

    // do work here...

    return;
}

