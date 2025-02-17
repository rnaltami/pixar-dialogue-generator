import openai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Replace with your actual fine-tuning job ID
fine_tune_job_id = "ftjob-AJsn3HLvRHkvUQDPdmZ030zf"

# Retrieve fine-tuning job details
job_status = openai.fine_tuning.jobs.retrieve(fine_tune_job_id)

# Print fine-tuning status
print(f"\n📌 Fine-Tuning Job Status: {job_status.status}")

# If fine-tuning succeeded, print the model ID
if job_status.status == "succeeded":
    print(f"✅ Fine-tuning completed! Model ID: {job_status.fine_tuned_model}")
elif job_status.status == "failed":
    print("❌ Fine-tuning failed. Check your dataset format and try again.")
else:
    print(f"⏳ Fine-tuning still in progress... Current status: {job_status.status}")
