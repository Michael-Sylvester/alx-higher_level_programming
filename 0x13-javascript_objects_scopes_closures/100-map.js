#!/usr/bin/node

const list = require('./101-data.js').list;
let listB = [];

for  (let i = 0; i < list.length; i++){
  listB.push(list[i] * i);
}

console.log(list);
console.log(listB);
