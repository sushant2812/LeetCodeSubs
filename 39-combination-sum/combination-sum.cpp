class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> tmp;
        backtrack(candidates, target, 0, 0, tmp, res);
        return res;
    }

private:
    void backtrack(vector<int>& candidates, int target, int idx, int sum, vector<int>& tmp, vector<vector<int>>& res) {
        // If the current sum equals target, add the current combination to the result
        if (sum == target) {
            res.push_back(tmp);
            return;
        }

        // If the sum exceeds target or we've processed all candidates, return
        if (sum > target || idx >= candidates.size()) {
            return;
        }

        // Include the current candidate (same index allowed for reuse)
        tmp.push_back(candidates[idx]);
        backtrack(candidates, target, idx, sum + candidates[idx], tmp, res); // Continue with the same index

        // Backtrack: remove the last element and try the next index
        tmp.pop_back();
        
        // Try the next candidate
        backtrack(candidates, target, idx + 1, sum, tmp, res);
    }
};
