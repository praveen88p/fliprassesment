
//LINK - https://leetcode.com/problems/maximum-subarray/
// QuE - Maximum subarray
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum =0;
        int maxi=nums[0];

        for(int i=0;i<nums.size();i++){

           sum = sum+nums[i];
           if(sum<0){
                sum = 0;
            }
            maxi =  max(maxi,sum);

            
        }
        return maxi;
    }
};