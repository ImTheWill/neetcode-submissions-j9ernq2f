#include <vector>
#include <string>
#include <iostream>

class Solution {
public:
    bool isValid(string s) {
        if(s.length() %2 != 0){
            return false;
        }

        vector<char> vString;
        for(int i =0; i < s.length(); i++){
            if(s[i] == '(' || s[i] =='{' || s[i] == '['){
                vString.push_back(s[i]);
            }else{
                if(vString.empty()){
                    return false;
                }
                char prevChar = vString[vString.size()-1];
                if((prevChar == '(' && s[i] == ')') || prevChar == '{' && s[i] == '}' || prevChar == '[' && s[i] == ']' ){
                    vString.pop_back();
                }
                else{
                    return false;
                }
            }
            
        }
        if(!vString.empty()){
            return false;
        }else{
            return true;
        }
    }
};
