function solution(s) {
  while (isNaN(s)) {
    if (s.includes("zero")) s = s.replace("zero", 0);
    if (s.includes("one")) s = s.replace("one", 1);
    if (s.includes("two")) s = s.replace("two", 2);
    if (s.includes("three")) s = s.replace("three", 3);
    if (s.includes("four")) s = s.replace("four", 4);
    if (s.includes("five")) s = s.replace("five", 5);
    if (s.includes("six")) s = s.replace("six", 6);
    if (s.includes("seven")) s = s.replace("seven", 7);
    if (s.includes("eight")) s = s.replace("eight", 8);
    if (s.includes("nine")) s = s.replace("nine", 9);
  }
  return s;
}

// 2

function solution(s) {
  s = s
    .replace(/zero/gi, 0)
    .replace(/one/gi, 1)
    .replace(/two/gi, 2)
    .replace(/three/gi, 3)
    .replace(/four/gi, 4)
    .replace(/five/gi, 5)
    .replace(/six/gi, 6)
    .replace(/seven/gi, 7)
    .replace(/eight/gi, 8)
    .replace(/nine/gi, 9);
  return parseInt(s);
}
