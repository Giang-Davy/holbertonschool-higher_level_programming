#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err); // If an error occurs, print the error object
  } else {
    console.log(data); // Otherwise, print the file content
  }
});
