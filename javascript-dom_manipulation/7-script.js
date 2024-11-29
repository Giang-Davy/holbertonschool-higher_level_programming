// 7-script.js
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())  // Parse the JSON response
  .then(data => {
    const movieList = document.querySelector('#list_movies');  // Get the <ul> element
    data.results.forEach(movie => {
      const listItem = document.createElement('li');  // Create a new <li> element
      listItem.textContent = movie.title;  // Set the text to the movie title
      movieList.appendChild(listItem);  // Append the <li> to the <ul>
    });
  })
  .catch(error => {
    console.log('Error fetching movies:', error);  // Handle any errors
  });
