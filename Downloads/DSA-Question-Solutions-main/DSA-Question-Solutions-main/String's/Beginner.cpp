QUE = Longest Palindrome
Link = https://leetcode.com/problems/longest-palindrome/

class Solution {
public:
    int longestPalindrome(string s) {
        map<char, int>counts;
        for(char c:s) counts[c]++;

        int result = 0;
        bool odd_found = false;
        for(auto& c: counts){
            if(c.second%2==0) result+=c.second;
            else{
                odd_found = true;
                result+=c.second-1;
            }
        }
        if(odd_found) result++;
        return result;
    }
};
