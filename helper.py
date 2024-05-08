from urlextract import URLExtract
from wordcloud import WordCloud
extractor = URLExtract()

def fetch_stats(selected_user,df):

    if(selected_user != 'Overall'):
        df = df[df['users'] == selected_user]
    #no of messages
    num_messages = df.shape[0]
    #no of words
    words = []
    for message in df['messages']:
        words.extend(message.split())

    num_media = df[df['messages']==' <Media omitted>'].shape[0]

    y=[]
    for message in df['messages']:
        y.extend(extractor.find_urls(message))

    return num_messages,len(words),num_media,len(y)

def most_busy_users(df):
    users= df['users'].value_counts().head()
    return users

def create_world_cloud(selected_user,df):
    if(selected_user != 'Overall'):
        df = df[df['users'] == selected_user]

        wc = WordCloud(width = 500 ,height=500,min_font_size =10 ,background_color='white')
        df_wc = wc.generate(df['messages'].str.cat(sep=" "))

        return df_wc

def most_words():
    words = []
    for message in df['messages']:
        words.extend(message.split())
    pd.DataFrame(Counter(words).most_common(20))    