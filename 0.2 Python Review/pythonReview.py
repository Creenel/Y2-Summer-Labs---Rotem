def create_youtube_video(title,description):
		youtube_video = {"Title":title,"Description":description,"Likes":0,"Dislikes":0,"Comments":{}}
		return youtube_video
def like(youtube_video):
	if "Likes" in youtube_video:
		youtube_video["Likes"] += 1
	return youtube_video
def dislike(youtube_video):
	if "Dislikes" in youtube_video:
		youtube_video["Dislikes"] += 1
	return youtube_video
def add_comment(youtubevideo,username,comment_text):
	youtubevideo["Comments"][username] = comment_text
	return youtubevideo
x1 = create_youtube_video("Did Trump stage his own assassination attempt?","lol")
print(x1)
x2 = add_comment(x1,"joe","yes he did")
print(x2)
for i in range(495):
	x2 = like(x2)
print(x2)