#from streamlit_option_menu import option_menu
from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Muhammed Ajmal P V"
PAGE_ICON = ":wave:"
NAME = "Muhammed Ajmal P V"
DESCRIPTION = """
Machine Learning and Data Science Enthusiast
"""
EMAIL = "pvajmal29@gmail.com"
Phone = "+919048547406"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/muhammedajmal/",
    "GitHub": "https://github.com/pvajmal",
    "Instagram": "https://www.instagram.com/__aj_u/"

}
PROJECTS = {
    "📖 Machine Learning in Python": "https://perfectelearning.com/certificate/907226e396",
    "📖  Learn JMeter ‑ Perfomance testing & API": "https://udemy-certificate.s3.amazonaws.com/pdf/UC-99eb1505-d675-4afc-a536-beb1f1a9c0fe.pdf",
    "📖 Wings Core Tech T3 Machine First And Intelligent Business certification": "https://drive.google.com/file/d/1ieYXFNUQX3H0w6EA8gPfUfea-d959lte/view?usp=sharing",
    "📖 The Art of Articulation": "https://drive.google.com/file/d/1yj5SQAmY9xHjaB4AriD20dZCdDtOZKjI/view?usp=sharing",
    "📖 Commence : Business English Certification": "https://drive.google.com/file/d/1txfuzSYk6WNC8liMaLkEpm7y3zL2hUUr/view?usp=sharing",
    "📖 INS ‑ Certificate in Blockchain Invogue" : "https://drive.google.com/file/d/1Sgg1nTzOInsxOfbcZUz_OWQS5XmBXThJ/view?usp=sharing",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("📞", Phone)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- About Me ---
st.write('\n')
st.subheader("About Me")
st.write(
    """
- ✔️ More than 1.5 years of Experience in Retail Domain as Software Quality Engineer.
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL
- 📊 Data Visulization: Matplotlib, MS Excel
- 📚 Modeling: Logistic regression, linear regression, decition trees
-  🗣 Natural Language Processing - NLTK
- 🐎 Web application performance and API Testing: Apache JMeter, Postman
- 👩‍💻 Working knowledge in Microsoft word, Microsoft Excel, Microsoft PowerPoint, SAP ERP, HP ALM, Azure Board, and Teradata SQL.
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Assistant Systems Engineer | Tata Consultancy Services**")
st.write("03/2021 - Present")
st.write(
    """
- ► QA Engineer at US based retail project. Reviewing quality specifications and technical design documents to provide timely and meaningful feedback. Creating detailed, comprehensive and well‑structured test plans and test cases. Estimating, prioritizing, planning and coordinating quality testing activities.
- ► Handled Performance testing, ETL testing using Python, Manual testing projects and delivered quality products to customers.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Business Development Executive | Extramarks Education**")
st.write("11/2020 ‑ 02/2021")
st.write(
    """
- ► Contact potential customers (parents and students), set up meetings, counsels the student on learning pedagogues.
"""
)
# --- EDUCATION ---
st.write('\n')
st.subheader("Education")
st.write("---")

# --- 1
st.write("🎓", "**Bachelor of Technology in Mechanical Enginering | TKM College of Engineering**")
st.write("08/2016 - 10/2020")
st.write(
    """
- ► CGPA ‑ 8.42/10
- ► Awarded Honours degree from APJ Abdul Kalam University for earning additional credits (Subjects covered: Project Management, Total Quality Management, Green Buildings, Nuclear Engineering)
- ► Internships: \n
    Capitol Engineering & Construction (6 months) - MEP Design and Estimation of G+7 and G+2 projects.\n 
    Cochin Shipyard Ltd, Kerala, India (2017) \n 
    Bosch Rexroth‑CET centre of Excellence in Automation, Kerala, India (2018)
"""
)
# --- Achievements ---
st.write('\n')
st.subheader("Achievements")
st.write("---")

# --- 1

st.write(
    """
- ► Star of the Month Award- For dedication, ownership, innovation, learning and multitasking to accomodate and accomplish multiple Customer deliverables (Tata Consultancy Services)
- ► On the Spot Award- For learning Customer Business, QE process and leading multiple project assignments with Customer appreciations earned on the good work done (Tata Consultancy Services)

"""
)

# --- Certifications and Learnings ---
st.write('\n')
st.subheader("Certifications & Learnings")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
