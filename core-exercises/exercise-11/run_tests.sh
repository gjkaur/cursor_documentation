#!/bin/bash
echo "Running Tests..."
gcc test_calculator.c -o test_calculator
if [ $? -ne 0 ]; then
    echo "Compilation failed!"
    exit 1
fi
./test_calculator
