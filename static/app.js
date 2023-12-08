// Variables globales
let cartItemCount = 0;
let cartPayment = 0;
let coffeesNames = '';


// Selección de elementos del DOM
const addToCartButtons = document.querySelectorAll('[data-btn-action="add-btn-cart"]');
const closeModalButton = document.querySelector('.jsModalClose');
const cartModal = document.querySelector('#jsModalCarrito');
const cartItemsContainer = document.querySelector('.modal__list');
const emptyCartButton = document.querySelector('.btn-border');
const cartCountElement = document.querySelector('.jsCartItemCount');

// Función para agregar un elemento al carrito
function addToCart(itemName, itemPrice, itemImage) {
    // Crear un nuevo elemento para el carrito
    const cartItem = document.createElement('div');
    cartItem.classList.add('modal__item');

    // Estructura del elemento del carrito
    cartItem.innerHTML = `
        <div class="modal__thumb">
            <img src="${itemImage}" alt="${itemName}">
        </div>
        <div class="modal__text-product">
            <p>${itemName}</p>
            <p><strong>${itemPrice}</strong></p>
        </div>
    `;

    // Agregar el elemento al contenedor del carrito
    cartItemsContainer.appendChild(cartItem);

    // Incrementar el contador de productos
    cartItemCount++;

    coffeesNames += itemName + ',';

    // Actualizar el contador en el HTML
    updateCartItemCount();

    // Calcular y actualizar el total
    calculateTotal();

    // Abrir el modal del carrito
    cartModal.classList.add('active');
}

// Función para actualizar el contador de productos en el HTML
function updateCartItemCount() {
    if (cartCountElement) {
        cartCountElement.textContent = cartItemCount;
    }
}

// Función para calcular el total de los elementos en el carrito
function calculateTotal() {
    let total = 0;
    const cartItems = document.querySelectorAll('.modal__item');

    cartItems.forEach(item => {
        const itemPriceString = item.querySelector('.modal__text-product strong').textContent;
        const itemPrice = parseFloat(itemPriceString.replace('$', ''));
        total += itemPrice;
    });

    // Actualizar el elemento HTML que muestra el total
    const totalElement = document.querySelector('.modal__total-cart');
    if (totalElement) {
        totalElement.textContent = `Total: $${total.toFixed(2)}`;
        cartPayment = total;
    }
}

// Evento de clic en los botones "Agregar al carrito"
addToCartButtons.forEach(btn => {
    btn.addEventListener('click', (event) => {
        const itemName = event.target.parentElement.querySelector('.product-grid__name').textContent;
        const itemPrice = event.target.parentElement.querySelector('.product-grid__price').textContent;
        const itemImage = event.target.parentElement.parentElement.querySelector('.product-grid__imagen img').src;

        // Agregar el ítem al carrito
        addToCart(itemName, itemPrice, itemImage);
    });
});

// Evento de clic en el botón "Vaciar carrito"
emptyCartButton.addEventListener('click', () => {
    // Vaciar el contenedor del carrito
    cartItemsContainer.innerHTML = '';

    // Reiniciar el contador de productos
    cartItemCount = 0;

    // Actualizar el contador en el HTML
    updateCartItemCount();

    // Calcular y actualizar el total
    calculateTotal();

    // Cerrar el modal del carrito
    cartModal.classList.remove('active');
});

// Evento de clic en el botón de cerrar el modal
closeModalButton.addEventListener('click', () => {
    cartModal.classList.remove('active');
});

// Cerrar el modal al hacer clic fuera del contenido del modal
window.onclick = (event) => {
    if (event.target == cartModal) {
        cartModal.classList.remove('active');
    }
};

// Agregar evento de clic al botón "Comprar Ahora"
const buyNowButton = document.querySelector('.btn-primary');

buyNowButton.addEventListener('click', () => {
    // Cerrar el modal del carrito
    cartModal.classList.remove('active');

    // Abrir el modal de Pague en OXXO
    const modalOXXO = document.querySelector('#jsModalOXXO');
    modalOXXO.classList.add('active');
});

// Evento de clic en el botón de cerrar el modal de Pague en OXXO
const closeModalOXXOButton = document.querySelector('#jsModalOXXO .jsModalClose');

closeModalOXXOButton.addEventListener('click', () => {
    const modalOXXO = document.querySelector('#jsModalOXXO');
    modalOXXO.classList.remove('active');
});

// Cerrar el modal de Pague en OXXO al hacer clic fuera del contenido del modal
window.onclick = (event) => {
    const modalOXXO = document.querySelector('#jsModalOXXO');
    if (event.target == modalOXXO) {
        modalOXXO.classList.remove('active');
    }
};