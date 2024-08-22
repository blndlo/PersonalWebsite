const listItems = document.querySelectorAll('li');

listItems.forEach(item => {
  const text = item.textContent;
  item.textContent = ''; // Clear original text

  const span = document.createElement('span');
  span.textContent = text;
  item.appendChild(span);
});
