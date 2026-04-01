class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    scoreOfString(s) {
        let totalVal = 0;
        for(let i = 0; i < s.length-1; i++){
            let init = s.charCodeAt(i);
            let adj = s.charCodeAt(i+1);           
            totalVal += Math.abs(adj - init);
        }
        return totalVal;
    }
}
