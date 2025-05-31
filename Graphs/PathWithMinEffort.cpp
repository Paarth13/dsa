/**
 * Twist on Djikstra
 * https://leetcode.com/problems/path-with-minimum-effort/
 * 
 * You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
 * 
 */

class Solution {
public:
struct my_comparator
{
    // queue elements are vectors so we need to compare those
    bool operator()(std::vector<int> const& a, std::vector<int> const& b) const
    {

        // reverse sort puts the lowest value at the top    
        return a[0] > b[0];
    }
};
    int minimumEffortPath(vector<vector<int>>& heights) {
        int rows = heights.size(),cols= heights[0].size();
        vector<vector<bool>> vis(rows,vector<bool>(cols,false));
        priority_queue<vector<int>,vector<vector<int>>,my_comparator> pq; //  Here we take min as we want the min effort required
        pq.push({0,0,0});
        vector<vector<int>>DIR {{0,1},{1,0},{-1,0},{0,-1}};
        while(!pq.empty())
        {
            vector<int> v =  pq.top();
            pq.pop();
            if(vis[v[1]][v[2]])
                continue;
            vis[v[1]][v[2]] = true;
            if(v[1] == rows-1 && v[2] == cols-1)
            {
                return v[0];
            }
            for(auto dir : DIR)
            {
                int r = v[1]+dir[0];
                int c = v[2] + dir[1];
                if(r>=0 && r<rows && c>=0 && c<cols && !vis[r][c])
                {
                    int diff = max (v[0],abs(heights[v[1]][v[2]] - heights[r][c])); 
                    pq.push({diff, r,c});
                }
            }
        }
        return -1;
    }
};