var containsDuplicate = function(nums) {
    var numsSet = new Set();
    for (i=0; i<nums.length ; i++){
if(numsSet.has(nums[i])){
    return true;
}
else {
    numsSet.add(nums[i]);

}



    }
        return false;

    
};