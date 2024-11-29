// 4-script.js
document.querySelector('#add_item').addEventListener('click', function () {
  const newItem = document.createElement('li');  // Create a new <li> element
  newItem.textContent = 'Item';  // Set the text content of the new <li>
  document.querySelector('.my_list').appendChild(newItem);  // Append the new <li> to the <ul>
});
