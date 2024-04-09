#!/usr/bin/node

let msg = 'My number: ';
let num;
if (process.argv[2] !== undefined) {
  num = parseInt(process.argv[2]);

  if (!isNaN(num)) {
    msg += num;
    console.log(msg);
  } else {
    console.log('Not a number');
  }
}
