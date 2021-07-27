function solution(n) {
  let number = 1;
  while (1) {
    if (Math.pow(number, 2) === n) return Math.pow(number + 1, 2);
    if (Math.pow(number, 2) > n) return -1;
    number += 1;
  }
}
