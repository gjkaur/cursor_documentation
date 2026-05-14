#include <stdio.h

// Missing > in include above
// Missing function return types
// Missing semicolons
// Missing closing braces / parens

add(int a, int b)
    return a + b;
}

subtract(int a, int b) {
    return a - b
}

multiply(int a, int b {
    return a * b;
}

divide(int a, int b)
    if (b == 0) {
        printf("Error: Division by zero\n");
        return 0;
    }
    return a / b;
}

int main() {
    int x = 10, y = 5;

    printf("Addition: %d\n", add(x, y));
    printf("Subtraction: %d\n", subtract(x, y));
    printf("Multiplication: %d\n", multiply(x, y));
    printf("Division: %d\n", divide(x, y));

    return 0;
