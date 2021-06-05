function solution(n) {
  const array = Array.from(Array(n), (n, i) => Array(i + 1).fill(0));
  let result = [];
  let count = 1;
  let [x, y, direction] = [0, 0, 0];

  while (array[x] !== undefined && array[x][y] === 0) {
    array[x][y] = count;
    count++;

    const nextX = move[direction].x;
    const nextY = move[direction].y;

    if (array[x + nextX] && array[x + nextX][y + nextY] === 0) {
      x += nextX;
      y += nextY;
      continue;
    }

    if (!array[x + move[direction].x] && direction < 3) direction++;

    if (
      array[x + move[direction].x][y + move[direction].y] !== 0 &&
      direction < 3
    )
      direction++;

    if (direction === 3) direction = 0;

    x += move[direction].x;
    y += move[direction].y;
  }

  array.forEach((arrays) => {
    result = [...result, ...arrays];
  });

  return result;
}

const move = [
  { x: 1, y: 0 },
  { x: 0, y: 1 },
  { x: -1, y: -1 },
];
