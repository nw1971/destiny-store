import os
import time
from datetime import datetime

def run_income_engine():
    print(f"--- INCOME ENGINE ONLINE: {datetime.now()} ---")
    print("[DESTINY] SELL MODE FINAL")

    # Example product (keep your existing logic if you had more)
    product_name = "Emergency Survival System"
    filename = f"product_{int(time.time())}.html"

    print(f"[CREATING]: {product_name}")

    # Payment link (your system already generates this)
    payment_link = "https://buy.stripe.com/7sY14m8Y3dfO5QW52b2h924"
    print(f"[PAYMENT LINK]: {payment_link}")

    # 🔥 THIS IS THE ONLY FIX (ensures folder exists)
    os.makedirs("./products", exist_ok=True)

    # Write product file
    with open(f"./products/{filename}", "w") as f:
        f.write(f"""
        <html>
        <head><title>{product_name}</title></head>
        <body>
            <h1>{product_name}</h1>
            <p>Get access now:</p>
            <a href="{payment_link}">Buy Now</a>
        </body>
        </html>
        """)

    print(f"[PRODUCT CREATED]: {filename}")

    # Git push (leave as-is, even if warnings happen)
    os.system("git add .")
    os.system("git commit -m 'auto product'")
    os.system("git push")

    print("[LIVE PUSH COMPLETE]")
    print("[CORE] SUCCESS - INCOME RUN")

if __name__ == "__main__":
    run_income_engine()
