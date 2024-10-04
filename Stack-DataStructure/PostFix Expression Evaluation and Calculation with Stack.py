#include <iostream>
#include <stack>
#include <map>
#include <vector>
using namespace std;

string InFixConverision(string InFix)
{
    map<char, int> precedence;
    string PostFix = "";
    vector<char> Operators = {'(', ')', '+', '-', '/', '*', '^'};
    stack<char> st;

    precedence['+'] = 1;
    precedence['-'] = 1;
    precedence['*'] = 2;
    precedence['/'] = 2;
    precedence['^'] = 3;

    for (int i = 0; i < InFix.length(); i++)
    {
        char currChar = InFix[i];

        if (find(Operators.begin(), Operators.end(), currChar) == Operators.end())
        {
            char topValue = st.top();
            PostFix += topValue;
            st.pop();
        }
        else if (currChar == '(')
        {
            st.push(currChar);
        }

        else if (currChar == ')')
        {

            while (st.top() != '(')
            {
                char topValue = st.top();
                PostFix += topValue;
                st.pop();
            }
            st.pop();
        }

        else
        {
            while (!st.empty() && precedence[st.top()] >= precedence[currChar])
            {
                char topValue = st.top();
                PostFix += topValue;
                st.pop();
            }

            st.push(currChar);
        }
    }

    while (!st.empty())
    {
        PostFix += st.top();
        st.pop();
    }
    return PostFix;
}

int PostFixEvaluation(string PostFix)
{
    stack<char> st;
    vector<char> Operators = {'+', '-', '/', '*', '^'};

    for (int i = 0; i < PostFix.length(); i++)
    {   
        char currChar = PostFix[i];
        if (find(Operators.begin(), Operators.end(), currChar) == Operators.end())
        {
            st.push(currChar);
        }
        else
        {
            int Operand2 = st.top();
            st.pop();
            int Operand1 = st.top();
            st.pop();

            if (currChar == '+')
            {
                st.push(Operand1 + Operand2);
            }
            else if (currChar == '-')
            {
                st.push(Operand1 - Operand2);
            }
            else if (currChar == '/')
            {
                st.push(Operand1 / Operand2);
            }
            else if (currChar == '*')
            {
                st.push(Operand1 * Operand2);
            }
            else if (currChar == '^') 
            { 
                st.push(Operand1 ^ Operand2); 
            }
        }
    }
    int Val = st.top();
    st.pop();
    return Val;
}

int main()
{
    string InFixExpression = "(2-3/4)*(5/6-7)";

    string PostFixExpression = InFixConverision(InFixExpression);

    int EvaluatedAns = PostFixEvaluation(PostFixExpression);
    cout << "Answer : " << EvaluatedAns << endl;
    return 0;
}
