import requests
import json

def getGitStats():
	#Getting commit stats
	response = requests.get("https://api.github.com/repos/mattgallant/AustinConcerts/stats/contributors")
	data = response.json()

	commits = zanderCommits = guyCommits = mattCommits = dylanCommits = willCommits = michaelCommits = 0;
	for i in data:
		if(i.get("author").get("login") == "zandertedjo"):
			zanderCommits = i.get("total")
		if(i.get("author").get("login") == "farmerguycf"):
			guyCommits = i.get("total")
		if(i.get("author").get("login") == "Mattgallant"):
			mattCommits = i.get("total")
		if(i.get("author").get("login") == "dylanwolford"):
			dylanCommits = i.get("total")
		if(i.get("author").get("login") == "michaelhilborn"):
			michaelCommits = i.get("total")
		if(i.get("author").get("login") == "willworthington"):
			willCommits = i.get("total")
		commits += i.get("total")

	#Getting issues stats
	response = requests.get("https://api.github.com/repos/mattgallant/AustinConcerts/issues")
	data = response.json()

	issues = zanderIssues = guyIssues = mattIssues = dylanIssues = willIssues = michaelIssues = 0;
	for i in data:
		if(i.get("user").get("login") == "zandertedjo"):
		    zanderIssues += 1
		if(i.get("user").get("login") == "farmerguycf"):
		    guyIssues += 1
		if(i.get("user").get("login") == "Mattgallant"):
		    mattIssues += 1
		if(i.get("user").get("login") == "dylanwolford"):
		    dylanIssues += 1
		if(i.get("user").get("login") == "michaelhilborn"):
		    michaelIssues += 1
		if(i.get("user").get("login") == "willworthington"):
		    willIssues+= 1

	ret_dict ={
		'totalCommits' : commits,
		'zanderCommits' : zanderCommits,
		'mattCommits' : mattCommits,
		'guyCommits' : guyCommits,
		'willCommits' : willCommits,
		'michaelCommits' : michaelCommits,
		'dylanCommits': dylanCommits,
		'totalIssues' : data[0].get("number"),
		'michaelIssues': michaelIssues,
		'zanderIssues': zanderIssues,
		'mattIssues': mattIssues,
		'guyIssues': guyIssues,
		'willIssues': willIssues,
		'dylanIssues': dylanIssues
	}
	#print(ret_dict)
	return ret_dict