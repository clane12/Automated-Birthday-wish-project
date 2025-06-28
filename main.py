import random
import smtplib
import pandas as pd
import datetime


letter_namelist = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

#----------------------------------------smtp part----------------------------------------------------------------
my_email = "clanerumao4@gmail.com"
password = "sankfargguonavsn"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)




#------------------------------------------pandas part-----------------------------------------------------------

data = pd.read_csv("birthday.csv")

data = data.to_dict(orient="records") # orient = records is used to put the dictionary into a list, makes it easier to access.


reci_month = data[0]["month"]
reci_day = data[0]["day"]
recipient_email = data[0]["email"]
print(recipient_email, reci_month, reci_day)
print(data[1]["month"], data[1]["day"])

#-------------------------------------------------datetime and letter.txt with open--------------------------------------------------------

date = datetime.datetime.now()
current_day = date.day
current_month = date.month

print(current_month, current_day)

letter = open(f"{random.choice(letter_namelist)}", "r", encoding="utf-8")
contents = letter.read()

for i in range(len(data)):
    if current_month == data[i]["month"] and current_day == data[i]["day"]:
        contents = contents.replace("[NAME]", data[i]["name"]) # this is short and can have multiple people but, if 2 people have birthday on same day. its not gonna work as [NAME] will not be for 2nd time.
        connection.sendmail(from_addr=my_email, to_addrs=data[i]["email"], msg=f"subject: birthday wish \n\n {contents}")


# if current_month == reci_month and current_day == reci_day:
#     contents = contents.replace("[NAME]", "Mom")
#     connection.sendmail(from_addr=my_email, to_addrs=recipient_email, msg=f"subject: birthday wish \n\n {contents}")
#
# elif current_month == data[1]["month"] and current_day == data[1]["day"]:
#     contents = contents.replace("[NAME]", "Dad")
#     connection.sendmail(from_addr=my_email, to_addrs=data[1]["email"], msg=f"subject: Birthday wish \n\n {contents}")


connection.close()
letter.close()

