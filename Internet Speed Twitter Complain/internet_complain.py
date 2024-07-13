from os import getenv
from internet_speed_twitter_bot import InternetSpeedTwitterBot

EMAIL_TWITTER: str = getenv('twitter_email')
PASSWORD_TWITTER: str = getenv('twitter_password')
PROMISSED_DOWN = '100'
PROMISSED_UP = '50'

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
