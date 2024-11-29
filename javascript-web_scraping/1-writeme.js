#!/usr/bin/node
// 1-writeme.js
const fs = require('fs');

// Get the file path and content from the command-line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Use fs.writeFile to write the content to the file asynchronously in utf-8 encoding
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.log(err);  // If an error occurs, print the error object
  }
});
