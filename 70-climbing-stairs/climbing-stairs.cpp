class Solution {
public:
    int climbStairs(int n) {
        
        int a =0;
        int b=1;
        int tmp;
        for(int i=1;i<=n;i++){
            tmp=b;
            b=a+b;
            a=tmp;
        }
        return b;
    }
};