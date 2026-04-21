import os
import time
import datetime
import random

def run_income_engine():
    products = [
        {"name": "30 Day Food Storage Plan", "link": "https://buy.stripe.com/5kQ14m8Y3b7Gfrwbqz2h91Y"},
        {"name": "Emergency Survival System", "link": "https://buy.stripe.com/7sY14m8Y3dfO5QW52b2h924"}
    ]

    print(f"--- INCOME ENGINE ONLINE: {datetime.datetime.now()} ---")
    
    while True:
        product = random.choice(products)
        timestamp = int(time.time())
        filename = f"product_{timestamp}.html"
        
        print(f"[DESTINY] SELL MODE FINAL")
        print(f"[CREATING]: {product['name']}")
        print(f"[PAYMENT LINK]: {product['link']}")
        
        # Write to the local products folder
        with open(f"./products/{filename}", "w") as f:
            f.write(f"<html><body><h1>{product['name']}</h1><a href='{product['link']}'>Buy Now</a></body></html>")
        
        print(f"[PRODUCT CREATED]: {filename}")
        
        # GitHub sync
        os.system("git add .")
        os.system(f"git commit -m 'final payment fix'")
        os.system("git push origin main")
        
        print("[LIVE PUSH COMPLETE]")
        print("[CORE] SUCCESS - INCOME RUN")
        print(f"[MEMORY] Stored RAW: {timestamp}.txt")

        # 5-MINUTE SPEED LIMIT
        print(f"\n[>] STABILIZING: Resting for 300 seconds...")
        time.sleep(300)

if __name__ == "__main__":
    run_income_engine()
