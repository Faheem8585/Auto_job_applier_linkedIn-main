###################################################### APPLICATION INPUTS ######################################################


# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Give an relative path of your default resume to be uploaded. If file in not found, will continue using your previously uploaded resume in LinkedIn.
default_resume_path = "all resumes/default/resume.pdf"      # (In Development)

# What do you want to answer for questions that ask about years of experience you have, this is different from current_experience? 
years_of_experience = "3"          # A number in quotes Eg: "0","1","2","3","4", etc.

# Do you need visa sponsorship now or in future?
require_visa = "No"               # "Yes" or "No"

# What is the link to your portfolio website, leave it empty as "", if you want to leave this question unanswered
website = "https://portfolio-five-rouge-60.vercel.app/"                        # "www.example.bio" or "" and so on....

# Please provide the link to your LinkedIn profile.
linkedIn = "https://www.linkedin.com/in/muhammadfaheemarshad99/"       # "https://www.linkedin.com/in/example" or "" and so on...

# What is the status of your citizenship? # If left empty as "", tool will not answer the question. However, note that some companies make it compulsory to be answered
# Valid options are: "U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", "Canadian Citizen/Permanent Resident" or "Other"
us_citizenship = "Non-citizen allowed to work for any employer"



## SOME ANNOYING QUESTIONS BY COMPANIES 🫠 ##

# What to enter in your desired salary question (American and European), What is your expected CTC (South Asian and others)?, only enter in numbers as some companies only allow numbers,
desired_salary = 46000          # 80000, 90000, 100000 or 120000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your expected CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
And if asked in months, then it will divide by 12 and answer. Examples:
* 2400000 will be answered as "200000"
* 850000 will be answered as "70833"
'''

# What is your current CTC? Some companies make it compulsory to be answered in numbers...
current_ctc = 00000        # 800000, 900000, 1000000 or 1200000 and so on... Do NOT use quotes
'''
Note: If question has the word "lakhs" in it (Example: What is your current CTC in lakhs), 
then it will add '.' before last 5 digits and answer. Examples: 
* 2400000 will be answered as "24.00"
* 850000 will be answered as "8.50"
# And if asked in months, then it will divide by 12 and answer. Examples:
# * 2400000 will be answered as "200000"
# * 850000 will be answered as "70833"
'''

# (In Development) # Currency of salaries you mentioned. Companies that allow string inputs will add this tag to the end of numbers. Eg: 
currency = "EUR"                 # "USD", "INR", "EUR", etc.

# What is your notice period in days?
notice_period = 30                   # Any number >= 0 without quotes. Eg: 0, 7, 15, 30, 45, etc.
'''
Note: If question has 'month' or 'week' in it (Example: What is your notice period in months), 
then it will divide by 30 or 7 and answer respectively. Examples:
* For notice_period = 66:
  - "66" OR "2" if asked in months OR "9" if asked in weeks
* For notice_period = 15:"
  - "15" OR "0" if asked in months OR "2" if asked in weeks
* For notice_period = 0:
  - "0" OR "0" if asked in months OR "0" if asked in weeks
