🕉️ Gita Gyan — Daily Bhagavad Gita Learning
Receive a verse of wisdom every morning, straight to your inbox.

"Let your daily practice begin not with struggle, but with a shloka."


📖 What Is This?
Gita Gyan is an automated daily email system that delivers a verse (shloka) from the Bhagavad Gita to a group of learners every morning. Each email includes:

🔤 The Sanskrit shloka (from the standard 700-verse edition)
📝 A word-by-word breakdown of key Sanskrit terms
💡 A simple English meaning (1–2 sentences)
📖 A detailed explanation with story context
🌱 A practical life takeaway you can apply that day

Each person progresses through all 700 shlokas (18 chapters) at their own pace — one verse per day, chapter by chapter, from 1.1 all the way to 18.78.

✨ Features
FeatureDescription⏰ Scheduled Daily DeliveryRuns every morning at 7:00 AM via GitHub Actions cron🤖 AI-Generated ExplanationsUses Gemini 2.5 Flash to generate rich, scholar-quality commentary💾 Smart CachingGenerated content is saved in contents.json — a shloka is only generated once, ever👥 Multi-User SupportEach user has an independent progress tracker (current_index)🔁 Auto-Retry LogicIf the Gemini API fails, it retries up to 3 times with increasing wait times🔒 Secure SecretsAll emails and API keys are stored as GitHub Secrets — never hardcoded📬 Gmail SMTPSends beautifully formatted plain-text emails via Gmail

🏗️ Project Structure
Gita_learning/
│
├── 📄 main.py                  # Core logic: generate, cache & send shlokas
├── 📋 shloka_number.txt        # All 700 shloka IDs (e.g., 1.1, 2.47, 18.78)
├── 👥 user.json                # User profiles & their current progress index
├── 💾 contents.json            # Cache of all previously generated shloka content
├── 📦 requirements.txt         # Python dependencies
│
└── .github/
    └── workflows/
        └── 📅 daily_gita.yml   # GitHub Actions workflow (runs daily at 7 AM)

        

Subject: Bhagwad Gita Shlok Number: 2.47

🕉️ Chapter 2, Verse 47

📖 Sanskrit:
कर्मण्येवाधिकारस्ते मा फलेषु कदाचन।
मा कर्मफलहेतुर्भूर्मा ते सङ्गोऽस्त्वकर्मणि॥

📝 Word-by-Word Meaning:
karmaṇi – in action | eva – only | adhikāraḥ – right/authority
te – your | mā – never | phaleṣu – in the fruits...

💡 Simple Meaning:
You have the right to perform your duties, but never to the fruits
of your actions. Do not be motivated by the results, nor be
attached to inaction.

📖 Detailed Meaning:
[Contextual story and deeper explanation...]

🌱 Practical Takeaway:
Focus fully on the quality of your work today. Release attachment
to how it will be received or rewarded.



🛠️ Tech Stack

Python 3.11 — Core scripting language
Google Gemini 2.5 Flash — AI model for shloka explanations (google-genai)
smtplib + MIME — Email delivery via Gmail SMTP
GitHub Actions — Scheduled automation (cron job)
JSON — Lightweight data storage for users and content cache
