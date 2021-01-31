import praw
import pandas as pd

def lambda_handler(event, context):

    reddit = praw.Reddit(client_id='OzDq72tPFF_sBQ', client_secret='cZEK5LrHFW_GBqylCsdOT9H6bM5xDQ', user_agent='Reddit WebScrape')
    
    nyse = pd.read_csv("./resources/nyse.csv")
    nasdaq = pd.read_csv("./resources/nasdaq.csv")
    
    nyse_symbols = [symbol for symbol in nyse['Symbol'] if len(symbol) > 1]
    nasdaq_symbols = [symbol for symbol in nasdaq['Symbol'] if len(symbol) > 1]
    
    total_symbols = nasdaq_symbols + nyse_symbols
    
    posts = []
    for post in reddit.subreddit("wallstreetbets").hot(limit = 100):
        context = [post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created]
        submission = reddit.submission(id = post.id)
        submission.comments.replace_more(limit=0) #Comment forest
        comments = []
        for comment in submission.comments.list():
            comments.append(comment.body)
        context.append(comments)
        posts.append(context)
    posts_hot = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created', 'comments'])
    
    posts = []
    for post in reddit.subreddit("wallstreetbets").top(limit = 100):
        context = [post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created]
        submission = reddit.submission(id = post.id)
        submission.comments.replace_more(limit=0) #Comment forest
        comments = []
        for comment in submission.comments.list():
            comments.append(comment.body)
        context.append(comments)
        posts.append(context)
    
    posts_top = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created', 'comments'])
    
    posts = []
    for post in reddit.subreddit("wallstreetbets").new(limit = 100):
        context = [post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created]
        submission = reddit.submission(id = post.id)
        submission.comments.replace_more(limit=0) #Comment forest
        comments = []
        for comment in submission.comments.list():
            comments.append(comment.body)
        context.append(comments)
        posts.append(context)
    posts_new = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created', 'comments'])

    return {
        'posts_hot': posts_hot,
        'posts_top': posts_top,
        'posts_new': posts_new,
        'total_symbols': total_symbols
    }
