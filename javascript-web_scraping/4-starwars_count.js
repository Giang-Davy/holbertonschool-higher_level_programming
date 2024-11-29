#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body);
    let count = 0;

    console.log('Films fetched:', films.results.length); // Affiche le nombre de films récupérés pour le débogage

    films.results.forEach(film => {
      console.log('Checking film:', film.title); // Affiche chaque titre de film pour le débogage
      if (film.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        count++;
      }
    });

    console.log(count);
  } else {
    console.log('Error:', response.statusCode);
  }
});
