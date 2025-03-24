import streamlit as st
import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import datetime

# Load model and tokenizer (Microsoft Phi-2)
model_name = "microsoft/phi-2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to("cuda")

# Create or load CSV to save responses
csv_filename = "responses.csv"
try:
    df = pd.read_csv(csv_filename)
except FileNotFoundError:
    df = pd.DataFrame(columns=["Timestamp", "User Query", "AI Response"])
    df.to_csv(csv_filename, index=False)

def generate_response(user_query):
    """
    Retrieves relevant posts and generates a response using Microsoft Phi-2.
    """
    prompt = f"User: {user_query}\n\nAssistant:"
    
    # Tokenize input
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs["input_ids"].to("cuda")
    attention_mask = inputs["attention_mask"].to("cuda")

    # Generate response
    output = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        max_length=300,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.2,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True
    )

    # Decode response
    response_text = tokenizer.decode(output[0], skip_special_tokens=True).strip()

    # Fallback if response is blank
    if not response_text or response_text.lower().startswith("assistant:"):
        response_text = "I'm sorry, I couldn't generate a response. Can you rephrase your question?"

    return response_text

# Streamlit UI
st.title("💬 AI Chatbot")
user_query = st.text_input("Ask something:")

if st.button("Generate Response"):
    if user_query:
        response = generate_response(user_query)

        # Save to CSV
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_data = pd.DataFrame([[timestamp, user_query, response]], columns=["Timestamp", "User Query", "AI Response"])
        new_data.to_csv(csv_filename, mode='a', header=False, index=False)

        # Display response
        st.write("✅ AI Response:")
        st.success(response)
    else:
        st.warning("Please enter a question.")

# Display past responses
if st.checkbox("📜 Show previous responses"):
    df = pd.read_csv(csv_filename)
    st.dataframe(df)
