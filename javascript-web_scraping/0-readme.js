#!/usr/bin/node
// 0-readme.js
const fs = require('fs');

// Get the file path from the first command-line argument
const filePath = process.argv[2];

// Use fs.readFile to read the file asynchronously in utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err); // If an error occurs, print the error object
  } else {
    console.log(data); // Otherwise, print the file content
  }
});

