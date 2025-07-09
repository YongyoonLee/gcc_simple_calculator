#include <iostream>
#include "add.h"
#include "subtract.h"
#include "multiply.h"
#include "divide.h"

int main() {
    double num1, num2;
    char op;

    std::cout << "input the first number: ";
    std::cin >> num1;
    std::cout << "input the operator(+ - * /): ";
    std::cin >> op;
    std::cout << "input the seconde number: ";
    std::cin >> num2;

    double result = 0.0;
    bool valid = true;

    switch (op) {
        case '+':
            result = add(num1, num2);
            break;
        case '-':
            result = subtract(num1, num2);
            break;
        case '*':
            result = multiply(num1, num2);
            break;
        case '/':
            if (num2 == 0) {
                std::cout << "cannot divide by 0." << std::endl;
                valid = false;
            } else {
                result = divide(num1, num2);
            }
            break;
        default:
            std::cout << "the operator is not supported." << std::endl;
            valid = false;
    }

    if (valid) {
        std::cout << "result: " << result << std::endl;
    }

    return 0;
}