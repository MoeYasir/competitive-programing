/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function(operations) {
    let num = 0;
    for (i=0; i<operations.length;i++){

if(operations[i].includes("--")){
    num = num -1;
}
if(operations[i].includes("++")){
    num = num +1
}


    }
    return num
};
