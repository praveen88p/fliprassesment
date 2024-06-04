LINK= https://leetcode.com/problems/single-number-iii/description/
Question: single-number-iii

  class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        vector<int>ans;
        map<int,int>mp;

        for(int i=0;i<nums.size();i++){
            mp[nums[i]]++;
        }

        for(auto i:mp){
            if(i.second ==1){
                ans.push_back(i.first);
            }
        }
        return ans;
    }
};

QUE = Union of Two Arrays
LINK = https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=union-of-two-sorted-arrays
 class Solution{
    public:
    //arr1,arr2 : the arrays
    // n, m: size of arrays
    //Function to return a list containing the union of the two arrays. 
    vector<int> findUnion(int arr1[], int arr2[], int n, int m)
    {
        //Your code here
        //return vector with correct order of elements
        set<int>st;
        
        for(int i =0;i<n;i++){
            st.insert(arr1[i]);}
            
        for(int i =0;i<m;i++){
            st.insert(arr2[i]);}     
          
          
          vector<int>ans;
           for (auto it = st.begin(); it != st.end(); it++)
             ans.push_back(*it);
             return ans;
    }
};
