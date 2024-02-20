#!/usr/bin/node
const req = require('request');

function getStatus (id) {
  const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
  req(url, (err, res, body) => {
    if (err) {
      console.log(err);
      return;
    }
    body = JSON.parse(body);
    console.log(`${body.title}`);
  });
}

if (process.argv.length !== 4) {
  console.log('Usage: ./0-statuscode.js <url_path>');
} else {
  getStatus(process.argv[2]);
}
