request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log('Data:', data);  // Affiche la réponse complète de l'API
    let count = 0;

    if (data.results) {
      data.results.forEach(film => {
        console.log(film.characters);  // Affiche la liste des personnages pour chaque film
        if (film.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
          count++;
        }
      });
    }

    console.log(count);  // Affiche le nombre de films où Wedge Antilles apparaît
  } else {
    console.log('Error:', response.statusCode);
  }
});
