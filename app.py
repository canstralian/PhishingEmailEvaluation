import gradio as gr
from transformers import pipeline

# Load the fine-tuned model.
model_path = "models/finetuned-phishing-model"
classifier = pipeline("text-classification", model=model_path, tokenizer=model_path)

def evaluate_url(url):
    result = classifier(url)[0]
    label = result['label']
    score = result['score']
    return f"Label: {label} (confidence: {score:.2f})"

def evaluate_email(email):
    result = classifier(email)[0]
    label = result['label']
    score = result['score']
    return f"Label: {label} (confidence: {score:.2f})"

with gr.Blocks() as demo:
    gr.Markdown("# Phishing Evaluation App Powered by Transformers")
    
    with gr.Tabs():
        with gr.TabItem("URL Evaluation"):
            gr.Markdown("Enter a URL to evaluate if it's phishing or safe.")
            url_input = gr.Textbox(label="Enter URL", placeholder="https://www.example.com")
            url_output = gr.Textbox(label="Evaluation", interactive=False)
            url_btn = gr.Button("Evaluate URL")
            url_btn.click(fn=evaluate_url, inputs=url_input, outputs=url_output)
        
        with gr.TabItem("Email Evaluation"):
            gr.Markdown("Enter an email to evaluate if it's phishing or safe.")
            email_input = gr.Textbox(label="Enter Email", placeholder="user@example.com")
            email_output = gr.Textbox(label="Evaluation", interactive=False)
            email_btn = gr.Button("Evaluate Email")
            email_btn.click(fn=evaluate_email, inputs=email_input, outputs=email_output)

demo.launch()
