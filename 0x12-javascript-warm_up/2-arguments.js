#!/usr/bin/node

const { argv } = require('node:process');

const size = argv.length;

if (size < 3) {
  console.log('No argument');
} else if (size === 3) {
  console.log('Argument found');
} else if (size > 3) {
  console.log('Arguments found');
}
