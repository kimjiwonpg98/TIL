function solution(absolutes, signs) {
  return absolutes.reduce((pre, sec, i) => {
    if (!signs[i]) sec *= -1;
    return pre + sec;
  }, 0);
}
