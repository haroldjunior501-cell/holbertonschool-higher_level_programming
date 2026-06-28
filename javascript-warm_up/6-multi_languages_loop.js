#!/usr/bin/node
// Loop to languages
const languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let output = '';

for (let i = 0; i < languages.length; i++) {
  output += `${languages[i]}\n`;
}

console.log(output.trim());
