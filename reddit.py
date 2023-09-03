import random
import praw
import time

reddit = praw.Reddit(
    client_id="enter your reddit id",
    client_secret="secret key",
    user_agent="<console:redpyapp:1.0>",
    username="user name",
    password="enter your password"
)
sad_quote= ["All our dreams can come true, if we have the courage to pursue them. —Walt Disney","The secret of getting ahead is getting started. —Mark Twain","I’ve missed more than 9,000 shots in my career. I’ve lost almost 300 games. 26 times I’ve been trusted to take the game winning shot and missed. I’ve failed over and over and over again in my life, and that is why I succeed. —Michael Jordan","Don’t limit yourself. Many people limit themselves to what they think they can do. You can go as far as your mind lets you. What you believe, remember, you can achieve. —Mary Kay Ash" ,"The best time to plant a tree was 20 years ago. The second best time is now. ―Chinese Proverb"]

subreddit= reddit.subreddit("television")
for submission in  subreddit.hot(limit=10):
    print("************************")
    # print(submission.title)

    ## our target is to create a bot, it extract the "sad" word from a comment and reply that comment with a inspirational quote

    for comment in submission.comments:
        if hasattr(comment, "body"):
            comment_lower= comment.body.lower()
            if " sad " in comment_lower:
                print("----sad comment-----")
                print(comment.body)
             
                random_replay= random.randint(0, len(sad_quote)-1)
                print("---sad comment replay-------")
                comment.reply(sad_quote[random_replay])
                time.sleep(300)

            if " fuck " in comment_lower:
                print("--non unappropiate comment---")
                print(comment.body)
                comment.replay("please do not use unappropiate word")
                time.sleep(240)
        else:
            print("No such comments are there")

