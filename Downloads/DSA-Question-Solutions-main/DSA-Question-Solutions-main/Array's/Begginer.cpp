
Que = Remove duplicate from sorted Array
LINK = https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/






link- https://leetcode.com/problems/unique-number-of-occurrences/
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
    unordered_map<int,int>mp;
    for(int &x:arr){
        mp[x]++;
    }
    unordered_set<int>st;
    for(auto &it : mp){
        int freq = it.second;

        if(st.find(freq)!=st.end())
        return false;
        st.insert(freq);
    }
 return true;
    }
};



Find all duplicate in a Array
LINK = https://leetcode.com/problems/find-all-duplicates-in-an-array/
class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> ans ;
        for(int i=0;i<nums.size();i++){
            int index = abs(nums[i])-1;
            if(nums[index]<0){
                ans.push_back(abs(nums[i]));

            }
            nums[index]= nums[index]*-1;
        }
        return ans;
    }
};



QUE = Score of a String
LINK = https://leetcode.com/problems/score-of-a-string/

class Solution {
public:
    int scoreOfString(string s) {
        vector<int> arr;
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            arr.push_back((int)s[i]);
        }
        for (int i = 1; i < arr.size(); i++) {
            ans += abs(arr[i - 1] - arr[i]);
        }

        return ans;
    }
};




QUE = MOVE ZEROES
LINK = https://leetcode.com/problems/move-zeroes/
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int j=-1;
        for(int i=0;i<nums.size();i++){
            if(nums[i]==0){
                j=i;
                break;
            }
        }
        if(j==-1){
            return;
        }
        for(int i=j+1;i<nums.size();i++){
            if(nums[i]!=0){
                swap(nums[i],nums[j]);
                j++;
            }
        }
        
    }
};

QUE = Missing number
LINK = https://leetcode.com/problems/missing-number/
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n=nums.size();
        int x = (n*(n+1))/2;
        int y =0;
        for(int i=0;i<n;i++){
          y+=nums[i];
        }
        return x-y;

    }
};

QUE = Max Consequtive Ones 
LINK = https://leetcode.com/problems/max-consecutive-ones/
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        
        int cnt1=0;
        int cnt2 =0;
    for(int i=0;i<nums.size();i++){
        if(nums[i]==1){
            cnt1+=1;
             cnt2 =max(cnt1,cnt2);
        }
        else{
           
            cnt1=0;
        }
        
    }
    return cnt2;
    }
};

QUE = Single Number	
LINK = https://leetcode.com/problems/single-number/	
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans=0;
        for(int i=0;i<nums.size();i++){
          ans = nums[i]^ans;
        }
        return ans;}
};


QUE = TWO SUM
LINK = https://leetcode.com/problems/two-sum/
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int>mpp;
        for(int i =0;i<nums.size();i++){
            int num = nums[i];
            int moreneed= target - num;
            if(mpp.find(moreneed)!=mpp.end()){
                return {mpp[moreneed],i};
            }
            mpp[num]=i;
            

        }
        return {-1,-1};
    }
};
