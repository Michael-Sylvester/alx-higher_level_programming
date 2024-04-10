#!/usr/bin/node

const list = require('./100-data.js').list;
const listB = list.map((num, index) => num * index);

console.log(list);
console.log(listB);
