# 🎉 Birthday Email Automation

A Python-based automation script that sends personalized birthday emails using a predefined template. It checks the current date, compares it to a CSV file containing users' birth dates, and sends them a birthday wish with a customized message. The script uses **SMTP** for sending emails and **Pandas** for handling CSV data.

---

## ✨ Features

- 🎂 Sends automated birthday emails based on the data in a CSV file.
- 🎁 Randomly selects one of three template letters for personalized messages.
- 📅 Compares the current date with users' birthdays and sends an email only on the correct day.
- 📧 Sends the email via Gmail's SMTP server.

---

## 📦 Requirements

- Python 3.x+
- **Pandas**: To read and process the birthday data from a CSV file.
- **smtplib**: To send emails using Gmail's SMTP server.

To install the required libraries, run the following command:

```bash
pip install pandas

🚀 How to Run
Save the script as birthday_email_automation.py.

Ensure you have Python 3.x installed.

Make sure you have a birthday.csv file formatted as follows:
name,month,day,email
John,1,25,john@example.com
Alice,2,14,alice@example.com
name: The recipient's name.

month: The month of their birthday (1-12).

day: The day of their birthday (1-31).

email: The recipient's email address.

Ensure that your Gmail account allows less secure apps to log in (or use an app password for better security).

Run the script by typing the following command in your terminal:
python birthday_email_automation.py
The script will check the current date, match it with the dates in birthday.csv, and send the email to the relevant people.

🎮 How to Use
CSV File: Populate the birthday.csv file with your recipients' details.

Letter Templates: Ensure you have the letter template files (letter_1.txt, letter_2.txt, letter_3.txt) in the same directory as your script. These templates will be randomly selected for the email content.

Email: Ensure that the email address used in the script (clanerumao4@gmail.com) is correct and has access to send emails via SMTP.

🧩 Future Enhancements
🎨 Allow users to add more templates dynamically.

🔒 Add better security features (like OAuth2 for sending emails securely).

🧑‍🤝‍🧑 Integrate with a web app to manage birthdays and templates.

