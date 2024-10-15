#should import based on file name
#import user #WAY  1
from user import User #WAY 2
import post

#Calling a function
#wAY1 user_1 = user.User("abc@email.com", "ATG", "103", "DevOps")
user_1 = User("abc@email.com", "ATG", "103", "DevOps")
user_1.get_user()


author = post.Post("NATIONAL anthem", "TAGORE")
author.get_post()