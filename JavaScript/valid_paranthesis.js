/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    if(s.length %2 !== 0) return false;
    let stack = [];
    for(let i=0; i<s.length;i++){
        // In the conditions push the corresponding closing brackets
        if(s[i] === '('){
            stack.push(')')
        } else if (s[i] === '['){
            stack.push(']')
        } else if (s[i] === '{'){
            stack.push('}')
        } 
        // it will come to this condition if a closing bracket is encountered on traversing, here we will pop the bracket from the stack. Since the order should mathch. Obviously the current looped element must match with the popped element. If it doesn't match, it means a wrong bracket was closed and was not in order and we return false
        else if (stack.length === 0 || stack.pop() !== s[i]){
            return false;
        }
    }
    // here we return true if all the brackets are properly popped and return false if there are more stack elements. This means some opening bracket was not closed properly
    return stack.length === 0 ;
    
    
};