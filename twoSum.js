const twoSum = (nums, target) => {
   
    //  This code is sorted array
    // let first = 0;
    // let last = nums.length - 1;

    // while (first < last) {
    //     const currentSum = nums[first] + nums[last];
    //     // console.log(currentSum);

    //     if (currentSum === target) {
    //         return [first, last];
    //     } else if (currentSum < target) {
    //         first++;
    //     } else {
    //         last--;
    //     }
    // }

    for (let i = 0; i < nums.length; i++) {
        for (let j = i+1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target) {
                return [i, j]
            }
        }
    }
    return "No Matches";

};
console.log(twoSum([3, 2, 4, 11, 6, 3, 12], 23)); 