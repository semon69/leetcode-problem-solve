const removeDuplicates = (nums) => {
//   let without_dup = [];
  // for(i = 0; i<nums.length; i++){
  //     if(!without_dup.includes(nums[i])){
  //         without_dup.push(nums[i])
  //     }
  // }
  let k =0;
  nums.map((num) => {
    if (without_dup.includes(num)) {
      return without_dup
    } else(
        without_dup.push(num)
    )
  });
  return without_dup.length
};

const removeDuplicates2 = (nums) => {
  
    if (nums.length === 0) return 0;

    let slowPointer = 0;

    for (let fastPointer = 1; fastPointer < nums.length; fastPointer++) {
        if (nums[fastPointer] !== nums[slowPointer]) {
            slowPointer++;
            nums[slowPointer] = nums[fastPointer];
        }
    }

    return slowPointer + 1;
};


