
#include "LinkedList.h"

static void test_LinkedList_constructor(Arena *a) {
    LinkedList *instance = new_LinkedList(a);
    assert(instance);
}

static void test_LinkedList_hash(Arena *a) {
    LinkedList *instance = new_LinkedList(a);
    instance->vt->hash(instance);
    assert(1);
}

static void test_LinkedList_equals(Arena *a) {
    LinkedList *instance = new_LinkedList(a);
    instance->vt->equals(instance);
    assert(1);
}

static void test_LinkedList_to_string(Arena *a) {
    LinkedList *instance = new_LinkedList(a);
    instance->vt->to_string(instance);
    assert(1);
}

static void test_LinkedList_serialize(Arena *a) {
    LinkedList *instance = new_LinkedList(a);
    instance->vt->serialize(instance);
    assert(1);
}

static void test_LinkedList_unserialize(Arena *a) {
    LinkedList *instance = new_LinkedList(a);
    instance->vt->unserialize(instance);
    assert(1);
}

static void test_LinkedList_destroy(Arena *a) {
    LinkedList *instance = new_LinkedList(a);
    instance->vt->destroy(instance);
    assert(1);
}

void test_LinkedList(Arena *a) {
    test_LinkedList_constructor(a);
    test_LinkedList_hash(a);
    test_LinkedList_equals(a);
    test_LinkedList_to_string(a);
    test_LinkedList_serialize(a);
    test_LinkedList_unserialize(a);
    test_LinkedList_destroy(a);
}
