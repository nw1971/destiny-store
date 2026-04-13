import json
import stripe

def create_checkout_session():
    with open("token.json") as f:
        stripe.api_key = json.load(f)["stripe_api_key"]

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        mode="payment",
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {"name": "Destiny Product"},
                "unit_amount": 1000,
            },
            "quantity": 1,
        }],
        success_url="http://localhost:5000/success",
        cancel_url="http://localhost:5000/cancel",
    )

    return session.url
