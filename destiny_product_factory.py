import subprocess
import time

print("Destiny Product Factory Starting...")

while True:

    print("Generating new products...")
    subprocess.run(["python", "pdf_product_generator.py"])

    print("Uploading products to Stripe...")
    subprocess.run(["python", "stripe_pdf_uploader.py"])

    print("Updating store page...")
    subprocess.run(["python", "sales_page_generator.py"])

    print("Uploading updated store to GitHub...")
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "store update"])
    subprocess.run(["git", "push"])

    print("Cycle complete. Waiting 1 hour before next run.")

    time.sleep(3600)
