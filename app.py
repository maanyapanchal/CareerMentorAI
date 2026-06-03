import streamlit as st
from groq import Groq

client = Groq(
    api_key="Your Groq API KEY"
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
