
import streamlit as st
import requests
from streamlit_lottie import st_lottie
# import time
from bs4 import BeautifulSoup

import openai
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from docx import Document
import gradio as gr
import re
import json
st.set_page_config(page_title="Job Finder",page_icon=":tada:",layout="wide")
st.markdown("""
<style>
.css-nqowgj.edgvbvh3
{
    visibility:hidden;
}
.css-164nlkn.egzxvld1
{
    visibility:hidden;
}
</style>
""",unsafe_allow_html=True)
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_xbf1be8x.json")


with st.container():
    # st.title("Job Finder")
    st.markdown("<h1 style='text-align: center;'>Job Finder</h1>", unsafe_allow_html=True)
    st.subheader("Welcome to Job Finder")


with st.container():
    st.write("---")
    left_column,right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        # st.snow()
        # picture = st.camera_input("take a picture")
        # if picture:
        #     st.image(picture)
        # st.balloons()
        # st.select_slider(
        #     'Select a color of the rainbow',
        #     options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
        # st.snow()
        # with st.spinner('Wait for it...'):
        #      time.sleep(5)
        #      st.success('Done!')
        # st.text_input('Movie title', 'Life of Brian')
        # st.camera_input("take a picture")
        st.text(
            """
            On this Job Finder:\n
            \t People can easily find their suitable jobs in one location\n
            \tEnter the job description and get the suitable job positions
            
            """
        )

    with right_column:
        st_lottie(lottie_coding,height=300,key="coding")


with st.container():
    st.write("---")
    st.header("Job Search")
    st.write("##")
    description = st.text_area("Enter the description:")
    job =[]
    if st.button("Search"):
        # st.write("congratulations"+description)

        openai.api_key = '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'

            
        response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Get the job role, education , place , technologies , number of years of experience , job type from Description:\n{description}\n",
        
        temperature=0.5,
        max_tokens=100,
        n=1,
        stop=None,
        timeout=10,
        
        )

        main_summary = response.choices[0].text.strip()

        # print(main_summary)

        if main_summary != " ":       
            # Extract specific information using regular expressions
            job_role = re.search(r'Job Role:(.*)', main_summary).group(1).strip()
            education = re.search(r'Education:(.*)', main_summary).group(1).strip()
            place = re.search(r'Place:(.*)', main_summary).group(1).strip()
            technologies = re.search(r'Technologies:(.*)', main_summary).group(1).strip()
            experience = re.search(r'Experience:(.*)', main_summary).group(1).strip()
            job_type = re.search(r'Job Type:(.*)', main_summary).group(1).strip()

            # Create a dictionary for the summary
            summary_dict = {
                'Job_Role': job_role,
                'Education': education,
                'Place': place,
                'Technologies': technologies,
                'Experience': experience,
                'Job_Type': job_type,
            }

            # Print the summary dictionary
            print(summary_dict)
            print("SAZIYA")

            value1 = summary_dict.get("Job_Role")
            formatted_job_title = value1.replace(" ", "-")
            print(formatted_job_title)
            
            # print(value1)
            # b=value1.split()
            # print(b)
            # stop_words =stopwords.words("english")
            # stop_words.extend(["in"])
            value2 = summary_dict.get("Education")
            value3 = summary_dict.get("Place")
            value4 = summary_dict.get("Technologies")
            value5_str = summary_dict.get("Experience")
            lowercase_value5_str = value5_str.lower()
            years_index = value5_str.find("Years")

            print(value1)
            print(value4)
            print(value5_str)
            if years_index != -1:
                experience_num_str = value5_str[:years_index].strip()
                try:
                    value5 = int(experience_num_str)
                except ValueError:
                    value5 = 0
            else:
                if value5_str.lower() in ["n/a", "not specified", "none", " "]:
                    value5 = 0
                else:
                    value5 = 0  # Assign a default value when experience is text or empty

            if value5 != 0:
                if value5 < 4:
                    x = value5 * 12
                    print(x)
                else:
                    y = 500
                    print(y)
            else:
                print("Experience should not be zero")

            # value5_str = summary_dict.get("Experience")
            # lowercase_value5_str = value5_str.lower()
            # years_index = value5_str.find("Years")

            # print(value1)
            # print(value4)
            # print(value5_str)
            # if years_index != -1:
            #     experience_num_str = value5_str[:years_index].strip()
            #     value5 = float(experience_num_str)
            # else:
            #     value5 = int(value5_str)
            #     Z = int(value5)
            #     print(Z)

            # if Z != 0:
            #         if Z < 4:
            #             x = Z * 12
            #             print(x)
                        
            #         else:
            #             y = 500
            #             print(y)
                        
            # else:
            #         print("experience should not be zero")

            print("LALITHA")

            value6 = summary_dict.get("Job_Type")
            if value6.lower() == "full time":
                print("1")
            elif value6.lower() == "part time":
                print("2")
            elif value6.lower() == "internship":
                print("3")
            elif value6.lower() == "apprenticeship":
                print("6")
            else:
                print("Your job type is not in the list.")
            #jjob=[]
            if formatted_job_title.lower() != "N/A" and formatted_job_title.lower()!= "Not Specified" and formatted_job_title.lower() != "None" and formatted_job_title.lower() != " ":
                job.append(formatted_job_title.lower())
            else:
                pass

            if value2 != "N/A" and value2 != "Not Specified" and value2 != "None" and value2 != " ":
                job.append(value2)
                print(job)
            else:
                pass
            if value3 != "N/A" and value3 != "Not Specified" and value3 != "None" and value3 != " ":
                job.append(value3)
            else:
                pass

            if value4.lower() != "N/A" and value4.lower() != "Not Specified" and value4.lower() != "None" and value4.lower() != " ":
                job.append(value4)
            else:
                pass
            if value5 != 0:
                if value5 < 4:
                    x =value5 * 12
                    print(x)
                    job.append(x)
                else:
                    x = 500
                    print(x)
                    job.append(x)
            
            
            

            if value6.lower() != "N/A" and value6.lower != "Not Specified" and value6.lower() != "None" and value6.lower() != " ":
                job.append(value6)
            else:
                pass

            print(job)
            joined_string =  '-'.join(str(element) for element in job) 
            print(joined_string)
           # URL="https://www.freshersworld.com/jobs/jobsearch/"+
            # URL =f"https://www.freshersworld.com/jobs/jobsearch/"+{formatted_job_title}+"-for-"+{value3}+"?course=16&experience="+{x}
            url2 ="https://www.freshersworld.com/jobs/jobsearch/" + formatted_job_title.lower() 
            URL = "https://www.freshersworld.com/jobs/jobsearch/" + formatted_job_title.lower() +  "?course=16&experience=" + str(value5)
            url1= "https://www.freshersworld.com/jobs/jobsearch/" + formatted_job_title.lower() +"-for-"+value2+ "?course=16&experience=" + str(value5)
            
            print(url2)
            print(URL)
            print(url1)

             
