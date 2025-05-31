/**
 * 309. Best Time to Buy and Sell Stock with Cooldown
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
 * You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may buy and sell one NeetCoin multiple times with the following restrictions:

After you sell your NeetCoin, you cannot buy another one on the next day (i.e., there is a cooldown period of one day).
You may only own at most one NeetCoin at a time.
You may complete as many transactions as you like.

Return the maximum profit you can achieve.

Example 1:

Input: prices = [1,3,4,0,4]

Output: 6
Explanation: Buy on day 0 (price = 1) and sell on day 1 (price = 3), profit = 3-1 = 2. Then buy on day 3 (price = 0) and sell on day 4 (price = 4), profit = 4-0 = 4. Total profit is 2 + 4 = 6.
 */

class Solution {
public:
    int DFS(vector<int>& prices,unordered_map<long,int>& mp, bool isBuying ,int i)
    {
        if(i>= prices.size())
        {
            return 0;
        }
        
        long p = static_cast<long>(i) << 1 | static_cast<long>(isBuying);
        if(mp.count(p) >0)
        {
            return mp[p];
        }
        int cool = DFS(prices,mp,isBuying,i+1);
        if(isBuying)
        {
            int buy = DFS(prices,mp,!isBuying,i+1) - prices[i];
            mp[p] = max(buy,cool);
        }
        else
        {
            int sell = DFS(prices,mp,!isBuying,i+2) + prices[i];
            mp[p] = max(sell,cool);
        }
        return mp[p];
    }
    int maxProfit(vector<int>& prices) {
        unordered_map<long,int> mp;
        bool isBuying = true;
        return DFS(prices,mp,isBuying,0);
    }
};
