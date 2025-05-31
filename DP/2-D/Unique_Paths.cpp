/**
 * https://leetcode.com/problems/unique-paths/description/
 * There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
 */

class Solution {
public:
    int DFS(vector<vector<int>>& grid, int m, int n, int r, int c)
    {
        if(r<0 || r>=m || c<0 || c>=n)
        {
            return 0;
        } 
        if(r == m-1 && c == n-1)
        {
            return 1;
        }
        if(grid[r][c] == 0)
        {
            vector<vector<int>> pa{
                {0,1},{1,0}
            };
            for(auto p : pa)
            {
                grid[r][c] +=DFS(grid,m,n,r+p[0],c+p[1]);
            }
        }
        return grid[r][c];
    }
    int uniquePaths(int m, int n) {
        vector<vector<int>> grid;
        for(int i =0 ;i<m;i++)
        {
            vector<int> v(n,0);
            grid.push_back(v);
        }
        grid[m-1][n-1] = -1;
        return DFS(grid,m,n,0,0);
    }
};
