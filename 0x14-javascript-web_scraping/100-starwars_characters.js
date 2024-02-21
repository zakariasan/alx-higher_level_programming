#!/usr/bin/node
const req = require('request');

function getStatus (id) {
  const url = `https://swapi-api.hbtn.io/api/films/${id}`;
  req(url, (_err, _res, boddy) => {
    const body = JSON.parse(boddy).characters;
    for (let i = 0; i < body.length; i++) {
      req(body[i], (_err, _res, bodyy) => {
        console.log(JSON.parse(bodyy).name);
      });
    }
  });
}

if (process.argv.length !== 3) {
  console.log('Usage: ./0-statuscode.js <url_path>');
} else {
  getStatus(process.argv[2]);
}
