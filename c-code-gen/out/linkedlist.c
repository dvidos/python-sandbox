#include "linkedlist.h"

typedef struct linkedlist_private_data linkedlist_private_data;

#define LINKEDLIST_MEMORY_SIZE()           (sizeof(linkedlist) + sizeof(linkedlist_private_data))
#define LINKEDLIST_PRIVATE_DATA(instance)  (linkedlist_private_data *)(((void *)(instance)) + sizeof(linkedlist))


// private data, stored after instance
struct linkedlist_private_data {
    arena *arena;
    int length;
    void *head;
    void *tail;
};


// private methods, exposed through pointers
static int linkedlist__get_length(linkedlist *instance);
static void linkedlist__set_length(linkedlist *instance, int length);
static char *linkedlist__func3(linkedlist *instance, char *arg1);
static int linkedlist__equals(linkedlist *instance, linkedlist *other);
static void linkedlist__to_string(linkedlist *instance, string_builder *sb);
static unsigned linkedlist__hash(linkedlist *instance);
static void linkedlist__destroy(linkedlist *instance);

static linkedlist_vtable vtable = {
    .get_length = linkedlist__get_length,
    .set_length = linkedlist__set_length,
    .func3 = linkedlist__func3,
    .equals = linkedlist__equals,
    .to_string = linkedlist__to_string,
    .hash = linkedlist__hash,
    .destroy = linkedlist__destroy
};

linkedlist *new_linkedlist(arena *arena) {
    // one pointer holds space for both the public and private parts
    void *ptr = arena->alloc(LINKEDLIST_MEMORY_SIZE());

    linkedlist *instance = (linkedlist *)ptr;
    instance->vt = &vtable;

    linkedlist_private_data *data = LINKEDLIST_PRIVATE_DATA(instance);
    memset(data, 0, sizeof(linkedlist_private_data));
    data->arena = arena;


    return instance;
}

static int linkedlist__get_length(linkedlist *instance) {
    if (instance == NULL)
        return -1;
    linkedlist_private_data *data = LINKEDLIST_PRIVATE_DATA(instance);

    // do work here...
    return data->length;
}

static void linkedlist__set_length(linkedlist *instance, int length) {
    if (instance == NULL)
        return;
    linkedlist_private_data *data = LINKEDLIST_PRIVATE_DATA(instance);

    // do work here...
    data->length = length;
}

static char *linkedlist__func3(linkedlist *instance, char *arg1) {
    if (instance == NULL)
        return NULL;
    linkedlist_private_data *data = LINKEDLIST_PRIVATE_DATA(instance);

    // do work here...
    
    return arg1;
}

static int linkedlist__equals(linkedlist *instance, linkedlist *other) {
    if (instance == NULL)
        return (other == NULL);
    linkedlist_private_data *data = LINKEDLIST_PRIVATE_DATA(instance);
    linkedlist_private_data *other_data = LINKEDLIST_PRIVATE_DATA(other);

    if (data != other_data)
        return false;
    if (data->length != other_data->length)
        return false;
    
    return true;
}

static void linkedlist__to_string(linkedlist *instance, string_builder *sb) {
    if (instance == NULL || sb == NULL)
        return;
    linkedlist_private_data *data = LINKEDLIST_PRIVATE_DATA(instance);

    sb->vt->appendf("linkedlist(length=%d)", data->length);
}

static unsigned linkedlist__hash(linkedlist *instance) {
    if (instance == NULL)
        return 0;
    linkedlist_private_data *data = LINKEDLIST_PRIVATE_DATA(instance);

    unsigned hash = 0;
    // calculate hash for private data

    return hash;
}

static void linkedlist__destroy(linkedlist *instance) {
    if (instance == NULL)
        return;
    linkedlist_private_data *data = LINKEDLIST_PRIVATE_DATA(instance);

    // destroy private data here (e.g. close files)

    data->arena->free(instance);
}
