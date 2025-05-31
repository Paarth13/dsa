/**
 * Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Link - https://leetcode.com/problems/number-of-islands/description/
 */

class Solution {
public:

    void DFS(int i, int j, vector<vector<char>>& grid, vector<vector<int>>& visited,int rows, int cols)
    {
        if(i >= 0 && i<rows && j>=0 && j< cols && visited[i][j]==0 && grid[i][j] == '1' )
        {
            visited[i][j] = 1;
            for(auto itr: dir)
            {
                DFS(i+itr[0],j+itr[1],grid,visited,rows,cols);
            }
        }
    }
    int numIslands(vector<vector<char>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int count = 0;
        vector<vector<int>> visited;
        for(int k=0 ; k<rows ; k++)
        {
            vector<int> v(cols);
            visited.push_back(v);
        }
        for(int i =0 ; i< rows; i++)
        {
            for (int j = 0 ; j<cols;j++)
            {
                if(grid[i][j] == '1' && visited[i][j]== 0)
                {
                    DFS(i,j,grid,visited,rows,cols);
                    count+=1;
                }
            }
        }
        return count;
    }
    vector<vector<int>> dir = {{-1,0},{0,1},{0,-1},{1,0}};
};