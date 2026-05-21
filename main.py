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
    chapter, verse = shloka_number.strip().split(".")
    prompt = f"""
You are a Bhagavad Gita scholar. Provide Chapter {chapter}, Verse {verse} of the Bhagavad Gita.

CRITICAL: Use ONLY the standard 700-verse edition of the Bhagavad Gita as found in the Bhishma Parva of the Mahabharata. Follow the verse numbering used by Swami Prabhupada's "Bhagavad Gita As It Is" or Swami Chinmayananda's edition. These are the most widely accepted numbering systems.


STRICT RULES:
- Give ONLY Chapter {chapter}, Verse {verse}. Do NOT include adjacent verses.
- Sanskrit must be accurate and complete.
- Do not add any introduction, conclusion, or extra commentary.

FORMAT (follow exactly):

🕉️ Chapter {chapter}, Verse {verse}

📖 Sanskrit:
[Sanskrit shloka here]

📝 Word-by-Word Meaning:
[Break down key Sanskrit words and their meanings]

💡 Simple Meaning:
[1-2 sentence plain English meaning]

📖 Detailed Meaning:
[Explain the words in brief and the context. And explain a bit in the story format a bit ]

🌱 Practical Takeaway:
[1 actionable life lesson from this verse]

        """
    client = genai.Client(api_key=google_api)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
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

