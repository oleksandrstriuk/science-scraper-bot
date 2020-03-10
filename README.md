# Description

This script is a realization of the idea of scraping scientific news from the “Science” Subreddit and broadcasting them via a telegram bot into a telegram channel. Initially, I've constructed two simple code fragments in Python for each of these tasks, but then I decided to combine them in one solid block of code so that the bot can automatically send the info that has been scrapped to the channel each time the program is executed. 

Basically this is the simplest algorithm that allows extracting results from one block of code (Reddit Scraper) into another (Posting Telegram Bot).

# Modules to Install

* telegram
* telebot
* praw

# Manuals

* https://core.telegram.org/bots — instructions for creating and deploying bots.
* https://praw.readthedocs.io/en/stable/index.html — PRAW documentation (The Python Reddit API Wrapper).
* https://www.reddit.com/prefs/apps — how to create Reddit Application (+ API usage guidelines).
