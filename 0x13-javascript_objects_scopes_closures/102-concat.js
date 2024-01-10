#!/usr/bin/node
// Script that prints “JavaScript is amazing”

const fs = require('fs');
fs.writeFileSync(process.argv[4], fs.readFileSync(process.argv[2]) + fs.readFileSync(process.argv[3], 'utf8'));
console.log(`Files ${process.argv[2]} and ${process.argv[3]} concatenated to ${process.argv[4]}`);
