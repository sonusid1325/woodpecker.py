
---

## 📧 Bulk Internship Application Mailer

This script automates sending internship application emails to multiple recipients using Python, SMTP, and environment variables. Each email is personalized with recipient data from a CSV file and a customizable message template from a text file.

---

### 🚀 Features

- ✅ Uses `.env` for sensitive configuration
    
- ✅ Reads recipient data from `data.csv`
    
- ✅ Sends personalized emails in bulk
    
- ✅ Uses plain SMTP with TLS for security
    

---

### 📂 Project Structure

```
.
├── main.py               # The Python script
├── application.txt       # Email body template (with placeholders)
├── data.csv              # Recipient data (email, name, company)
└── .env                  # Environment variables (email creds etc.)
```

---

### 🧪 Requirements

Install Python dependencies:

```bash
pip install python-dotenv pandas
```

---

### 📄 .env File Setup

Create a `.env` file in the root directory with the following values:

```env
SENDER_EMAIL=your_email@example.com
DISPLAY_NAME=Your Name
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
SMTP_USERNAME=your_smtp_username
SMTP_PASSWORD=your_smtp_password
```

---

### 📄 application.txt Template

Create a `application.txt` file that includes placeholders like this:

```
Dear {name},

I hope this message finds you well.

I’m writing to express my interest in an internship opportunity at {company_name}. I’m passionate about {domain} and would love to contribute to your team. Feel free to reply to this email at {sender_email}.

Looking forward to hearing from you!

Best regards,  
ソヌ
```

---

### 📄 data.csv Format

This file should contain recipient data:

```csv
email,name,company
john@example.com,John Doe,Google
jane@example.com,Jane Smith,Microsoft
```

---

### ▶️ Run the Script

```bash
python main.py
```

Each recipient will get a personalized email with their name and company name inserted into the template. You'll see console messages like:

```
✅ Email sent to john@example.com successfully!
```

---

### 🛑 Note

- Make sure your SMTP credentials are valid.
    
- Some email providers may require app passwords or less-secure app access.
    
- Avoid spamming — always use responsibly!
    

---

### 💡 Credits

<p align="left"> <a href="https://github.com/sonusid1325" target="_blank" > <img src="https://github.com/sonusid1325.png" width="200" style="border-radius: 50%;" alt="ソヌ's GitHub Profile Photo"/> </a> </p>
Made with ❤️ by **ソヌ**  
Automating cold emails, the smart way.



---
