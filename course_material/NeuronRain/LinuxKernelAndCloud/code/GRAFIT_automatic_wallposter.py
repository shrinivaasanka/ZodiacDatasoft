##############################################################################################################################################
#<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
##############################################################################################################################################
#Course Authored By:
#-----------------------------------------------------------------------------------------------------------
#K.Srinivasan
#NeuronRain Documentation and Licensing: http://neuronrain-documentation.readthedocs.io/en/latest/
#Personal website(research): https://sites.google.com/site/kuja27/
#-----------------------------------------------------------------------------------------------------------

import sys
import facebook
import requests

#Function to post in user wall - not invoked at present 
def grafit_wall_post(user,mss):
	token="EAACvK6dFKs8BAPwfAJTDXPvZCXHo42KDAkqZC1WDabI2cba3SYKRZAkr3VxZBgWfsdfwJKEvcMUoqIq7V1ni5PrE9JztHJu58n8N9qQEjVPHQfEZA1SZBdLRwFZCcijdnlwF6XdLNxnzF3zNRuqdI8ZCXmrubKhDKiYfiBXWUwbjCtu1GyJhNOHVCA8Ky8VwMZAqgDZB7kIbP3GAZDZD"
	graph=facebook.GraphAPI(access_token=token,version=3.0)
	profile=graph.put_object(parent_object=user,connection_name="feed",message=mss)
	
def facebook_graph(user):
	token="EAACvK6dFKs8BAPwfAJTDXPvZCXHo42KDAkqZC1WDabI2cba3SYKRZAkr3VxZBgWfsdfwJKEvcMUoqIq7V1ni5PrE9JztHJu58n8N9qQEjVPHQfEZA1SZBdLRwFZCcijdnlwF6XdLNxnzF3zNRuqdI8ZCXmrubKhDKiYfiBXWUwbjCtu1GyJhNOHVCA8Ky8VwMZAqgDZB7kIbP3GAZDZD"

	graph=facebook.GraphAPI(access_token=token,version=3.0)
	profile=graph.get_object(user)
	print("====================")
	print("Posts:")
	print("====================")
	posts = graph.get_connections(profile['id'], 'posts')
	breaking=False
	while posts is not None and not breaking:
		try:
			print(posts)
			posts=requests.get(posts['paging']['next']).json()
			for p in posts['data']:
				comments=graph.get_connections(id=p['id'],connection_name='comments')
				if len(comments['data']) > 0:
					print("===================")
					print("Comments")
					print("===================")
					print(comments)
		except KeyError:
			print("All posts exhausted")
			breaking=True
	Fields=graph.request(user, {"fields":"name"})
	print("====================")
	print("Fields:")
	print("====================")
	print(Fields)
	print("====================")
	print("Connections:")
	print("====================")
	friends = graph.get_connections(id=user, connection_name='friends')
	print(friends['summary'])
	for f in friends['data']:
		print(f)

if __name__=="__main__":
	#facebook_graph(sys.argv[1])
	grafit_wall_post(sys.argv[1],sys.argv[2])
