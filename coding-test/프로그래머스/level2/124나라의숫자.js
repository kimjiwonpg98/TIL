function solution(n) {
  let countryNum = "";

  while (n > 0) {
    let divN = `${parseInt(n % 3)}`;
    n = parseInt(n / 3);
    if (divN === "0") {
      n -= 1;
      divN = "4";
    }

    countryNum = divN + countryNum;
  }
  return countryNum;
}
