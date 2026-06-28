#!/usr/bin/node
// Square
const arg = process.argv[2];
const size = parseInt(arg, 10);

if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    if (row) {
      console.log(row);
    }
  }
}
