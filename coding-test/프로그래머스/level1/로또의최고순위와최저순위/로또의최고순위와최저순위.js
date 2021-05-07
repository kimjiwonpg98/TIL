function solution(lottos, winNums) {
  let count = 0;
  let zero = 0;

  lottos.forEach((num) => {
    if (winNums.includes(num)) count++;
    if (num === 0) zero++;
  });

  let high = 7 - (count + zero);
  let low = 7 - count;

  if (zero === 6) low--;
  if (count === 0 && zero === 0) {
    high--;
    low--;
  }

  return [high, low];
}
