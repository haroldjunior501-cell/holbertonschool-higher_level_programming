#!/usr/bin/node
// I love C
const arg = process.argv[2];
const num = parseInt(arg, 10);

if (Number.isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  let output = '';
  for (let i = 0; i < num; i++) {
    output += 'C is fun\n';
  }
  if (output) {
    console.log(output.trim());
  }
}
