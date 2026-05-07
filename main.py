from email.mime.text import MIMEText
from google import genai
import os
import smtplib
from dotenv import load_dotenv
import json

load_dotenv()
google_api = os.getenv("GOOGLE_API")
EMAIL_USER=os.getenv("EMAIL")
EMAIL_PASS=os.getenv("PASSWORD")




#Loadig all the json
def load_shlokas():
    with open("shloka_number.txt", "r") as f:
        return f.read().split(",")

def load_content():
    try:
        with open("contents.json", "r") as f:
            return json.load(f)
    except:
        return{}


with open("user.json","r") as f:
    user_data = json.load(f)


# Generating Shloka if not there in the contents.json
def generate_shloka(shloka_number):
    prompt = f"""
        Give structured output for Bhagavad Gita shloka {shloka_number} in this format:

        1. Shloka (sanskrit)
        2. Meaning (simple)
        3. Learning (practical takeaway)
        4. 

        Keep it clean and labeled. since i want to sent it directly in email to someone!
        so dont even right here is your result, rather just give me the above mentioned things
        """
    client = genai.Client(api_key=google_api)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    print(response.text)
    return response.text

# Getting the Shlok Numbers by verses

shlok_number = load_shlokas()

def send_email(to_email, subject, body):
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = f"Bhagwad Gita Shlok Number: {subject}"
    msg["From"] = EMAIL_USER
    msg["To"] = to_email


    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, to_email, msg.as_string())


#  The logic to select, save and send shlok

def save_contents(data):
    with open("contents.json", "w") as f:
        json.dump(data, f, indent=2)

contents_data = load_content()

for ROLL_NO, user in user_data["users"].items():
    index = user["current_index"]
    shlok_no = shlok_number[index]
    email = os.getenv(ROLL_NO)
    if  shlok_no not in contents_data:
        result = generate_shloka(shlok_no)
        contents_data[shlok_no]=result
        send_email(email, shlok_no, result)
    else:
        content = contents_data.get(shlok_no)
        send_email(email, shlok_no, content)



    user_data["users"][ROLL_NO]["current_index"] += 1




save_contents(contents_data)

with open("user.json", "w") as f:
    json.dump(user_data, f, indent=2)

