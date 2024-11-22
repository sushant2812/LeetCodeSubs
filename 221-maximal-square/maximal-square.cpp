class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        int max_length = 0;
        for(int i=m-1; i>-1; i--){
            for(int j=n-1; j>-1; j--){
                if(matrix[i][j]=='1'){
                    dp[i][j] = 1 + min({dp[i+1][j], dp[i][j+1], dp[i+1][j+1]});
                    max_length=max(max_length,dp[i][j]);
                }
            }
        }
        return max_length*max_length;
    }
};