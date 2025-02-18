# Pixar Dialogue Generator - Fine-Tuned GPT-3.5-Turbo

## 📌 Overview
This project fine-tunes an OpenAI **GPT-3.5-Turbo** model to generate **Pixar-style dialogue** based on character quotes. The model is trained using a small dataset of Pixar movie quotes, formatted in OpenAI's fine-tuning format for chat models.

## 🎬 Features
- Generates **Pixar-style dialogue** in character voices.
- Fine-tuned using a **small dataset of Pixar movie quotes**.
- Uses OpenAI’s fine-tuning methods for **chat models (GPT-3.5-Turbo-0125)**.
- Output follows the structure of a conversational Pixar script.

## 🔧 How It Works
1. **Dataset Preparation**: Pixar movie quotes were formatted into a JSONL dataset.
2. **Fine-Tuning**: The dataset was used to fine-tune an OpenAI GPT-3.5-Turbo model.
3. **Testing**: The model generates Pixar-style dialogue when given prompts.

## 🛠️ Environment Setup

This project requires an `.env` file for storing secrets.  
**Create a `.env` file in the root folder** and add the following:
OPENAI_API_KEY=your-api-key-here

## 🚀 Running the Model
Once the model is fine-tuned, you can generate Pixar-style dialogue using:
```python
import openai

response = openai.ChatCompletion.create(
    model="your-finetuned-model-id",
    messages=[{"role": "user", "content": "Write a Pixar-style dialogue between Woody and Buzz about teamwork."}]
)

print(response["choices"][0]["message"]["content"])
```
(Replace `your-finetuned-model-id` with your actual fine-tuned model ID.)

## 🎯 Limitations
- The dataset size is **small (~20 dialogue pairs)**, so results may be inconsistent.
- Expanding the dataset would improve the model’s accuracy.
- The model lacks true storytelling ability beyond short exchanges.

## 🔮 Future Improvements
- Expand dataset with **more dialogue examples**.
- Add **structured metadata** for better training.
- Experiment with **different fine-tuning techniques**.

## 📜 License
This project is for educational purposes and does not claim ownership over Pixar characters or quotes.

## 🤝 Contributions
Contributions are welcome! Feel free to **fork the repo**, make changes, and submit pull requests.

---
✅ **Author:** [rnaltami](https://github.com/rnaltami)  
🎬 **Project Repo:** [Pixar Dialogue Generator](https://github.com/rnaltami/pixar-dialogue-generator)

