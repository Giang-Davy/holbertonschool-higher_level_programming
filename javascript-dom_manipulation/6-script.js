// 6-script.js
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())  // Parse the JSON from the response
  .then(data => {
    document.querySelector('#character').textContent = data.name;  // Set the character name to the #character element
  })
  .catch(error => {
    console.log('Error fetching character:', error);  // Handle any errors
  });
