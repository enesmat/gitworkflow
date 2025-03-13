let cart = 0;
let version = '1.0.0';
let environment = 'dev';

document.getElementById = jest.fn(() => ({
  textContent: ''
}));


function addToCart() {
  cart += 1;
  alert('Artikel in den Warenkorb gelegt! Artikel im Warenkorb: ' + cart);
}

function getCart() {
  return cart;
}

// Dynamisches Setzen der Version und Umgebung im Footer
document.getElementById('env-version').textContent = `Version: ${version} | Umgebung: ${environment}`;

module.exports = { addToCart, getCart };
