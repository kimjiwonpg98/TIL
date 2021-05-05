function solution(nums) {
  const count = nums.length / 2;
  const num = [...new Set(nums)];

  if (num.length > count) return count;
  return num.length;
}
