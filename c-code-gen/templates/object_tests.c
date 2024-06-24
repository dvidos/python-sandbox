#include "[LNAME].h"


static void test__get_length() {
    arena *a = new_arena();
    [LNAME] *instance = new_[LNAME](a);
    assert(instance->vt->get_length() == 0);
    a->vt->destroy();
}

static void test__set_length() {

}

static void test__func3() {

}

static void test__equals() {

}

static void test__to_string() {

}

static void test__hash() {

}

static void test__destroy() {

}

void [LNAME]_tests() {
    test__get_length();
    test__set_length();
    test__func3();
    test__equals();
    test__to_string();
    test__hash();
    test__destroy();
}

