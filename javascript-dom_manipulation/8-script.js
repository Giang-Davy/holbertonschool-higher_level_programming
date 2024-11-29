// 8-script.js
window.onload = () => {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())  // Parse the JSON response
    .then(data => {
      document.querySelector('#hello').textContent = data.hello;  // Set the translation in the #hello element
    })
    .catch(error => {
      console.log('Error fetching translation:', error);  // Handle any errors
    });
};
