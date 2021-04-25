function solution(strings, n) {
  strings.sort(function (a, b) {
    let first = a[n];
    let second = b[n];
    if (first === second) {
      if (a < b) {
        return -1;
      }
    } else {
      if (first < second) {
        return -1;
      } else {
        return 1;
      }
    }
  });

  return strings;
}
