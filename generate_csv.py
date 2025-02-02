import csv
import os

# Create the data directory if it doesn't exist.
os.makedirs("data", exist_ok=True)

# Sample training data.
train_data = [
    {"text": "https://www.example.com/login", "label": "safe"},
    {"text": "user@example.com", "label": "safe"},
    {"text": "http://phishy-link.com/secure", "label": "phishing"},
    {"text": "phishing@malicious.com", "label": "phishing"},
    {"text": "http://legitimate-website.com", "label": "safe"},
    {"text": "admin@bank-phish.com", "label": "phishing"}
]

# Sample validation data.
val_data = [
    {"text": "https://www.example.com/dashboard", "label": "safe"},
    {"text": "contact@securebank.com", "label": "safe"},
    {"text": "http://dangerous-site.net", "label": "phishing"},
    {"text": "support@fraudulent.com", "label": "phishing"}
]

def write_csv(filename, data):
    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["text", "label"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    print(f"CSV file '{filename}' has been created successfully.")

# Generate training and validation CSV files.
write_csv("data/phishing_data.csv", train_data)
write_csv("data/phishing_data_val.csv", val_data)
