import json
import boto3
from monkeylearn import MonkeyLearn
from collections import defaultdict
import requests
import pandas as pd

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('reddit_parse')

def lambda_handler(event, context):
    # TODO implement
    
    res = requests.get("https://m4fcmxys7i.execute-api.us-west-2.amazonaws.com/default/reddit_parse")
    json_data = json.loads(res.text)
    
    total_symbols = res['total_symbols']
    posts_now = res['posts_now']
    posts_hot = res['posts_hot']
    posts_top = res['posts_top']
    
    posts = pd.concat([posts_now, posts_hot, posts_top])
    ##############RECEIVE FROM RES
    
    ml = MonkeyLearn('f8727eca4adb7979d592c3d905bfba05ff81863a')
    model_id = 'cl_pi3C7JiL'
    
    stock_sentiment_points = defaultdict(int)

    for i in range(len(posts)):
        curr_title = posts.iloc[i, 0]
        curr_body = posts.iloc[i, 6]
        curr_comments = " ".join(posts.iloc[i, 8])
        for symbol in total_symbols:
            if symbol in curr_title or symbol in curr_body or symbol in curr_comments:
                data = [curr_title + " " + curr_body + " " + curr_comments]
                result = ml.classifiers.classify(model_id, data)
                if result.body[0]["classifications"][0]["tag_name"] == "Positive":
                    stock_sentiment_points[symbol] += 1
                else:
                    stock_sentiment_points[symbol] -= 1
                stock_sentiment_points[symbol] = stock_sentiment_points[symbol] + curr_title.count("buy") + curr_body.count("buy") + curr_comments.count("buy")
                stock_sentiment_points[symbol] = stock_sentiment_points[symbol] - curr_title.count("sell") + curr_body.count("sell") + curr_comments.count("sell")
                
    
    for symbol in total_symbols:
        if symbol not in stock_sentiment_points:
            stock_sentiment_points[symbol] = 0
    
    for key in stock_sentiment_points.keys():
        pos = "Hold"
        if stock_sentiment_points[key] > 0:
            pos = "Buy"
        elif stock_sentiment_points[key] < 0:
            pos = "Sell"
        table.put_item(
            Item = {
                'stock': key,
                'action': pos
            }
        )
    response = {
        'message': 'Item added'
    }
    return {
        'statusCode': 200,
        'body': response
    }



