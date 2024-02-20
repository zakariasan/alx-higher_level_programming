#!/usr/bin/node
const req = require('request');

function getStatus (url) {
  req(url, (_err, _res, body) => {
    const doneTask = {};
    body = JSON.parse(body);
    for (let i = 0; i < body.length; i++) {
      const id = body[i].userId;
      const done = body[i].completed;
      if (done && !doneTask[id]) doneTask[id] = 0;
      if (done) ++doneTask[id];
    }
    console.log(doneTask);
  });
}

if (process.argv.length !== 3) {
  console.log('Usage: ./0-statuscode.js <url_path>');
} else {
  getStatus(process.argv[2]);
}
