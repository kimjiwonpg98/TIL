function solution(n) {
  let min = 0;
  while (n > min) {
    if (n % min === 1) {
      return min;
    }
    min++;
  }
}

solution(12);
