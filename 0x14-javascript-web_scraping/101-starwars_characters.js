#!/usr/bin/node
const req = require('request');

function getStatus (id) {
  const url = `https://swapi-api.hbtn.io/api/films/${id}`;
  req(url, (_err, _res, boddy) => {
    const body = JSON.parse(boddy).characters;
    recFun(body, 0);
  });
}

function recFun (star, nbr) {
  req(star[nbr], (_err, _res, by) => {
    console.log(JSON.parse(by).name);
    if (nbr + 1 < star.length) recFun(star, nbr + 1);
  });
}
if (process.argv.length !== 3) {
  console.log('Usage: ./0-statuscode.js <url_path>');
} else {
  getStatus(process.argv[2]);
}
