import pandas as pd
import json

# Load the cleaned CSV
df = pd.read_csv("clean_pixar_dialogue.csv")

# Function to convert data into chat-style fine-tuning format
def format_for_chat_finetune(row):
    return {
        "messages": [
            {"role": "system", "content": "You are an AI trained to write Pixar-style dialogue."},
            {"role": "user", "content": f'{row["Character"]} ({row["Movie"]}): "{row["Dialogue"]}"'},
            {"role": "assistant", "content": f'{row["Emotion"]} - {row["Context"]}'}
        ]
    }

# Apply formatting
formatted_data = df.apply(format_for_chat_finetune, axis=1).tolist()

# Save as JSONL
with open("pixar_dialogue_finetune.jsonl", "w") as f:
    for entry in formatted_data:
        f.write(json.dumps(entry) + "\n")

print("\n✅ Data conversion complete! JSONL file saved as 'pixar_dialogue_finetune.jsonl'.")
