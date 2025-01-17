type Fn = (accum: number, curr: number) => number

function reduce(nums: number[], fn: Fn, init: number): number {
    let sumValue = init

    for(let i=0; i< nums.length; i++) {
        sumValue = fn(sumValue, nums[i])
    }
    return sumValue
};