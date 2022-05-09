from pickle import TRUE
import requests,json
import datetime
import pytz
import tweepy
import settings

# Git の設定
git_username = settings.GIT_USERNAME
git_client_id = settings.GIT_CLIENT_ID
git_client_secrets = settings.GIT_CLIENT_SECRETS


# Twitter APIのキーを設定
consumer_key = settings.TWITTER_CONSUMER_API_KEY
consumer_secret = settings.TWITTER_CONSUMER_API_SECRET_KEY

# Twitter APIのアクセストークンを設定
access_token=settings.TWITTER_ACCESS_TOKEN
access_token_secret =settings.TWITTER_ACCESS_TOKEN_SECRET


# Gitの情報を取得

w_list = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

# Twitterへの投稿
## TwitterClientの作成
client = tweepy.Client(
  consumer_key=consumer_key, 
  consumer_secret=consumer_secret, 
  access_token=access_token, 
  access_token_secret=access_token_secret
)
## 投稿文
raw_text = '''【Github Commit Bot】
Github Name: {0}
Github URL: https://github.com/{1}
Period : {2}({4}) - {3} ({5})
Total Commit : {6}commit
#GitHub #GitHubCommitBot'''
text = raw_text.format(git_username, git_username, start_date.strftime('%m/%d'), finish_date.strftime('%m/%d'), w_list[start_date.weekday()], w_list[finish_date.weekday()] ,total_commit_count)

# 投稿
if type(total_commit_count) == int:
  client.create_tweet(text=text)
elif type(total_commit_count) == str:
  client.create_tweet(text=total_commit_count)
else:
  pass