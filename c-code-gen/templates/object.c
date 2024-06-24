#include "[LNAME].h"

typedef struct [LNAME]_private_data [LNAME]_private_data;

#define [UNAME]_MEMORY_SIZE()           (sizeof([LNAME]) + sizeof([LNAME]_private_data))
#define [UNAME]_PRIVATE_DATA(instance)  ([LNAME]_private_data *)(((void *)(instance)) + sizeof([LNAME]))


// private data, stored after instance
struct [LNAME]_private_data {
    arena *arena;
    int length;
    void *head;
    void *tail;
};


// private methods, exposed through pointers
static int [LNAME]__get_length([LNAME] *instance);
static void [LNAME]__set_length([LNAME] *instance, int length);
static char *[LNAME]__func3([LNAME] *instance, char *arg1);
static int [LNAME]__equals([LNAME] *instance, [LNAME] *other);
static void [LNAME]__to_string([LNAME] *instance, string_builder *sb);
static unsigned [LNAME]__hash([LNAME] *instance);
static void [LNAME]__destroy([LNAME] *instance);

static [LNAME]_vtable vtable = {
    .get_length = [LNAME]__get_length,
    .set_length = [LNAME]__set_length,
    .func3 = [LNAME]__func3,
    .equals = [LNAME]__equals,
    .to_string = [LNAME]__to_string,
    .hash = [LNAME]__hash,
    .destroy = [LNAME]__destroy
};

[LNAME] *new_[LNAME](arena *arena) {
    // one pointer holds space for both the public and private parts
    void *ptr = arena->alloc([UNAME]_MEMORY_SIZE());

    [LNAME] *instance = ([LNAME] *)ptr;
    instance->vt = &vtable;

    [LNAME]_private_data *data = [UNAME]_PRIVATE_DATA(instance);
    memset(data, 0, sizeof([LNAME]_private_data));
    data->arena = arena;


    return instance;
}

static int [LNAME]__get_length([LNAME] *instance) {
    if (instance == NULL)
        return -1;
    [LNAME]_private_data *data = [UNAME]_PRIVATE_DATA(instance);

    // do work here...
    return data->length;
}

static void [LNAME]__set_length([LNAME] *instance, int length) {
    if (instance == NULL)
        return;
    [LNAME]_private_data *data = [UNAME]_PRIVATE_DATA(instance);

    // do work here...
    data->length = length;
}

static char *[LNAME]__func3([LNAME] *instance, char *arg1) {
    if (instance == NULL)
        return NULL;
    [LNAME]_private_data *data = [UNAME]_PRIVATE_DATA(instance);

    // do work here...
    
    return arg1;
}

static int [LNAME]__equals([LNAME] *instance, [LNAME] *other) {
    if (instance == NULL)
        return (other == NULL);
    [LNAME]_private_data *data = [UNAME]_PRIVATE_DATA(instance);
    [LNAME]_private_data *other_data = [UNAME]_PRIVATE_DATA(other);

    if (data != other_data)
        return false;
    if (data->length != other_data->length)
        return false;
    
    return true;
}

static void [LNAME]__to_string([LNAME] *instance, string_builder *sb) {
    if (instance == NULL || sb == NULL)
        return;
    [LNAME]_private_data *data = [UNAME]_PRIVATE_DATA(instance);

    sb->vt->appendf("[LNAME](length=%d)", data->length);
}

static unsigned [LNAME]__hash([LNAME] *instance) {
    if (instance == NULL)
        return 0;
    [LNAME]_private_data *data = [UNAME]_PRIVATE_DATA(instance);

    unsigned hash = 0;
    // calculate hash for private data

    return hash;
}

static void [LNAME]__destroy([LNAME] *instance) {
    if (instance == NULL)
        return;
    [LNAME]_private_data *data = [UNAME]_PRIVATE_DATA(instance);

    // destroy private data here (e.g. close files)

    data->arena->free(instance);
}
