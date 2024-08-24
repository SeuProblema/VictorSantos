from highrise import *
from highrise.models import *
from highrise.webapi import *
from highrise.models_webapi import *

async def userinfo (self: BaseBot, user: User, message: str) -> None:
    #Split the message into parts
    parts = message.split(" ")
    if len(parts) != 2:
        await self.highrise.chat("Incorrect format, please use /userinfo <@username>")
        return
    #Removes the @ from the username if it exists
    if parts[1].startswith("@"):
        username = parts[1][1:]
    else:
        username = parts[1]
    #Get the user id from the username
    user = await self.webapi.get_users(username = username, limit=1)
    if user:
        user_id = user.users[0].user_id
    else:
        await self.highrise.chat("User not found, please specify a valid user")
        return
    
    #Get the user info
    userinfo = await self.webapi.get_user(user_id)
    number_of_followers = userinfo.user.num_followers
    number_of_friends = userinfo.user.num_friends
    number_of_folowing = userinfo.user.num_following
    joined_at = (userinfo.user.joined_at).strftime("%d/%m/%Y %H:%M:%S")
    try:
        last_login = (userinfo.user.last_online_in).strftime("%d/%m/%Y %H:%M:%S")
    except:
        last_login = "Last login not available"
    #Get the number of posts and the most liked post
    userposts = await self.webapi.get_posts(author_id = user_id)
    number_of_posts = 0
    most_likes_post = 0
    try:
        while userposts.last_id != "":
            for post in userposts.posts:
                if post.num_likes > most_likes_post:
                    most_likes_post = post.num_likes
                number_of_posts += 1
            userposts = await self.webapi.get_posts(author_id = user_id, starts_after=userposts.last_id)
    except Exception as e:
        print (e)
    
    #Send the info to the chat
    await self.highrise.chat(f"""Usuario: {username}\nNúmero de seguidores : {number_of_followers}\nNúmero de amigos : {number_of_friends}\nNúmero de seguindo: {number_of_folowing}\nEntrou no HR em : {joined_at}\nÚltimo Login: {last_login}\nNúmero de posts : {number_of_posts}\nMais curtidas em uma postagem : {most_likes_post}""")