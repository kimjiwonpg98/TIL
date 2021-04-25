function solution(s) {
  const sToLower = s.toLowerCase().split("");

  let pp, yy;
  pp = yy = 0;

  for (let seq of sToLower) {
    if (seq === "p") {
      pp++;
    } else if (seq === "y") {
      yy++;
    }
  }

  return pp === yy;
}
