#!/usr/bin/node

let big2;
let biggest;
let i = 2;

if (process.argv.length < 4) {
  console.log(0);
} else {
  biggest = parseInt(process.argv[i]);
  big2 = biggest
  for (i = 2; process.argv[i] !== undefined; i++) {
    const temp = parseInt(process.argv[i]);
    if (temp > biggest) {
      biggest = temp;
    }
    if (temp < big2) {
      big2 = temp;
    }
  }
  for (i = 2; process.argv[i] !== undefined; i++) {
    const temp = parseInt(process.argv[i]);
    if (temp < biggest && temp > big2) {
      big2 = temp;
    }
  }
  console.log(big2);
}
