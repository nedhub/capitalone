
// Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

// Example

// For inputArray = [3, 6, -2, -5, 7, 3], the output should be
// solution(inputArray) = 21.

// 7 and 3 produce the largest product.



//reminder convert to python code without using numpy library.


function solution(inputArray) {
    let max = -Infinity;
        for (let i = 1; i < inputArray.length; i++) {
            max = Math.max(inputArray[i] * inputArray[i - 1], max);
        }
    
        return max;
    }
    