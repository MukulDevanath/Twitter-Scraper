import datetime
import pandas as pd
import snscrape.modules.twitter as sntwitter
import streamlit as st

st.title("Twitter Scraper")
name = st.text_input("Enter Keyword or Hashtag")
result = []

col1, col2 = st.columns(2)
with col1:
    from_date = st.date_input("From Date", value=datetime.date(2023, 1, 1))
with col2:
    to_date = st.date_input("To Date")

tweet_range = st.text_input("Number of tweets to be Scraped", value=1000)

if st.button('Submit'):
    st.success(name)
    result.append(name)
    result.append(from_date)
    result.append(to_date)
    result.append(tweet_range)

def scrape_data(result):
    try:
        tweets_list1 = []
        search = result[0] + " since:" + str(result[1]) + " until:" + str(result[2])
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(search).get_items()):
            if i > int(result[3]):
                break
            tweets_list1.append(
                [tweet.date, tweet.id, tweet.url, tweet.content, tweet.user.username, tweet.replyCount,
                 tweet.retweetCount, tweet.lang, tweet.source, tweet.likeCount])

        tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet_Id', 'URL', 'Content', 'Username', 'Reply_Count',
                                                         'Retweet_Count', 'Language', 'Source', 'Like_Count'])
        return tweets_df1
    except (ValueError, IndexError):
        pass

dataframe = scrape_data(result)
st.dataframe(dataframe)

try:
    csv_file = dataframe.to_csv().encode('utf-8')
    json_file = dataframe.to_json()

    st.download_button(label="Download as CSV", data=csv_file, mime='text/csv')
    st.download_button('Download as JSON', data=json_file)

except AttributeError:
    pass