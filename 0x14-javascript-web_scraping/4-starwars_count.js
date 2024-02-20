#!/usr/bin/node
const req = require('request');

function getStatus (url) {
  req(url, (_err, _res, body) => {
    body = JSON.parse(body).results;
    let nbr = 0;
    for (let i = 0; i < body.length; i++) {
      const star = body[i].characters;
      for (let j = 0; j < star.length; j++) {
        const id = star[j].split('/')[5];
        if (id === '18') {
          nbr++;
        }
      }
    }
    console.log(`${nbr}`);
  });
}

if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars.js <url_path>');
} else {
  getStatus(process.argv[2]);
}
