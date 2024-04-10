#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    return;
  }
  fs.readFile(process.argv[3], 'utf8', (err, data2) => {
    if (err) {
      return;
    }
    const FileC = data + data2;
    fs.writeFile(process.argv[4], FileC, (err) => {
      if (err) {
        return (1);
      }
    });
  });
});
