function solution(price, money, count) {
  const originalPrice = price;
  while (count > 0) {
    money -= price;
    price += originalPrice;
    count--;
  }
  if (money > 0) return 0;

  return Math.abs(money);
}

solution(3, 20, 4);
