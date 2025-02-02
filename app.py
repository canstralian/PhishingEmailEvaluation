import gradio as gr

# Define the evaluation functions.
def evaluate_url(url):
    # Placeholder logic for URL evaluation.
    return "This URL is safe" if "example.com" in url else "This URL is suspicious"

def evaluate_email(email):
    # Placeholder logic for email evaluation.
    return "This email is safe" if "example.com" in email else "This email is suspicious"

# Create the app using Blocks and Tabs.
with gr.Blocks() as demo:
    gr.Markdown("# Phishing Evaluation App")
    
    with gr.Tabs():
        # Tab for URL Evaluation.
        with gr.TabItem("URL Evaluation"):
            gr.Markdown("Enter a URL to check if it might be a phishing attempt.")
            url_input = gr.Textbox(label="Enter URL", placeholder="https://www.example.com")
            url_output = gr.Textbox(label="Evaluation", interactive=False)
            url_btn = gr.Button("Evaluate URL")
            # Connect the button to the evaluation function.
            url_btn.click(fn=evaluate_url, inputs=url_input, outputs=url_output)
        
        # Tab for Email Evaluation.
        with gr.TabItem("Email Evaluation"):
            gr.Markdown("Enter an email address to check if it might be a phishing attempt.")
            email_input = gr.Textbox(label="Enter Email", placeholder="user@example.com")
            email_output = gr.Textbox(label="Evaluation", interactive=False)
            email_btn = gr.Button("Evaluate Email")
            # Connect the button to the evaluation function.
            email_btn.click(fn=evaluate_email, inputs=email_input, outputs=email_output)

# Launch the combined app.
demo.launch()
