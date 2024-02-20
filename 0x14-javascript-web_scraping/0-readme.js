#!/usr/bin/node
const fs = require('fs');

function readFile (fPath) {
  fs.readFile(fPath, 'utf8', (err, data) => {
    if (err) {
      console.log(err);
      return;
    }
    console.log(data);
  });
}

if (process.argv.length !== 3) {
  console.log('Usage: ./0-readme.js <file_path>');
} else {
  readFile(process.argv[2]);
}
