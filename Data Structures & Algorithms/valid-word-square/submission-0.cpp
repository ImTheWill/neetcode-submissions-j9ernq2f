class Solution {
public:
    bool validWordSquare(vector<string>& words) {
        int n = words.size();
        unordered_map<int, string> col;
        unordered_map<int, string> row;
        for(int i = 0; i < n; i++){
            row[i] = words[i];
            for(int j = 0; j < words[i].length(); j++){
                col[j] += words[i][j];
            }
        }
        if(col == row) return true;
        else return false;
    }
};
