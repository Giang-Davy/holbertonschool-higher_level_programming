#!/usr/bin/node

const fetch = require('node-fetch');

const url = process.argv[2];

fetch(url)
  .then(response => response.json())
  .then(data => {
    let count = 0;
    data.results.forEach(film => {
      if (film.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        count++;
      }
    });
    console.log(count);
  })
  .catch(error => console.error(error));
