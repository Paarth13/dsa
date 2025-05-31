/*
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Link : https://leetcode.com/problems/longest-palindromic-subsequence/description/
Scaler Class :https://www.scaler.com/academy/mentee-dashboard/class/7636/session?joinSession=1
*/

class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int s1 = s.size();
        vector<vector<int>> dp(s1,vector<int>(s1,0));
        for(int i =0;i<s1;i++)
        {
            dp[i][i] = 1; 
        }
        int ans =0;
        for(int l=1;l<s1;l++)
        {
            int i = 0;
            int j = l;
            while (i+1<s1 && j<s1)
            {
                if(s[i]==s[j])
                {
                    dp[i][j] = 2+ dp[i+1][j-1];
                }
                else
                {
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1]);
                }
                ans= max(ans,dp[i][j]);
                i++;
                j++;
            }
        }
        for(int i =0;i<s1;i++)
        for(int j=0;j<s1;j++)
        ans = max(ans,dp[i][j]);
        return ans;
    }
};