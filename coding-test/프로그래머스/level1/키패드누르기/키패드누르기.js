function solution(numbers, hand) {
  const leftNums = [1, 4, 7];
  const rightNums = [3, 6, 9];
  const middleNums = [2, 5, 8, 0];

  let rightHand = [2, 3];
  let leftHand = [0, 3];
  let middleHand = [1, 0];

  let result = "";

  numbers.forEach((num) => {
    let findRight = rightNums.indexOf(num);
    let findLeft = leftNums.indexOf(num);

    if (findRight !== -1) {
      result += "R";
      if (findRight === 0) rightHand = [2, 0];
      if (findRight === 1) rightHand = [2, 1];
      if (findRight === 2) rightHand = [2, 2];
    } else if (findLeft !== -1) {
      result += "L";
      if (findLeft === 0) leftHand = [0, 0];
      if (findLeft === 1) leftHand = [0, 1];
      if (findLeft === 2) leftHand = [0, 2];
    } else {
      let middleNum = middleNums.indexOf(num);
      middleHand[1] = middleNum;

      let rightCount =
        Math.abs(rightHand[0] - middleHand[0]) +
        Math.abs(rightHand[1] - middleHand[1]);
      let leftCount =
        Math.abs(leftHand[0] - middleHand[0]) +
        Math.abs(leftHand[1] - middleHand[1]);

      if (rightCount === leftCount) {
        if (hand === "right") {
          result += "R";
          rightHand = [1, middleNum];
        } else {
          result += "L";
          leftHand = [1, middleNum];
        }
      } else if (rightCount > leftCount) {
        result += "L";
        leftHand = [1, middleNum];
      } else {
        result += "R";
        rightHand = [1, middleNum];
      }
    }
  });

  return result;
}
