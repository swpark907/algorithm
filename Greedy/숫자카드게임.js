const inputExample = ["3 1 2", "4 1 4", "2 2 2"];
let answer = 0;
for (a of inputExample) {
  if (answer < Math.min(...a.split(" ").map(Number)))
    answer = Math.min(...a.split(" ").map(Number));
}

console.log(answer);
