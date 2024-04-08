#!/usr/bin/node
let i;
const msg = 'C is fun';

if (process.argv[2] !== undefined) {
  i = parseInt(process.argv[2]);

  if (isNaN(i)) {
    console.log('Missing number of occurrences');
  } else {
    for (; i > 0; i--) {
      console.log(msg);
    }
  }
}
