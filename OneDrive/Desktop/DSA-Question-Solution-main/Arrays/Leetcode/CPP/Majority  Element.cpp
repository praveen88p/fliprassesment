//majority Element 
// Link - https://leetcode.com/problems/majority-element/
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());

        if(n == 1){
            return nums[0];
        }

        int cnt = 1; 
        for (int i = 1; i < n; i++) {
            if (nums[i] == nums[i - 1]) {
                cnt += 1;
                if (cnt > n / 2) {
                    return nums[i];
                }
            } else {
                cnt = 1; 
            }

        }
        
        
        return -1;
    }
};
