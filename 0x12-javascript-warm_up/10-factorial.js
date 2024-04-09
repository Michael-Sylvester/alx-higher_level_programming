#!/usr/bin/node

let num;

if (process.argv[2] !== undefined) {
  num = parseInt(process.argv[2]);
  console.log(factorial(num));
} else {
  console.log(1);
}

function factorial (number) {
  if (number !== 0) {
    return (number * factorial(number - 1));
  } else {
    return (1);
  }
}
