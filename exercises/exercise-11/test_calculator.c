#include <stdio.h>
#include <assert.h>

int add(int a, int b) { return a + b; }
int subtract(int a, int b) { return a - b; }
int multiply(int a, int b) { return a * b; }
int divide(int a, int b) {
    if (b == 0) return 0;
    return a / b;
}

void test_add() {
    assert(add(2, 3) == 5);
    assert(add(-1, 1) == 0);
    assert(add(0, 0) == 0);
    printf("PASS: test_add passed\n");
}

void test_subtract() {
    assert(subtract(5, 3) == 2);
    assert(subtract(0, 5) == -5);
    assert(subtract(10, 10) == 0);
    printf("PASS: test_subtract passed\n");
}

void test_multiply() {
    assert(multiply(2, 3) == 6);
    assert(multiply(-2, 3) == -6);
    assert(multiply(0, 5) == 0);
    printf("PASS: test_multiply passed\n");
}

void test_divide() {
    assert(divide(6, 2) == 3);
    assert(divide(5, 2) == 2);
    assert(divide(10, 0) == 0);
    printf("PASS: test_divide passed\n");
}

int main() {
    printf("Running Calculator Tests...\n");
    printf("===========================\n");
    test_add();
    test_subtract();
    test_multiply();
    test_divide();
    printf("===========================\n");
    printf("All tests passed!\n");
    return 0;
}
