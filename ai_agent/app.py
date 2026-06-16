import streamlit as st
from utils.resume_parser import extract_text_from_pdf
from utils.prompts import (
    resume_analysis_prompt,
    job_match_prompt,
    career_qa_prompt
)
from utils.llm import call_ollama

st.set_page_config(page_title="AI Career Assistant", layout="wide")

st.title("🤖 AI Career Assistant Agent")

menu = st.sidebar.selectbox(
    "Choose Feature",
    ["📄 Resume Analysis", "📌 Job Matching", "💬 Career Q&A"]
)

# ---------------------------
# 📄 RESUME ANALYSIS
# ---------------------------
if menu == "📄 Resume Analysis":
    st.header("Upload Your Resume")
    file = st.file_uploader("Upload PDF Resume", type=["pdf"])

    if file:
        text = extract_text_from_pdf(file)

        if st.button("Analyze Resume"):
            prompt = resume_analysis_prompt(text)
            response = call_ollama(prompt)
            st.subheader("📊 Analysis Result")
            st.write(response)

# ---------------------------
# 📌 JOB MATCHING
# ---------------------------
elif menu == "📌 Job Matching":
    st.header("Resume vs Job Description")

    file = st.file_uploader("Upload Resume PDF", type=["pdf"])
    job_desc = st.text_area("Paste Job Description")

    if file and job_desc and st.button("Match Resume"):
        resume_text = extract_text_from_pdf(file)

        prompt = job_match_prompt(resume_text, job_desc)
        response = call_ollama(prompt)

        st.subheader("📊 Match Result")
        st.write(response)

# ---------------------------
# 💬 CAREER Q&A
# ---------------------------
elif menu == "💬 Career Q&A":
    st.header("Ask Career / Interview Questions")

    question = st.text_area("Enter your question")

    if question and st.button("Get Answer"):
        prompt = career_qa_prompt(question)
        response = call_ollama(prompt)

        st.subheader("🤖 Answer")
        st.write(response)