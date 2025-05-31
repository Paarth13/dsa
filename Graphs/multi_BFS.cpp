// Problem Description

// Given a matrix of integers A of size N x M consisting of 0 or 1.

// For each cell of the matrix find the distance of nearest 1 in the matrix.

// Distance between two cells (x1, y1) and (x2, y2) is defined as |x1 - x2| + |y1 - y2|.

// Find and return a matrix B of size N x M which defines for each cell in A distance of nearest 1 in the matrix A.

// NOTE: There is atleast one 1 is present in the matrix.

/**
 * Example Input

Input 1:

 A = [
       [0, 0, 0, 1]
       [0, 0, 1, 1] 
       [0, 1, 1, 0]
     ]
Input 2:

 A = [
       [1, 0, 0]
       [0, 0, 0]
       [0, 0, 0]  
     ]


Example Output

Output 1:

 [ 
   [3, 2, 1, 0]
   [2, 1, 0, 0]
   [1, 0, 0, 1]   
 ]
Output 2:

 [
   [0, 1, 2]
   [1, 2, 3]
   [2, 3, 4] 
 ]
 */
// Link for question - https://www.scaler.com/academy/mentee-dashboard/class/7414/homework/problems/4705/?navref=cl_pb_nv_tb

vector<vector<int> > Solution::solve(vector<vector<int> > &A) {
    queue<vector<int>> pq;
    int rows = A.size(), cols = A[0].size();
    vector<vector<bool>>vis(rows,vector<bool>(cols,false));
    for(int i =0 ;i<rows;i++)
    {
        for(int j = 0; j<cols;j++)
        {
            if(A[i][j] == 1)
            {
                pq.push({0,i,j});
                vis[i][j] = true;
            }
        }
    }
    vector<vector<int>> DIR {{0,1},{0,-1},{1,0},{-1,0}};
    while(!pq.empty())
    {
        vector<int> v = pq.front();
        pq.pop();
        A[v[1]][v[2]] = v[0];
        for(auto& dir: DIR)
        {
            int r= v[1] + dir[0];
            int c = v[2] + dir[1];
            if(r>=0 && r<rows && c>=0 && c<cols && !vis[r][c])
            {
                pq.push({v[0]+1,r,c});
                vis[r][c] = true;
            }
        }
    }
    return A;
}
