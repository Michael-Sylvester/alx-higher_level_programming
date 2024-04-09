#!/usr/bin/node

let num1, num2;

if (process.argv[2] !== undefined && process.argv[3] !== undefined) {
  num1 = parseInt(process.argv[2]);
  num2 = parseInt(process.argv[3]);
  console.log(add(num1, num2));
} else {
  console.log(NaN);
}

function add (a, b) {
  return (a + b);
}
