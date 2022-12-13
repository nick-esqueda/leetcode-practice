/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    return validAnagrams(s, t);
};

const validAnagrams = (s, t) => {
  let lettersArr = new Array(26).fill(0)

  for (let i = 0; i < s.length; i++) {
    let letterIdx = s.charCodeAt(i) - 97
    lettersArr[letterIdx]++
  }

  for (let i = 0; i < t.length; i++) {
    let letterIdx = t.charCodeAt(i) - 97
    if (lettersArr[letterIdx] === 0) return false
    lettersArr[letterIdx]--
  }

  return lettersArr.every(el => el === 0)
}