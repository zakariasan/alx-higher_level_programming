#!/usr/bin/node
const req = require('request');
const fs = require('fs');

function getStatus (url, file) {
  req(url, (_err, _res, body) => {
    fs.writeFile(file, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  });
}

if (process.argv.length !== 4) {
  console.log('Usage: ./0-statuscode.js <url_path>');
} else {
  getStatus(process.argv[2], process.argv[3]);
}
