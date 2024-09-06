//Continuous subarray sum
//Link = https://leetcode.com/problems/continuous-subarray-sum/submissions/1281953070/?envType=daily-question&envId=2024-06-08

class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> mp;
        mp[0] = -1;
        int s = 0;
        for (int i = 0; i < nums.size(); ++i) {
            s += nums[i];
            int r = s % k;
            if (mp.count(r) && i - mp[r] >= 2) return true;
            if (!mp.count(r)) mp[r] = i;
        }
        return false;
    }
};
