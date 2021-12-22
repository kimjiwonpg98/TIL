function solution(numbers) {
  let result = 45;
  let plus = numbers.reduce((a, b) => a + b);

  return result - plus;
}
