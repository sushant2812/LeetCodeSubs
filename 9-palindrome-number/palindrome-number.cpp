class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0){
            return false;
        }
        long long tmp=x;
        long long palindrome=0;
        int digit;
        while(x!=0){
            digit=x%10;
            palindrome=palindrome*10+digit;
            x=x/10;
        }
        return palindrome==tmp;
    }
};