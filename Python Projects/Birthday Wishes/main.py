import pandas as pd
import datetime
import smtplib
# Enter your Authentication details
GMAIL_ID = 'nkismwm@gmail.com'
GMAIL_PSWD = 'Kisanchand8126@!'
def sendEmail(to, sub, msg):
    print(f"Email to {to} sent  with subject: {sub} and message {msg}")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
    s.quit()

    

if __name__ == "__main__":
    # Just for testing
    # sendEmail(GMAIL_ID, "subject", "test message")
    # exit()
    
    df = pd.read_excel("data.xlsx.xlsx")
    # print(df)        #df = dataFrame
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    # print(type(today))   
    writeInd = []
    for index, item in df.iterrows():
        # print(index, item['Birthday'])
        bday = item['Birthday'].strftime("%d-%m")
        # print(bday)
        if(today==bday) and yearNow not in str(item['Year']):
            # sendEmail(item['Email'], "Happy Birthday", item['Dialogue'])
            sendEmail(GMAIL_ID, "Happy Birthday", item['Dialogue'])
            writeInd.append(index) 
        # print(writeInd)
    for i in writeInd:
        yr = df.loc[i, 'Year']
        df.loc[i, 'Year'] = str(yr) + ',' + str(yearNow)
        # print(df.loc[i, 'Year'])
    # print(df)
    df.to_excel('data.xlsx', index = False)


        
            
        
            
            

            


    

