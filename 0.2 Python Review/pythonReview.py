def create_youtube_video(title,description):
		youtube_video = {"Title":title,"Description":description,"Likes":0,"Dislikes":0,"Comments":{},"Hashtags":[]}
		for i in range(5):
			youtube_video["Hashtags"].append(input("Tag " + str(i+1) + ": "))
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
def similarity_to_video(v1,v2):
	sim = 0;
	for i in range(5):
		if v1["Hashtags"][i] == v2["Hashtags"][i]:
			sim += 20
	return sim
x1 = create_youtube_video("Did Trump stage his own assassination attempt?","lol")
y1 = create_youtube_video(input("Title: "),input("Desc: "))
print(x1)
x2 = add_comment(x1,"joe","yes he did")
print(x2)
for i in range(495):
	x2 = like(x2)
print(x2)
print(similarity_to_video(x1,y1))
if x1["Likes"] > 20 and x1["Likes"] > x1["Dislikes"]:
	print(x1["Title"] + " is trending!")