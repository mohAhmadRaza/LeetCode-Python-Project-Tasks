#include <iostream>
#include <algorithm>
using namespace std;

class Stack
{
private:
    int top;

public:
    int stack[100];

    Stack() { top = -1; }

    void push(int newElement)
    {
        if (IsFull())
        {
            cout << "Stack overflow" << endl;
        }
        else
        {
            stack[++top] = newElement;
        }
    }

    int pop(){
        if (IsEmpty()){
            cout << "Stack is empty" << endl;
            return NULL;
        }
        else{
            return stack[top--];
        }
    }

    bool IsEmpty(){
        if (top == -1){
            return true;
        }
        else{
            return false;
        }
    }

    bool IsFull(){
        if (top >= 99){
            return true;
        }
        else{
            return false;
        }
    }

    int top(){
        return stack[top];
    }
};
