#!/usr/bin/node

let big2;
let biggest;
let i = 2;

if (process.argv.length < 3) {
  console.log(0);
} else {
  big2 = parseInt(process.argv[i]);
  biggest = big2;

  for (i = 2; process.argv[i] !== undefined; i++) {
    const temp = parseInt(process.argv[i]);
    if (temp > biggest) {
      biggest = temp;
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
