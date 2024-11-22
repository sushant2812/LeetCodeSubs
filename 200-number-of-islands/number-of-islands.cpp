class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int res = 0;
        for(int i=0; i<rows; i++){
            for(int j=0; j<cols; j++){
                if(grid[i][j]=='1'){
                    res+=1;
                    dfs(i,j,rows,cols, grid);
                }
            }
        }
        return res;
    }
    void dfs(int i, int j, int rows, int cols, vector<vector<char>>& grid){
        if((i<0 || i>=rows) || (j<0 || j>=cols) || grid[i][j]=='0') return;
        grid[i][j]='0';
        dfs(i+1,j,rows,cols, grid);
        dfs(i,j+1,rows,cols, grid);
        dfs(i-1,j,rows,cols, grid);
        dfs(i,j-1,rows,cols, grid);
    }
};