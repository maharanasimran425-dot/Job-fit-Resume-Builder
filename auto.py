from google import genai
import streamlit as st

st.title("JobFit Resume Builder📄")
client = genai.Client(api_key="...............................")

def resume(job,name,email,ph,location,education,skills,project):
   response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
    You are a professional resume writer.

Job Description:{job}
Name: {name}
Email: {email}
Phone: {ph}
location:{location}
education:{education}
Skills: {skills}
project:{project}

        rules:
        - Create a professional, ATS-friendly resume
        - Customize the resume ONLY for the given job description
        - Match skills and experience with JD keywords
        - Write a role-specific professional summary
        - Do NOT create a generic or universal resume
        - Use clear section headings

        Output only the resume content.
"""
        
    )
   return response

name=st.text_input("Enter your name:")
email=st.text_input("Enter your email address")
ph=st.text_input("Enter your phone number")
location=st.text_input("Enter your location")
education=st.text_input("Enter your education")
skills=st.text_area("add your skills")
job = st.text_area("Enter your Job Description")
project=st.text_area("Add your project")
if st.button("Generate"):
    if not name or not job or not ph or not location or not email or not skills or not education :
        st.warning("Please fill all required fields.")
    else:
        with st.spinner("Generating resume..."):
            result = resume(name,job,email, ph,location,education,skills,project)
            st.write(result.text)