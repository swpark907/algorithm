const arr = [23, 5];
let a = arr[0];
let count = 0;
while (a !== 1) {
  if (a % arr[1] === 0) {
    a = a / arr[1];
  } else {
    a -= 1;
  }
  count++;
}

console.log(count);
