#!/usr/bin/node
let msg;
if (process.argv[2] !== undefined) {
  msg = process.argv[2];

  msg += ' is ';

  if (process.argv[3] !== undefined) {
    msg += process.argv[3];
    console.log(msg);
  }
}
