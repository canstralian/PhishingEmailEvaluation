---
title: PhishingEmailEvaluation
emoji: 📈
colorFrom: blue
colorTo: pink
sdk: gradio
sdk_version: 5.14.0
app_file: app.py
pinned: false
short_description: Phishing Email Evaluation
---

# Phishing Detection Project

This project demonstrates a phishing detection application powered by Transformers and served via a Gradio web interface. The project includes:

- **Data Generation:** A script to generate sample CSV datasets.
- **Model Training:** Fine-tuning a Transformer model on a custom phishing dataset.
- **Web App:** A Gradio app with multiple tabs to evaluate URLs and emails.

## Setup Instructions

1. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

2. **Generate Sample Data:**

   ```bash
   python generate_csv.py

3. **Train the Model:**
   ```bash
   python train.py

4. **Run the Web App:**
   ```bash
   python app.py
   ```
Open the provided URL in your browser to interact with the app.

## Notes
- Adjust the dataset and model parameters as needed for your use-case.
- This project uses DistilBERT as a base model; you can swap it with another model if required.