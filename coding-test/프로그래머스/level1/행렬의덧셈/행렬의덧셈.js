function solution(firstArr, secondArr) {
  for (let i = 0; i < firstArr.length; i++) {
    for (let j = 0; j < firstArr[i].length; j++) {
      firstArr[i][j] += secondArr[i][j];
    }
  }
  console.log(firstArr);
}

function solution(firstArr, secondArr) {
  return firstArr.map((a, i) => a.map((b, j) => b + secondArr[i][j]));
}

solution([[1], [2]], [[3], [4]]);
