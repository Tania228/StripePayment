class StripeCheckoutForm {

    // Обработка платежей через Stripe Checkout

     constructor(itemId, publishableKey) {
        this.itemId = itemId;
        this.publishableKey = publishableKey;
        this.stripe = Stripe(publishableKey);
        this.btn = document.querySelector('.btn');
        this.isProcessing = false;

        this.init();
     }

    // Метод инициализации
    // обработчик событий клика на кнопку покупки
     init() {
        if (this.btn) {
        this.btn.addEventListener('click', (event) => {
            event.preventDefault();
            this.buy();
        })
        }
     }

    // Метод покупки
     async buy() {
        const response = await fetch(`/buy/${this.itemId}/`);
         const data = await response.json();

         this.stripe.redirectToCheckout({ sessionId: data.session_id });
     }
}

// Инициализация при загрузке страницы
document.addEventListener('DOMContentLoaded', () => {
        const btn = document.querySelector('.btn');
        if (btn) {
            const itemId = btn.dataset.itemId;
            const publishableKey = btn.dataset.stripeKey;
            new StripeCheckoutForm(itemId, publishableKey);
        }
})

