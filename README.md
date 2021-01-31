# Hobinrood

Try it out: https://vishyananth.github.io/index.html

## Inspiration
According to the results from a simple Google search, the term _hedge fund_ means the following:

__a limited partnership of investors that uses high risk methods, such as investing with borrowed money, in hopes of realizing large capital gains.__

Recent events (particularly on Reddit) have sparked a flurry of activity surrounding the stock markets. Cries of joy and anguish have shaken the glorious World Wide Web as students have become liberated from their debts while others have seen their dreams come to a spectacular end. Looks like that those __high risk methods__ have finally met their match: __r/wallstreetbets__.

Hear us out for a second. We might be students ourselves, but let's give the hedge funds a chance. Why not help them out? In a more altruistic sense, now more than ever, we need to help each other out. Especially these avid risktakers.

## What it does
So what is Hobinrood? If you read the title fast enough, you probably already have caught us in our play on words. However, this time around, we want to give the hedge funds a chance. Consider this an extension of the company's mission of __democratizing finance__.

Hobinrood is a web application that allows users to sign up for an account and create stock portfolios to track daily prices and watch trends across years. This is useful, but we wanted to do more than that, and this is where we turn the tides. In addition to simply tracking stock prices across NYSE and NASDAQ, Hobinrood brings insight to market sentiment to hedge funds so that they can make smarter choices when it comes to committing or backing off from certain stocks. The subreddit __r/wallstreetbets__ has been in quite the frenzy recently, so Hobinrood uses machine learning tools and technologies to scrape information on what the millions of users are planning to do next in the market. 

```
For example, if there is going to be a wave of GME buys, hedge funds that use Hobinrood will be the first to know.
```

Check out the **Sentiment** section of the application, enter the ticker symbol of your favorite stock (maybe AMZN or GOOG because we love cloud tech), and what you will see is an interactive diagram of what Reddit users are feeling about the stock of your choice. Pretty cool, right? You can build up a portfolio within this **Sentiment** section and track as many as you would like! Feel free to switch between stocks by clicking on them in the portfolio to the right.

In the **Portfolio** section of the app, you can similarly enter the ticker symbol of your choice and see its prices and trends in the market without even leaving the app.

Finally, if you really need to write something down because you are incredibly excited and never want to forget your experience with Hobinrood, check out our **Notes** section for all your note-taking needs!

## How we built it
Here is a quick run-down of the technologies that we used, separated into frontend and backend.

**Frontend**: Firebase Firestore & storage & authentication, trading view widgets, HTML, JS, CSS ------
**Backend**: Python, AWS Lambda & DynamoDB & API Gateway, Jupyter Notebooks, NLP packages

The objective of the frontend of the application was to emphasize ease of use and provide structure to our sentiment analysis of users on Reddit, presenting the data in a neat and readable manner. We took the following steps:

1. Use HTML, JS, and CSS for cross-browser functionality
2. Employ Firebase for rapid data access, storage, and authentication
3. Design the UI such that it is organized based on the frequency of usage of various areas
4. Implement Firebase interfaces
5. Perform comprehensive tests of the entire UI

The goal of backend (and the application as a whole) is to analyze user sentiment on Reddit. To accomplish this we took the following steps:

1. Use Reddit's developer tools to conveniently scrape posts, comments, and post metadata
2. Retreive .csv files containing lists of stock ticker symbols and past stock data
3. Use Jupyter notebooks to perform a case study on a set of posts and comments
4. Use the list of stock ticker symbols to find __hit points__ in the comments and posts to indicate sentiment analysis needs to be done
5. Analyze the text using NLP and store the sentiment
6. Transfer to AWS compatible Python scripts and deploy to AWS Lambda & DynamoDB & Gateway to prepare for consuming by the frontend

Here's a little snippet of that code that gives you that lightning speed response time:
```python
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('reddit_parse')

def lambda_handler(event, context):
    
    response = table.get_item(
        Key={
            'stock': event["stock"]
        }        
    )
    return {
        'statusCode': 200,
        'body': response
    }
```

## Challenges we ran into
**CHALLENGE #1**
```
Saving notes in the **Notes** section of the application was a difficult hurdle. This part of the application uses a "rich" text editor, and after researching and browsing the JS file API for a while before we realized that it was possible to base-64 encode the text.
```

**CHALLENGE #2**
```
Figuring out a way to display stock data and sentiment analysis data was a particular challenge in itself since the UI needed to be detailed. However, we were able to get our hands on an API that allowed for the aesthetic we wanted.
```

**CHALLENGE #3**
```
Scraping data from Reddit at first seemed like an impossible challenge to overcome since basic Python packages such as BeautifulSoup and even using tools such as Selenium would still make scraping data an incredibly tedious task to accomplish. Good thing we discovered Reddit's developer tools.
```

## Accomplishments that we're proud of
We are incredibly happy with this final product that we were able to make in the span of less than two days. Even when hacking together from a distance, we were able to communicate effectively and give each other what we needed, when we needed it. In addition, we are especially proud of the ease-of-use of this application and how smooth the UI is for an app that was built in a short amount of time.

## What we learned
There really is a huge amount of work that can be finished in a short amount of time. It takes effective (and responsive) communication, constant work updates, and accountability to keep all parts of the project in check.

Regarding the more technical side of the projects, we learned just how effective Jupyter Notebooks is for prototyping models and visualizing results before deploying the real thing to a server.

## What's next for Hobinrood
Projects are built to last. From the code all the way to the choice of data storage (NoSQL), we have the future in mind, regarding scalability. With an uptick in users and IPOs, our user base is bound to increase, and we have chosen the optimal technologies to quickly scale our application.

We also want Hobinrood to broaden its scope to cover a multitude of Reddit pages and even forums outside of Reddit, to build a more comprehensive NLP model to bring our hedge funds the accurate info that they need.

Thanks for checking out our project!
