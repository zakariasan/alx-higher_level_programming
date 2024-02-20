#!/usr/bin/node
const fs = require('fs');

function readFile (fPath, content) {
  fs.writeFile(fPath, content, 'utf8', (err) => {
    if (err) {
      console.log(err);
      return;
    }
  });
}

if (process.argv.length !== 4) {
  console.log('Usage: ./1-writeme.js <file_path>');
} else {
  readFile(process.argv[2], process.argv[3]);
}
