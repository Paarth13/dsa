/*
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Link : https://leetcode.com/problems/longest-common-subsequence/
Scaler class
https://www.scaler.com/academy/mentee-dashboard/class/7636/session?navref=cl_dd
*/

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        vector<vector<int>> dp(text1.size() + 1, vector<int>(text2.size() + 1,0));
        for(int i =1;i<=text1.size();i++)
        {
            for(int j = 1; j<=text2.size();j++)
            {
                if(text1[i-1] == text2[j-1])
                    dp[i][j]= 1+dp[i-1][j-1];
                else
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1]); 
            }
        }
        return dp[text1.size()][text2.size()];
    }
};
