# Twitter-Scraper
Twitter is a social media platform having Trillions of data, when we need to analyse the data we cannot copy and paste all those data so We use SNSCRAPE python package.

This is my project of getting data like Tweets, date, id, url, tweet content, user,reply count, retweet count, language from Twitter using a Keyword or Hashtag that is present in the Twitter systems.

I have used Streamlit to create the webpage, and Snscrape to Extract the data from Twitter. After Scraping data from Twitter, I have used Python MongoDB to store the data in a Database for future use.

In the program that I have attached to this Repository, The workflow that I constructed is,
  I have imported the required libraries like pandas, snscarpe, and streamlit
  Created my front end by using streamlit text inputs and button
  The user is required to provide the Username or Hashtag to scraped, Date range and number of tweets to be scraped.
  Once the Submit button is clicked, the dataframe is displayed which consists of all the scraped data.
  After displaying the data, It is stored in the Database by using MongoDB. 
  Then The user may Download the file in CSV or JSON file.

We can view all the information of the tweets, analyse all the details, and download it to our system if required.
