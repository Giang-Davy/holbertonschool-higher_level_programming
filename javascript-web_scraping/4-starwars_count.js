#!/usr/bin/node

const fetch = require('node-fetch');

const apiUrl = process.argv[2];

fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    const characterUrl = 'https://swapi-api.hbtn.io/api/people/18/';
    const count = data.results.filter(film => film.characters.includes(characterUrl)).length;
    console.log(count);
  })
  .catch(error => {
    console.error('Error:', error);
  });
