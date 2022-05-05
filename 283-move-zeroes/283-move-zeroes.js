/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
const moveZeroes = (arr) => {
  let i = -1; let j = 0;
  while (j < arr.length) {
    if (arr[j] !== 0) {
      ++i;
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }

    ++j;
  }
  
  return arr
}
