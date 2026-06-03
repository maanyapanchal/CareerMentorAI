import streamlit as st
from groq import Groq
import os

st.set_page_config(
    page_title="CareerMentor AI",
    layout="wide"
)

st.markdown("""
<style>

.stButton > button {
    background-color: #8B5E3C;
    color: white;
    border-radius: 8px;
    border: none;
}

.stButton > button:hover {
    background-color: #6F472D;
    color: white;
}

div[data-testid="stSidebar"] {
    background-color: #F5EBDD;
}

</style>
""", unsafe_allow_html=True)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
st.title("CareerMentor AI")

st.markdown("""
### Interview Preparation and Performance Analysis Platform

Generate company-specific interview questions, evaluate responses,
and improve interview performance through AI-powered feedback.
""")

with st.sidebar:

    st.header("Interview Configuration")

    role = st.selectbox(
        "Select Role",
        [
            "Software Engineer",
            "Python Developer",
            "Frontend Developer",
            "Backend Developer",
            "Data Analyst",
            "Data Scientist"
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
        placeholder="DBMS, Python, OOP, Operating Systems"
    )

    difficulty = st.selectbox(
        "Select Difficulty",
        ["Easy", "Medium", "Hard"]
    )

st.subheader("Interview Generator")
generate_clicked = st.button("Generate Questions")

if generate_clicked:

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

                st.markdown(
                    f"""
                    <div style="
                        background-color:#FDF8F2;
                        padding:20px;
                        border-radius:10px;
                        color:#3E2C23;
                        border:1px solid #E8DCCB;
                    ">
                    {output}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        except Exception as e:
            st.error(f"Error: {e}")

st.divider()

st.header("Performance Analyzer")

question = st.text_area(
    "Question to Evaluate",
    placeholder="Paste a generated interview question"
)

user_answer = st.text_area(
    "Your Interview Answer",
    placeholder="Write your answer here"
)

if st.button("Analyze Response"):

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
        """

        try:

            with st.spinner("Analyzing response..."):

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

                st.success("Analysis Complete!")

                st.markdown(
                    f"""
                    <div style="
                        background-color:#FDF8F2;
                        padding:20px;
                        border-radius:10px;
                        color:#3E2C23;
                        border:1px solid #E8DCCB;
                    ">
                    {evaluation}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        except Exception as e:
            st.error(f"Error: {e}")

st.divider()

st.caption(
    "CareerMentor AI | Built using Python, Streamlit, Groq API, and Llama 3.3"
)
