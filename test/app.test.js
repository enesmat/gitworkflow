// Am Anfang der Datei
global.alert = jest.fn();

// Importieren Sie die zu testenden Funktionen
const { addToCart, getCart } = require('./app');

describe('Shopping Cart Functions', () => {
  beforeEach(() => {
    // Zurücksetzen des Warenkorbs und des alert-Mocks vor jedem Test
    while(getCart() > 0) {
      addToCart(-1);
    }
    global.alert.mockClear();
  });

  test('addToCart erhöht die Anzahl im Warenkorb und ruft alert auf', () => {
    const initialCart = getCart();
    addToCart();
    expect(getCart()).toBe(initialCart + 1);
    expect(global.alert).toHaveBeenCalledWith('Artikel in den Warenkorb gelegt! Artikel im Warenkorb: 1');
  });

  // Weitere Tests...
});
