/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let sorted = strs.map((s) => s.split("").sort().join(""));
        let map = {}
        for (i=0; i<sorted.length; i++){
    if(!map[sorted[i]]){
        map[sorted[i]] = [strs[i]];
    }
    else{
        map[sorted[i]].push(strs[i])
    }
        }
        return Object.values(map);
    };