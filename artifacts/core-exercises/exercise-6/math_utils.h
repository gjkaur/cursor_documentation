#ifndef MATH_UTILS_H
#define MATH_UTILS_H

// Basic arithmetic operations
int add(int a, int b);
int subtract(int a, int b);
int multiply(int a, int b);
int divide(int a, int b);

// Advanced operations
int power(int base, int exp);
int factorial(int n);
int modulo(int a, int b);

// Validation helpers
int is_valid_number(int n);
int is_in_range(int n, int min, int max);

#endif
