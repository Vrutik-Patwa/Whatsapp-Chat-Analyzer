import pandas as pd
import re

def remove(text):
  text = text.strip('\n')
  return text

def preprocess(data):
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s.{2}\s-\s'

    messages = re.split(pattern,data)[1:]
    dates =re.findall(pattern,data)

    dates =[x.replace('\u202f',"") for x in dates]

    df = pd.DataFrame({'user_messge':messages , 'message_date': dates})

    df['message_date'] = [x.replace('pm','') for x in df['message_date']]

    df['message_date'] = [x.replace('am','') for x in df['message_date']]

    df['messsage_date']=pd.to_datetime(df['message_date'],format ='%d/%m/%y, %H:%M - ')

    df.rename(columns = {'messsage_date':'date'},inplace=True)

    users=[]
    messages = []
    for message in df['user_messge']:
        entry = list(message.split(':'))

        if entry[1:]:
            users.append(entry[0])
            messages.append(entry[1])
        else:
            users.append('group nortification')
            messages.append(entry[0])

    df['users']=users

    df['messages']=messages

    df.drop(['user_messge'],inplace=True,axis=1)

    df.drop(['message_date'],inplace=True,axis=1)
    df['year']= df['date'].dt.year
    df['year'] = [(str(x).strip(',')) for x in df['year']]
    df['month']=df['date'].dt.month
    df['hour']=df['date'].dt.hour
    df['minute']=df['date'].dt.minute
    df['day']=df['date'].dt.day
    df.drop(columns = ['date'],inplace=True)
    df['messages']=df['messages'].apply(remove)
    return df