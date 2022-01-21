import os
os.system("pip install cgi")
os.system("pip install instaloader")
import sys, instaloader, cgi
def todict (list: list):
	_dict = dict ()
	i = 0
	for l in list:
		_dict.update ({i: l})
		i+=1
	return _dict
if not 'tag' in cgi.FieldStorage():
	l = todict (sys.argv)
	if l.get (1, False):
		user = l.get (1)
	else:
		user = None
else:
	user = cgi.FieldStorage().getvalue('tag')
result = {}
if user:
	insta = instaloader.Instaloader()
	try:
		profile = instaloader.Profile.from_username (insta.context, user)
		result['ok'] = True
		result['channel'] = '@GrammerX'
		result['result'] = {}
		result['result']['profile_url'] = profile.profile_pic_url
		result['result']['name'] = profile.full_name
		result['result']['username'] = profile.username
		result['result']['id'] = profile.userid
		result['result']['page_id'] = profile.userid
		result['result']['verified'] = profile.is_verified
		result['result']['private'] = profile.is_private
		result['result']['post'] = profile.mediacount
		result['result']['highlight'] = profile._metadata ('highlight_reel_count')
		result['result']['follower'] = profile.followers
		result['result']['following'] = profile.followees
		result['result']['bio'] = profile.biography
		result['result']['link'] = profile.external_url
	except instaloader.ProfileNotExistsException:
		result['ok'] = False
		result['channel'] = '@ProgFy'
		result['message'] = 'not found page'
else:
	result['ok'] = False
	result['message'] = 'not isset tag'
print (result)