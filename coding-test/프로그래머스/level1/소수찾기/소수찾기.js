function solution(n) {
  const numbers = Array.from({ length: n }, (_, i) => i + 1);

  numbers[0] = 0;

  for (let i = 2; i * i <= n; i++) {
    if (numbers[i - 1]) {
      for (let j = i * i; j <= n; j += i) {
        numbers[j - 1] = 0;
      }
    }
  }

  return numbers.filter((number) => number).length;
}
// 제곱근을 이용해서 품

//2 set으로 품
function solution(n) {
  const set = new Set();

  for (let i = 1; i < n + 1; i += 2) set.add(i);

  set.delete(1);
  set.add(2);

  for (let j = 3; j < Math.sqrt(n); j++) {
    if (set.has(j)) {
      for (let k = j * 2; k <= n; k += j) set.delete(k);
    }
  }

  return set.size;
}
