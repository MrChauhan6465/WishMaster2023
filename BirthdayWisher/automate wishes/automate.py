import pandas as pd
import datetime
import smtplib
import os

os.chdir(r"F:\Python-projects\BirthdayWisher\BirthdayWisher\automate wishes")
os.mkdir("testing") 

# Enter your authentication details
GMAIL_ID = 'vijaykumarchauhan6465@gmail.com'
GMAIL_PSWD = 'trgswzdzojghwcac'


def sendEmail(to, subject, message):
    print(f"Email to {to} sent with subject: {subject} and message {message}" )
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to, f"Subject: {subject}\n\n{message}")
    s.quit()
    

if __name__ == "__main__":
    df = pd.read_csv("data.csv")
 
    today = datetime.datetime.now().strftime("%m-%d-%Y")
    
    writeInd = []
    for index, item in df.iterrows():
       
        bday = item['Birthday']
        if (today == bday) and  item[3] is not None:
            sendEmail(item[1], "Happy Birthday!", "Happy Birthday!") 
            writeInd.append(index)
            df.loc[index, 'Message'] = "Sent"
            df.loc[index, 'Year'] = str(datetime.datetime.now().strftime("%Y")) 

    df.to_csv('data.csv', index=False)
