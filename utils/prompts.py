def resume_analysis_prompt(resume_text):
    return f"""
You are an expert career coach.

Analyze the following resume:

RESUME:
{resume_text}

Give:
1. Strengths
2. Weaknesses
3. Improvements
4. Skill gaps
Return in clean bullet points.
"""


def job_match_prompt(resume_text, job_desc):
    return f"""
You are an ATS system and career expert.

Compare resume with job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_desc}

Return:
1. Match Percentage (0-100)
2. Matching Skills
3. Missing Skills
4. Suggestions to improve match
"""


def career_qa_prompt(question):
    return f"""
You are a professional career advisor and interview coach.

Question:
{question}

Give a clear, practical answer with examples if needed.
"""