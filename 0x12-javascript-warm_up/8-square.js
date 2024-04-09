#!/usr/bin/node

let size;
const errmsg = 'Missing size';

if (process.argv[2] !== undefined) {
  size = Number(process.argv[2]);

  if (isNaN(size)) {
    console.log(errmsg);
  } else {
    for (let i = 0; i < size; i++) {
      let square = '';
      for (let x = 0; x < size; x++) {
        square += 'x';
      }
      console.log(square);
    }
  }
} else {
  console.log(errmsg);
}