'''

# Your LinkedIn headline in quotes Eg: "Software Engineer @ Google, Masters in Computer Science", "Recent Grad Student @ MIT, Computer Science"
linkedin_headline = "MSc Artificial Intelligence, Data Analyst, Data Scientist, Python, SQL, Machine Learning, Computer Vision | Open to Work in Germany with a Master's in Artificial Intelligence and 2+ years of experience" # "Headline" or "" to leave this question unanswered

# Your summary in quotes, use \n to add line breaks if using single quotes "Summary".You can skip \n if using triple quotes """Summary"""
linkedin_summary = """
MSc Artificial Intelligence graduate (BTU Cottbus-Senftenberg, Nov 2025) with hands-on experience in data\n analysis, machine learning, and computer vision, built across research and applied engineering environments in Germany.\n
 
At Fraunhofer IFAM Dresden, I worked as a Research Assistant in the Hydrogen Technology department,\n developing automated Python pipelines for data analysis and outlier detection (curve fitting, k-Means, DBSCAN),\n building interactive dashboards with Streamlit and Plotly, and applying both classical and ML-based image\n analysis to industrial MicroCT datasets. My MSc thesis at Fraunhofer focused on automated electrode surface\n analysis using a dual-pipeline approach: classical image processing (OpenCV, CLAHE, adaptive thresholding,\n morphological filtering) and a deep learning U-Net model for multi-class segmentation and coating delamination\n detection. My work was recognised in a formal Fraunhofer reference letter for delivering complex analytical\n outputs to the highest standard and making data accessible to cross-functional teams.\n
 
At BTU Cottbus-Senftenberg, I have been working as a lab instructor since October 2023, delivering practical\n sessions on neural signal analysis, guiding students through Python and MATLAB data processing workflows, and\n managing the full data lifecycle from collection and preprocessing through to analysis and insight.\n
 
My independent project portfolio spans end-to-end BI dashboards (108K records, SQL, Power BI, Plotly), fraud\n detection systems (97.66% AUC, FastAPI, PostgreSQL), real-time object detection (YOLOv8), semantic segmentation\n (U-Net, 47.9% mIoU), and a RAG-based AI assistant pipeline (ChromaDB, HuggingFace, Gemini API).\n
I am currently based in Cottbus, Germany, and open to Data Analyst, Data Scientist, Computer Vision Expert and AI/ML Engineering roles.\n
Core stack: Python · SQL · Pandas · Scikit-learn · PyTorch · TensorFlow · OpenCV · Streamlit · Power BI · Docker · FastAPI
"""

'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Your cover letter in quotes, use \n to add line breaks if using single quotes "Cover Letter".You can skip \n if using triple quotes """Cover Letter""" (This question makes sense though)
cover_letter = """
Dear Hiring Team,\n\n 
98.55% classification accuracy on 54,305 agricultural images across 38 classes. 97.66% AUC on a production fraud detection service. 47.9% mIoU on aerial drone segmentation. 87% pytest coverage on a live automation platform. These are not side projects; they are deployed systems I built, tested, and maintained end to end.\n\n
I am a Machine Learning Engineer and Data Scientist with an MSc in Artificial Intelligence from BTU Cottbus-Senftenberg and 4+ years of applied experience spanning computer vision, LLM and RAG integration, data pipeline engineering, and production ML deployment. My work at Fraunhofer IFAM involved designing and benchmarking two competing CV pipelines for industrial CT imaging data under rigorous ablation study conditions; the kind of methodical, research-grade engineering that carries directly into production systems. Before that, I delivered ML systems for healthcare and financial clients at JAYZENAI LTD in Pakistan. Since October 2023 I have been a Lab Instructor at BTU, designing and delivering AI and data science sessions for graduate students.\n\n
My technical foundation covers the full ML stack: PyTorch, TensorFlow/Keras, OpenCV, scikit-learn, YOLOv8, U-Net, MobileNetV2, Grad-CAM, HuggingFace Transformers, Gemini and OpenAI APIs, ChromaDB, Python, SQL, FastAPI, Docker, Git, and AWS. I am equally comfortable building a segmentation model, integrating an LLM into a production workflow, designing a SQL data architecture, or shipping a monitored inference API. I write clean, tested, documented code, not notebooks that break in production.\n\n
I am based in Cottbus, Germany, hold a valid German work permit, and am open to relocation anywhere in Germany and Europe. I am flexible on start date. I would be glad to discuss how my background fits your team's needs.\n\n
Yours sincerely,\n\n
Muhammad Faheem Arshad
+49 15563125543
portfolio-five-rouge-60.vercel.app
"""

# Your user_information_all letter in quotes, use \n to add line breaks if using single quotes "user_information_all".You can skip \n if using triple quotes """user_information_all""" (This question makes sense though)
# We use this to pass to AI to generate answer from information , Assuing Information contians eg: resume  all the information like name, experience, skills, Country, any illness etc. 
user_information_all ="""
User Information
"""
##<
'''
Note: If left empty as "", the tool will not answer the question. However, note that some companies make it compulsory to be answered. Use \n to add line breaks.
''' 

# Name of your most recent employer
recent_employer = "Fraunhofer IFAM Dresden, BTU Cottbus-Senftenberg" # "", "Lala Company", "Google", "Snowflake", "Databricks"

# Example question: "On a scale of 1-10 how much experience do you have building web or mobile applications? 1 being very little or only in school, 10 being that you have built and launched applications to real users"
confidence_level = "8"             # Any number between "1" to "10" including 1 and 10, put it in quotes ""
##



# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

## Allow Manual Inputs
# Should the tool pause before every submit application during easy apply to let you check the information?
pause_before_submit = True         # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''

# Should the tool pause if it needs help in answering questions during easy apply?
# Note: If set as False will answer randomly...
pause_at_failed_question = True    # True or False, Note: True or False are case-sensitive
'''
Note: Will be treated as False if `run_in_background = True`
'''
##

# Do you want to overwrite previous answers?
overwrite_previous_answers = False # True or False, Note: True or False are case-sensitive







############################################################################################################
'''
THANK YOU for using my tool 😊! Wishing you the best in your job hunt 🙌🏻!

Sharing is caring! If you found this tool helpful, please share it with your peers 🥺. Your support keeps this project alive.


As an independent developer, I pour my heart and soul into creating tools like this, driven by the genuine desire to make a positive impact.

Your support, whether through donations big or small or simply spreading the word, means the world to me and helps keep this project alive and thriving.

Gratefully yours 🙏🏻,
'''
############################################################################################################