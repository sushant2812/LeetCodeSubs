#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        string current;
        backtrack(n, 0, 0, current, result);
        return result;
    }

private:
    void backtrack(int n, int left, int right, string& current, vector<string>& result) {
        if(left==right && left==n){
            result.push_back(current);
            return;
        }
        if(left>right){
            current.push_back(')');
            backtrack(n,left,right+1,current,result);
            current.pop_back();
        }
        if(left<n){
            current.push_back('(');
            backtrack(n,left+1,right,current,result);
            current.pop_back();
        }
    }
};
