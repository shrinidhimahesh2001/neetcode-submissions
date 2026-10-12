class Solution {
public:
    int maxProfit(vector<int>& prices)
    {int minimum_price=INT_MAX;
     int max_profit=0;
     for(int p:prices)
        {minimum_price= min(minimum_price,p);
         max_profit=max(max_profit,p-minimum_price);
        }    
     return max_profit;    
    }
};
