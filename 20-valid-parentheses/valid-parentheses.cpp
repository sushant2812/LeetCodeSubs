class Solution {
public:
    bool isValid(string s) {
        bool res = false;
        stack<char> stk;
        unordered_map<char, char> brackets ={{')','('}, {']','['}, {'}','{'}};
        unordered_set<char> openingBrackets = {'(', '{', '['}; 
        for(char c: s){
            if (openingBrackets.count(c)){
                stk.push(c);
            }
            else if(!stk.empty() && stk.top()==brackets[c]){
                stk.pop();
            }
            else{
                return false;
            }
        }
        return stk.size()==0;
    }
};