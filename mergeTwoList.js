const aabs = (list1, list2) => {
    // const newlist = [...l1, ...l2];
    // return newlist.sort()

    const merged_array = list1.concat(list2)
    return merged_array.sort()
}
// console.log(aabs([1,2,4], [1,3,4]));
console.log(aabs([], [0]));