const [N, M, K] = "5 8 3".split(" ").map(Number);
let arr = [2, 4, 5, 4, 6];

arr.sort((a, b) => b - a);
const result =
  (arr[0] * K + arr[1]) * Math.floor(M / (K + 1)) + (M % (K + 1)) * arr[0];

console.log(result);
