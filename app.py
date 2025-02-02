import gradio as gr

# Define the evaluation functions.
def evaluate_url(url):
    # Simulated URL evaluation.
    return "This URL is safe" if "example.com" in url else "This URL is suspicious"

def evaluate_email(email):
    # Simulated email evaluation.
    return "This email is safe" if "example.com" in email else "This email is suspicious"

# Create the app using Blocks and Tabs.
with gr.Blocks() as demo:
    gr.Markdown("# Phishing Evaluation App")
    with gr.Tabs():
        # Tab for URL evaluation.
        with gr.TabItem("URL Evaluation"):
            url_input = gr.Textbox(label="Enter URL", placeholder="https://www.example.com")
            url_output = gr.Textbox(label="Evaluation")
            url_btn = gr.Button("Evaluate URL")
            url_btn.click(fn=evaluate_url, inputs=url_input, outputs=url_output)
        
        # Tab for Email evaluation.
        with gr.TabItem("Email Evaluation"):
            email_input = gr.Textbox(label="Enter Email", placeholder="user@example.com")
            email_output = gr.Textbox(label="Evaluation")
            email_btn = gr.Button("Evaluate Email")
            email_btn.click(fn=evaluate_email, inputs=email_input, outputs=email_output)

# Launch the combined app.
demo.launch()
