import streamlit as st
from preprocessor import preprocess
import helper
import pandas as pd
import matplotlib.pyplot as plt
st.sidebar.title("Whatsapp chat analyzer")

uploaded_file = st.sidebar.file_uploader('Choose a file')

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode('utf-8')
    df = preprocess(data)
    user_list =df['users'].unique().tolist()
    user_list.remove('group nortification')
    user_list.sort()
    user_list.insert(0,'Overall')
    st.dataframe(df,use_container_width=True)
    selected_user =  st.sidebar.selectbox("Show analysis wrt",user_list)

    if st.sidebar.button('Show Analysis'):
        col1,col2,col3,col4 =st.columns(4)
        num_messages,num_words,num_media,num_urls = helper.fetch_stats(selected_user,df)


        with col1:
            st.header('Total Messages')
            st.title(num_messages)

        with col2:
            st.header('Total words')
            st.title(num_words)
        
        with col3:
            st.header('Media Shared')
            st.title(num_media)

        with col4:
            st.header('Urls Shared')
            st.title(num_urls)

        #finding the busiest users of the group

        if selected_user == 'Overall':
            st.header('Most Busy Users')

            col1,col2 = st.columns(2)
            users = helper.most_busy_users(df)
            fig,ax = plt.subplots()
            with col1:
                ax.bar(users.index,users.values,color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)


                # st.write(x)
            with col2:
                users =pd.DataFrame(round(((df['users'].value_counts()/df.shape[0])*100),2).reset_index().rename(columns={'index':'name','users':'percent'}))
                st.dataframe(users,use_container_width=True,height=320)


        #World Clous
        st.title("World Cloud")
        df_wc = helper.create_world_cloud(selected_user,df)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)