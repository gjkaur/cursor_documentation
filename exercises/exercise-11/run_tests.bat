@echo off
echo Running Tests...
gcc test_calculator.c -o test_calculator.exe
if %errorlevel% neq 0 (
    echo Compilation failed!
    exit /b 1
)
test_calculator.exe
