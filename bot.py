import telegram
import telebot
import praw

# set your Telegram data
bot_token = '<insert your token here>'
bot_chatID = '@your_channel_name'
bot = telebot.TeleBot('<insert your token here>')

# set your Reddit data, use the link --> https://www.reddit.com/prefs/apps
reddit = praw.Reddit(client_id='<PERSONAL_USE_SCRIPT_14_CHARS>', \
                     client_secret='<SECRET_KEY_27_CHARS>', \
                     user_agent='<YOUR_APP_NAME>', \
                     username='<YOUR_REDDIT_USERNAME>', \
                     password='<YOUR_REDDIT_LOGIN_PASSWORD>')
# ^ don't forget to remove the greater-than and less-than signs <>

def reddit_scraper(submission):
    news_data = []
    subreddit = reddit.subreddit('<name_of_subreddit>')
    new_subreddit = subreddit.new(limit=500)
    for submission in subreddit.new(limit=5):
        data = {}
        data['title'] = submission.title
        data['link'] = submission.url
        news_data.append(data)
    return news_data

def get_msg(news_data):
    msg = '\n\n\n'
    for news_item in news_data:
        title = news_item['title']
        link = news_item['link']
        msg += title+'\n[<a href="'+link+'">Read the full article --></a>]'
        msg += '\n\n'
        
    return msg

subreddit = reddit.subreddit('<name_of_subreddit>')
new_subreddit = subreddit.new
for submission in subreddit.new(limit=1):
    news_data = reddit_scraper(submission)
    if len(news_data) > 0:
        msg = get_msg(news_data)
        status = bot.send_message(chat_id='@your_channel_name', text=msg, parse_mode=telegram.ParseMode.HTML)        
        if status:            
            print(status)
else:
    print('No updates.')
