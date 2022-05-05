/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
const moveZeroes = (arr) => {
  const newArr = arr.filter(num => num !== 0);
  const numZeros = arr.length - newArr.length;
  
  let i = 0;
  while (i < numZeros) {
    newArr.push(0);
    console.log(newArr)
    ++i;
  }

  newArr.forEach((num, i) => arr[i] = num);
}
