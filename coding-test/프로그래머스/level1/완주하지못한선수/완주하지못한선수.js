function solution(participant, completion) {
  const obj = {};
  for (let player of participant) {
    if (obj[player]) {
      obj[player] += 1;
    } else {
      obj[player] = 1;
    }
  }
  for (let finisher of completion) {
    if (obj[finisher]) {
      obj[finisher] -= 1;
    }
  }
  for (let player of participant) {
    if (obj[player] >= 1) {
      return player;
    }
  }
}
