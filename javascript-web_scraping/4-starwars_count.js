#!/usr/bin/node
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log('Data:', data);
    let count = 0;

    if (data.results) {
      data.results.forEach(film => {
        console.log(film.characters);
        if (film.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
          count++;
        }
      });
    }

    console.log(count);
  } else {
    console.log('Error:', response.statusCode);
  }
});
