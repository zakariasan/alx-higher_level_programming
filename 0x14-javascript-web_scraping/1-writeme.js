#!/usr/bin/node
const fs = require('fs');

function readFile(f_path, content) {
	fs.writeFile(f_path, content,'utf8', (err) => {
		if (err) {
			console.log(err);
			return;
		}
		console.log(`${content}`);
	})
}

if (process.argv.length != 4) {
	console.log("Usage: ./1-writeme.js <file_path>");
} else {
	readFile(process.argv[2], process.argv[3]);
}
