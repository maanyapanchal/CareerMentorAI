import streamlit as st
from groq import Groq

import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


st.title("CareerMentor AI")

st.subheader("AI Powered Career Preparation and Interview Assistance Platform")

st.write(
    "Generate company-specific interview questions and answers "
    "based on role, topic, and difficulty."
)


role = st.selectbox(
    "Select Role",
    [
        "Software Engineer",
        "Python Developer",
        "Frontend Developer",
        "Data Analyst",
        "Data Scientist",
        "Backend Developer"
    ]
)


company = st.selectbox(
    "Select Company",
    [
        "General",
        "Infosys",
        "TCS",
        "Wipro",
        "Accenture",
        "Amazon",
        "Google",
        "Microsoft"
    ]
)


topic = st.text_input(
    "Enter Topic",
    placeholder="Example: DBMS, Python, OOP, Operating Systems"
)


difficulty = st.selectbox(
    "Select Difficulty",
    ["Easy", "Medium", "Hard"]
)


if st.button("Generate Questions"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:

        prompt = f"""
        Generate 5 {difficulty} level interview questions
        for a {role} role on the topic {topic}.

        The interview style should match {company} company interviews.

        For each question:
        1. Provide the question.
        2. Provide a short beginner-friendly answer.
        3. Explain the answer briefly.

        Format the output clearly.
        """

        try:
            with st.spinner("Generating interview questions..."):

                response = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    model="llama-3.3-70b-versatile"
                )

                output = response.choices[0].message.content

                st.success("Questions Generated Successfully!")

                st.subheader("Generated Questions and Answers")

                st.write(output)

        except Exception as e:
            st.error(f"Error: {e}")


st.markdown("---")
st.caption("CareerMentor AI | Built using Python, Streamlit, and Groq LLM API")

st.markdown("---")
st.header("Quick Self-Assessment")

st.info(
    "Choose one of the generated interview questions above, "
    "write your own answer, and receive AI-powered feedback "
    "on accuracy, completeness, and communication skills."
)

question = st.text_area(
    "Question to Evaluate",
    placeholder="Paste one of the generated questions here"
)

user_answer = st.text_area(
    "Your Interview Answer",
    placeholder="Write your answer here"
)

if st.button("Evaluate Answer"):

    if question.strip() == "" or user_answer.strip() == "":
        st.warning("Please enter both the question and your answer.")

    else:

        evaluation_prompt = f"""
        You are an expert technical interviewer.

        Interview Question:
        {question}

        Candidate Answer:
        {user_answer}

        Evaluate the answer on:

        1. Accuracy (out of 10)
        2. Completeness (out of 10)
        3. Communication Clarity (out of 10)

        Then provide:

        - Overall Assessment
        - Strengths
        - Weaknesses
        - Suggested Improvements
        - Improved Model Answer

        Format the response clearly using headings.
        """

        try:

            with st.spinner("Evaluating Answer..."):

                response = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": evaluation_prompt
                        }
                    ],
                    model="llama-3.3-70b-versatile"
                )

                evaluation = response.choices[0].message.content

                st.success("Evaluation Complete!")

                st.subheader("Interview Feedback")

                st.write(evaluation)

        except Exception as e:
            st.error(f"Error: {e}")
