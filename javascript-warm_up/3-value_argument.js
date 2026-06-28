#!/usr/bin/node
// Value of my argument
const arg = process.argv[2];

if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
