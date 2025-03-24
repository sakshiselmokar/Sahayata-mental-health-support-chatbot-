import streamlit as st
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import faiss
import pandas as pd
import os

# Load the model & tokenizer
MODEL_NAME = "microsoft/phi-2"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME).to("cuda")

# Placeholder function for retrieving relevant posts (replace with FAISS retrieval)
def retrieve_filtered_relevant_posts(user_query, df):
    return "Relevant context from dataset based on FAISS retrieval."

def generate_response(user_query, df):
    """
    Retrieves relevant posts and generates a response using Microsoft Phi-2.
    """
    relevant_posts = retrieve_filtered_relevant_posts(user_query, df)

    # Create prompt
    prompt = f"""User: {user_query}  

Assistant: Please provide a thoughtful, helpful response. Keep it concise and relevant.  
"""

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
    response_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return response_text 

# Load dataset (Replace with actual dataset)
df = pd.DataFrame({"text": ["Example Post 1", "Example Post 2"]})

# Streamlit UI
st.title("🧠 Mental Health AI Assistant")
st.write("Enter your thoughts, and let AI assist you.")

user_input = st.text_area("💬 How are you feeling today?", "")

if st.button("Get Support"):
    if user_input:
        response = generate_response(user_input, df)
        st.markdown(f"**🧠 AI Response:**\n{response}")
    else:
        st.warning("Please enter a message to receive a response.")
