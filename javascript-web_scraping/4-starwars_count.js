#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    let count = 0;

    if (data.results) {
      data.results.map(film => {
        if (film.characters.includes('https://swapi-api.hbtn.io/api/people/18/')){
          count++;
	}
      });
    }

    console.log(count);
  } else {
    console.log('Error:', response.statusCode);
  }
});
