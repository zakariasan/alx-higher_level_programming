#!/usr/bin/node
const req = require('request');

function getStatus (fPath) {
  req.get(fPath, (err, res) => {
    if (err) {
      console.log(err);
      return;
    }
    console.log(`code: ${res.statusCode}`);
  });
}

if (process.argv.length !== 3) {
  console.log('Usage: ./0-statuscode.js <url_path>');
} else {
  getStatus(process.argv[2]);
}
