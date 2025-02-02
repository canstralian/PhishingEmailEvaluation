import numpy as np
from datasets import load_dataset
from transformers import (AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer)
import evaluate
import os

# Ensure the models directory exists.
os.makedirs("models/finetuned-phishing-model", exist_ok=True)

# Load the dataset from CSV files.
data_files = {
    "train": "data/phishing_data.csv",
    "validation": "data/phishing_data_val.csv"
}
dataset = load_dataset("csv", data_files=data_files)

# Define model checkpoint.
model_checkpoint = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

# Tokenization function.
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Map string labels to integers.
label_list = ["safe", "phishing"]
label_to_id = {label: idx for idx, label in enumerate(label_list)}

def convert_labels(example):
    example["label"] = label_to_id[example["label"]]
    return example

tokenized_datasets = tokenized_datasets.map(convert_labels)

# Load model with the appropriate number of labels.
num_labels = len(label_list)
model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint, num_labels=num_labels)

# Define training arguments.
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,
)

# Load accuracy metric.
accuracy_metric = evaluate.load("accuracy")

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return accuracy_metric.compute(predictions=predictions, references=labels)

# Create Trainer.
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    tokenizer=tokenizer,
    compute_metrics=compute_metrics,
)

# Fine-tune the model.
trainer.train()

# Save the fine-tuned model and tokenizer.
model.save_pretrained("models/finetuned-phishing-model")
tokenizer.save_pretrained("models/finetuned-phishing-model")

print("Fine-tuning complete. Model saved in 'models/finetuned-phishing-model'.")
