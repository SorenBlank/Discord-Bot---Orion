import discord
from discord import Intents
from discord.ext import commands
from discord.ext import commands, tasks
import random
import asyncio
import wikipedia as wiki
import math
import sqlite3
import os
import psycopg2

base = sqlite3.connect("all.db")
cur = base.cursor()

class P1(commands.Cog):

	def __init__(self, client):
		self.client = client
	
	au = 0
	@commands.Cog.listener()
	async def on_ready(self):
		print("P1 is Loaded ----")

	@commands.group(invoke_without_command = True,case_insensitive=True,aliases = ["r","re","resources"])
	async def resource(self,ctx):
		rs = discord.Embed(title = "= = = = = | 📚 Learning Resources 📚 | = = = =", description= "Aliases = `re`,`resource`,`resources`\nFor more info: `.o help`\n-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -")

		rs.add_field(name = "―――――――――――――――――――――――――\n<:python:814811189241970718> PYTHON LEARNING RESOURCES",
					 value= ":small_orange_diamond: Here you will find some useful python learning resources that will help you go master or advance your python skills.\n**__Command:__** `.o resource python`",
					 inline = False)
		rs.add_field(name = "―――――――――――――――――――――――――\n<:html:815225352958771210> WEB DEVELOPMENT RESOURCES",
					 value = ":small_orange_diamond: Here you will find useful web development learning resources for any code newbie who is trying to learn web development.\n**__Command:__** `.o resource web`",
					 inline = False)

		rs.add_field(name = "―――――――――――――――――――――――――\n<:android:814849449570205736> ANDROID DEVELOPMENT RESOURCES",
					 value = ":small_orange_diamond: Here you will find some useful resources if you are interested in Android development.\n**__Command:__** `.o resource android`",
					 inline = False)

		rs.add_field(name = "―――――――――――――――――――――――――\n<:iOS:814846523128676372> iOS DEVELOPMENT RESOURCES",
					 value = ":white_small_square: Here you will find some useful iOS development learning resources to quick-start your iOS development journey.\n**__Command:__** `.o resource ios`",
					 inline = False)

		rs.add_field(name = "―――――――――――――――――――――――――\n:gear: MACHINE LEARNING RESOURCES",
					 value = ":small_orange_diamond: Here is a brief overview of the magnificent world of machine learning. Hope you find something useful or interesting!\n**__Command:__** `.o resource ml`",
					 inline = False)

		rs.add_field(name = "―――――――――――――――――――――――――\n:keyboard: GENERAL PROGRAMMING RESOURCES",
					 value = ":small_orange_diamond: Here are some general resources that you all will find useful, they aren't based on one specific topic. So there should be something here for everyone.\n**__Command:__** `.o resource programming`",
					 inline = False)

		rs.add_field(name = "―――――――――――――――――――――――――\n<:linux:814863906756624384> LINUX GUIDE",
					 value = ":small_orange_diamond: Here is a guide to getting started with linux. Hope everyone will find it very useful.\n__**Command:**__ `.o resource linux`",
					 inline = False)

		

		rs.set_footer(icon_url=ctx.author.avatar_url,text=f"Requested by {ctx.author.name}")
		await ctx.send(embed = rs)


	@resource.command(aliases = ["py"])
	async def python(self,ctx):
		py = discord.Embed(title = "= = =|<:python:814811189241970718> Python Learning Resources <:python:814811189241970718>|= = =",
						   color = 0xffd43b,
						   description = "Here are some python learning resources that will help you go master or advance your python skills.\n\
-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -\n\
:free: **FREE RESOURCES**\n\
:small_blue_diamond: [Python course by AlphaCodingSkills](https://www.alphacodingskills.com/python/python-introduction.php)\n\
:small_blue_diamond: [Python course for beginners by Tultlane](https://www.tutlane.com/tutorial/python/python-data-types)\n\
:small_blue_diamond: [Learn Python from basics to Advanced by TechBeamers](https://www.techbeamers.com/python-data-types-learn-basic-advanced/)\n\
:small_blue_diamond: [Google's Python Class](https://developers.google.com/edu/python/)\n\
:small_blue_diamond: [A Byte of Python](https://python.swaroopch.com/)\n\
:small_blue_diamond: [Free Interactive Python Tutorial](https://www.learnpython.org/)\n\
:small_blue_diamond: [Free Interactive Python Tutorial by DataCamp](https://www.datacamp.com/courses/intro-to-python-for-data-science?utm_source=learnpython_com&utm_campaign=learnpython_tutorials)\n\
:small_blue_diamond: [Python for everybody Specialization by Coursera](https://www.coursera.org/specializations/python)\n\
:small_blue_diamond: [Python Track from Basics to Advanced by Exercism](https://exercism.io/tracks/python)\n឵឵")


		py.add_field(name = ":dollar: PAID RESOURCES",
value = "\
:small_orange_diamond: [Learn Python Programming Masterclass from Udemy](https://www.udemy.com/course/python-the-complete-python-developer-course/)\n\
:small_orange_diamond: [Learn Python The hard way](https://learnpythonthehardway.org/python3/)\n\
:small_orange_diamond: [Learn Python Programming Masterclass](https://www.codecademy.com/learn/learn-python-3)\n឵឵",
					 inline = False)

		py.add_field(name = "<:youtube:814913080357027861> YOUTUBE RESOURCES",
value = "\
:small_blue_diamond: [Learn Python - Full Course for beginners by FreeCodeCamp](https://www.youtube.com/watch?v=rfscVS0vtbw&feature=emb_title)\n\
:small_blue_diamond: [Python Tutorial - Python for Beginners 2020 by Programming With Mosh](https://www.youtube.com/watch?v=kqtD5dpn9C8)\n\
:small_blue_diamond: [Python Tutorial for Absolute Beginners by CS Dojo](https://www.youtube.com/watch?v=Z1Yd7upQsXY&list=PLBZBJbE_rGRWeh5mIBhD-hhDwSEDxogDg)\n\
:small_blue_diamond: [Python Tutorial for Beginners by Corey Schafer](https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)\n\
:small_blue_diamond: [Python Tutorial for Beginners by Clever Programmer](https://www.youtube.com/watch?v=4F2m91eKmts)\n\
:small_blue_diamond: [Python Programming Tutorial for Beginners by Telusko](https://www.youtube.com/watch?v=4F2m91eKmts)\n\
:small_blue_diamond: [Python Full Course - Learn Python in 12 Hours by Edureka!](https://www.youtube.com/watch?v=WGJJIrtnfpk)\n឵឵",
					 inline = False)

		py.add_field(name = ":orange_book: BOOKS",
value = "\
:small_orange_diamond: [Python Python Crash Course](https://www.amazon.com/dp/1593276036/?tag=devdetailpage02-20)\n\
:small_orange_diamond: [Learn Python 3 the Hard Way](https://www.amazon.com/dp/0134692888/?tag=devdetailpage02-20)\n\
:small_orange_diamond: [Head First Python](https://www.amazon.com/dp/1491919531/?tag=devdetailpage02-20)\n\
:small_orange_diamond: [Invent Your Own Computer Games with Python](https://www.amazon.com/dp/1593277954/?tag=devdetailpage02-20)\n\
:small_orange_diamond: [Python Tricks: A Buffet of Awesome Python Features](https://www.amazon.com/dp/1775093301/?tag=devdetailpage02-20)\n\
:small_orange_diamond: [Effective Python: 59 Specific Ways to Write Better Python](https://www.amazon.com/dp/0134034287/?tag=devdetailpage02-20)\n\
:small_orange_diamond: [Learning Python by Mark Lutz](https://www.amazon.com/Learning-Python-5th-Mark-Lutz/dp/1449355730/ref=sr_1_3?dchild=1&keywords=python&qid=1607516757&sr=8-3)\n឵឵",
					 inline = False)

		py.add_field(name = ":boxing_glove: PYTHON EXERCISES/CHALLENGES",
					 value = "\
:small_blue_diamond: [Python Challenges on HackerRank](https://www.codewars.com/)\n\
:small_blue_diamond: [Python Challenges on CodeWars](https://www.codewars.com/)\n\
:small_blue_diamond: [Python Challenges on Exercism](https://exercism.io/tracks/python)",
					 inline = False)
		await ctx.send(embed = py)

	@resource.command()
	async def web(self,ctx):
		web = discord.Embed(title = "= ==|<:html:815225352958771210>Web Dev Learning Resources<:css:815225369040519168>|== =",
				  color = 0xf16524,
				  description = "Here you will find useful web development learning resources for any code newbie who is trying to learn web development, below is a list of resources you can use to start your journey.\n\
-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -")
		web.add_field(name = "🌐 ONLINE COURSES & BOOT CAMPS",
					  value = "\
:small_blue_diamond:[W3Schools](https://www.w3schools.com/)\n\
W3Schools is optimized for learning, testing, and training.\n\
:small_blue_diamond:[freeCodeCamp](https://www.freecodecamp.org/)\n\
Learn how to code from scratch, build projects and earn certificates.\n\
:small_orange_diamond:[Udemy](https://www.udemy.com/)\n\
Learn by following courses, build projects and earn certificates. Has over 10+ million students yearly.\n\
:small_orange_diamond:[Codecademy](https://www.codecademy.com/)\n\
Learn by doing, get instant feedback and put your learning into practice.\n\
:small_orange_diamond:[Coursera](https://www.coursera.org/)\n\
Build skills with courses from top universities like Yale, Michigan, Stanford or Harvard. Get certs on paid courses.\n\
:small_blue_diamond:[Khan Academy](https://www.khanacademy.org/)\n\
Free trusted online classes and practice at your own pace.\n឵឵",
					 inline = False)

		web.add_field(name = "<:udemy:814951952022110258> UDEMY RESOURCES",
			value = "\
:small_orange_diamond: [Build Responsive Real World Websites with HTML5 and CSS3](https://www.udemy.com/course/design-and-develop-a-killer-website-with-html5-and-css3/)\n\
:small_orange_diamond: [Advanced CSS and Sass: Flexbox, Grid, Animations and More](https://www.udemy.com/course/advanced-css-and-sass/)\n\
:small_orange_diamond: [The Complete JavaScript Course 2020: From Zero to Expert!](https://www.udemy.com/course/the-complete-javascript-course/)\n\
:small_orange_diamond: [Colt steele course](https://www.udemy.com/course/the-web-developer-bootcamp/)\n឵឵",
			inline = False)

		web.add_field(name = "<:react:814959323599077436> REACT LEARNING RESOURCES",
			value = "\
:small_blue_diamond:[Full React Course 2020 by freeCodeCamp](https://www.youtube.com/watch?v=4UZrsTqkcW4)\n\
:small_blue_diamond:[React Js tutorial by Brian Design](https://www.youtube.com/watch?v=9ohK7CapmIs&list=PLs1fqgQpnCmJSkrDA2wTsSsLnYpE8jpVy&index=10)\n\
:small_orange_diamond:[React - The Complete Guide by Max](https://www.udemy.com/course/react-the-complete-guide-incl-redux/)\n\
:small_orange_diamond:[Modern React with Redux](https://www.udemy.com/course/react-redux/)\n឵឵",
			inline = False)

		web.add_field(name = "<:youtube:814913080357027861> YOUTUBE RESOURCES",
			value = "\
:small_blue_diamond: [Traversy Media](https://www.youtube.com/channel/UC29ju8bIPH5as8OGnQzwJyA)\n\
:small_blue_diamond: [The Net Ninja](https://www.youtube.com/channel/UCW5YeuERMmlnqo4oq8vwUpg)\n\
:small_blue_diamond: [Dev Ed](https://www.youtube.com/channel/UClb90NQQcskPUGDIXsQEz5Q)\n\
:small_blue_diamond: [Florin Pop](https://www.youtube.com/channel/UCeU-1X402kT-JlLdAitxSMA)\n\
:small_blue_diamond: [Fun Fun Function](https://www.youtube.com/channel/UCO1cgjhGzsSYb1rsB4bFe4Q)\n\
:small_blue_diamond: [Web Dev Simplified](https://www.youtube.com/channel/UCFbNIlppjAuEX4znoulh0Cw)\n\
:small_blue_diamond: [Academind](https://www.youtube.com/channel/UCSJbGtTlrDami-tDGPUV9-w)\n\
:small_blue_diamond: [Kevin Powell](https://www.youtube.com/channel/UCJZv4d5rbIKd4QHMPkcABCw)\n឵឵",
			inline = False)

		web.add_field(name = ":blue_book: BOOKS",
			value = "\
:small_orange_diamond:[You dont know Js](https://github.com/getify/You-Dont-Know-JS)\n\
:small_orange_diamond:[Eloquent Js](https://www.amazon.com/Eloquent-JavaScript-3rd-Introduction-Programming/dp/1593279507)\n឵឵",
			inline = False)

		web.add_field(name = ":boxing_glove: FRONT END PRACTICE SITES",
			value = "\
:small_blue_diamond:[Front End Mentors](https://www.frontendmentor.io/)\n\
:small_blue_diamond:[Dev Challenges](https://devchallenges.io/)\n឵឵",
			inline = False)

		web.add_field(name = ":map: ROADMAPS",
			value = "\
:white_small_square:[Frontend Roadmap](https://www.freecodecamp.org/news/2019-web-developer-roadmap/)\n\
:white_small_square:[Backend Roadmap](https://www.freecodecamp.org/news/2019-web-developer-roadmap/)\n\
:white_small_square:[Full Stack Roadmap](https://levelup.gitconnected.com/the-2020-web-developer-roadmap-76503ddfb327)")

		await ctx.send(embed = web)

	@resource.command(aliases = ["an"])
	async def android(self,ctx):
		an = discord.Embed(title = "===| <:android:814849449570205736> Android Dev Resources <:android:814849449570205736> |===",
			color = 0x3ddb86,
			description = "Here you will find some useful resources if you are interested in Android development.\n\
-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -")
		an.add_field(name = ":dollar: PAID RESOURCES",
			value = "\
:small_orange_diamond:[The Complete Android Developer Course: Beginner To Advanced](https://www.udemy.com/course/androidcourse/?LSNPUBID=JVFxdTr9V80&ranEAID=JVFxdTr9V80&ranMID=39197&ranSiteID=JVFxdTr9V80-mBac39g5jAR5YrHl6Bl4dA&utm_medium=udemyads&utm_source=aff-campaign)\n\
:small_orange_diamond:[Coding with Mitch](https://codingwithmitch.com/)\n\
:small_orange_diamond:[Udacity: Become an Android Developer by Google](https://www.udacity.com/course/android-developer-nanodegree-by-google--nd801)\n឵឵",
			inline = False)

		an.add_field(name = "<:youtube:814913080357027861> YOUTUBE RESOURCES",
			value = "\
:small_blue_diamond:[Android developers](https://www.youtube.com/user/androiddevelopers)\n\
:small_blue_diamond:[Goobar](https://www.youtube.com/channel/UCVysWoMPvvHQMEJvRkslbAQ)\n\
:small_blue_diamond:[Coding with Mitch](https://www.youtube.com/channel/UCoNZZLhPuuRteu02rh7bzsw)\n\
:small_blue_diamond:[Raywenderlich](https://www.raywenderlich.com/android/videos)\n឵឵",
			inline = False)

		an.add_field(name = ":microphone2: PRODCAST & COMMUNITIES AND BLOGS",
			value = "\
:small_blue_diamond:[The official Android Developers publication on Medium](https://medium.com/androiddevelopers)\n\
:small_blue_diamond:[Android developers blog by Nick Rout](https://android-developers.googleblog.com/)\n\
:small_blue_diamond:[Fragmented](https://fragmentedpodcast.com/)\n\
:small_blue_diamond:[MindOrks](https://mindorks.com/)\n\
:small_blue_diamond:[Raywenderlich](https://www.raywenderlich.com/android/articles)\n឵឵",
			inline = False)

		an.add_field(name = "<:git:814810927748218934> LIBRARIES & FRAMEWORKS & APPS",
			value = "\
If you need a collection of open-source apps, library and frameworks, you can checkout this awesome person's [GitHub](https://github.com/moeindev?tab=stars) stars.\n឵឵")

		an.add_field(name = ":map: ROADMAP",
			value = ":small_blue_diamond: [Android Developer Roadmap by MindOrks](https://github.com/MindorksOpenSource/android-developer-roadmap)",
			inline = False)

		await ctx.send(embed = an)



	@resource.command()
	async def ios(self,ctx):
		ios = discord.Embed(title = "= = = = =|<:iOS:814846523128676372> iOS Dev Resources <:iOS:814846523128676372>|= = = = =",
			color = 0xea1e5d,
			description = "Here you will find some useful iOS development learning resources to quick-start your iOS development journey. \
The majority of resources and recommendations are geared towards native iOS development. Many may apply to cross-platform development as well.\n\
-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -")

		ios.add_field(name = ":green_book: GENERAL RESOURCES",
			value = "\
:small_blue_diamond:[Apple Developer](https://developer.apple.com/)\n\
:small_blue_diamond:[Ray Wenderlich](https://www.raywenderlich.com/)\n\
:small_blue_diamond:[HackingWithSwift](https://www.hackingwithswift.com/)\n\
:small_blue_diamond:[Medium](https://medium.com/)\n឵឵",
			inline = False)

		ios.add_field(name = "<:udemy:814951952022110258> UDEMY RESOURCES",
			value = "\
:small_orange_diamond:[iOS 13 & Swift 5 - The Complete iOS App Development Bootcamp](https://www.udemy.com/course/ios-13-app-development-bootcamp/)\n\
:small_orange_diamond:[iOS 14, Swift 5 & SwiftUI - The iOS Development Starter Kit](https://www.udemy.com/course/swift-starter-kit/)\n឵឵",
			inline = False)

		ios.add_field(name = "<:swift:815125486560608266> SWIFT LEARNING RESOURCES",
			value = "\
:small_blue_diamond:[Apple Developer - SwiftUI Tutorials](https://developer.apple.com/tutorials/swiftui/)\n\
:small_blue_diamond:[HackingWithSwift - SwiftUI Quick-Start](https://www.hackingwithswift.com/quick-start/swiftui)\n\
:small_blue_diamond:[Ray Wenderlich - Getting Started](https://www.raywenderlich.com/3715234-swiftui-getting-started)\n\
:small_blue_diamond:[Medium - You got this! Learn to build your first app](https://medium.com/swift-programming/swiftui-you-got-this-learn-to-build-your-first-app-part-1-of-3-56c8b918dc0a)\n឵឵")

		ios.add_field(name = ":question: Q&A",
			value = ":large_blue_diamond:[StackOverflow](http://stackoverflow.com/)\n\
:small_blue_diamond:- [iOS](https://stackoverflow.com/questions/tagged/ios)\n\
:small_blue_diamond:- [Swift](https://stackoverflow.com/questions/tagged/swift)/[Swift5](https://stackoverflow.com/questions/tagged/swift5)\n\
:small_blue_diamond:- [Objective-C](https://stackoverflow.com/questions/tagged/objective-c)\n\
:small_blue_diamond:- [Xcode](https://stackoverflow.com/questions/tagged/xcode)\n\
:small_blue_diamond:- [Core-Data](https://stackoverflow.com/questions/tagged/core-data)\n\
:small_blue_diamond:- [Apple Developer Forums](https://developer.apple.com/forums/)\n឵឵",
			inline = False)

		ios.add_field(name = ":pencil: EDITORIALS",
			value = "\
:white_small_square:[Open Source Learning ~ iOS Programming - by Greyson Murray](https://gist.github.com/greysonDEV/add089a24ea0392414a415ab3f081db6)\n\
:white_small_square:[Quick-start guide create apps in Swift without storyboards - by Greyson Murray](https://gist.github.com/greysonDEV/25d5347f2f708715934706dfe09a8686)",
			inline = False)
		await ctx.send(embed = ios)
	

	@resource.command(aliases = ["ml"])
	async def machine(self,ctx):
		ml = discord.Embed(title = "= = =|:gear:Machine Learning Resources:gear:|= = =",
						   color = 0x1cb1c2,
						   description = "Here is a brief overview of the magnificent world of machine learning. Hope you find something useful or interesting!\n\
-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -")

		ml.add_field(name = ":globe_with_meridians: WEBSITES",
			value = "\
:small_blue_diamond:[List of papers](https://paperswithcode.com/)\n\
:small_blue_diamond:[Easy to read articles](https://towardsdatascience.com/)\n\
:small_blue_diamond:[Description of terms you might encounter in machine learning](https://www.investopedia.com/financial-term-dictionary-4769738)\n឵឵",
			inline = False)

		ml.add_field(name = "<:youtube:814913080357027861> YOUTUBE RESOURCES",
			value = "\
:small_blue_diamond:[Jeff Heaton](https://www.youtube.com/c/HeatonResearch/)\n\
:small_blue_diamond:[StatQuest](https://www.youtube.com/c/joshstarmer/)\n\
:small_blue_diamond:[3Blue1Brown](https://www.youtube.com/c/3blue1brown/)\n\
:small_blue_diamond:[Tensorflow](https://www.youtube.com/c/TensorFlow/)\n\
:small_blue_diamond:[Two Minute Papers](https://www.youtube.com/user/keeroyz)\n\
:small_blue_diamond:[Computerphile](https://www.youtube.com/user/Computerphile)\n឵឵",
			inline = False)

		ml.add_field(name = ":tools: MACHINE LEARNING FRAMEWORKS",
			value = "\
:one: [Scikit-learn](https://scikit-learn.org/stable/)\n\
This framework is really good if you don't need the performance boost from using a GPU and you're not interested in designing your own neural networks. \
The documentation explains every topic and there are a lot of examples to learn from.\n\n\
:two: [Tensorflow](https://www.tensorflow.org/)\n\
Machine learning framework by Google.\n\n\
:three: [Pytorch](https://pytorch.org/)\n\
Machine learning framework by Facebook.\n឵឵",
			inline = False)

		ml.add_field(name = ":card_box: DATA SOURCES",
			value = ":one: [Public Datasets on Github](https://github.com/awesomedata/awesome-public-datasets)\n\
:two: [Public Datasets on Kaggle](https://www.kaggle.com/datasets)\n឵឵",
			inline = False)

		ml.add_field(name = ":blue_book: BOOKS",
			value = "\
:one: [Python for Data Analysis - Wes McKinney](https://amzn.to/37TahYG)\n\
This is a really good starting point if you are new to the field.\n\
:two: [Introduction to Data Mining - University of Minnesota](https://amzn.to/3qZZ9kf)\n\
This is a good resource if you already know some computer science. It introduces these topics: classification, association analysis, clustering, and anomaly detection.\n\
:three: [Machine Learning: A Bayesian and Optimization Perspective - Sergios](https://amzn.to/2ZSrsVM)\n\
This is the book to get if you love linear algebra and calculus. You will learn the math behind the most important parts of machine learning.\n\
:four: [Deep Learning - Goodfellow, Bengio, Courville](https://amzn.to/3dR5g6x)\n\
This is the book to read to learn deep learning.\n\
:five: [An Introduction to Statistical Learning](https://amzn.to/3syK7lW)\n\
This is the book to get if you love statistics.\n឵឵",
			inline = False)

		ml.add_field(name = ":bookmark_tabs: RELATED TOPICS",
			value = ":small_blue_diamond:[Apache Hadoop](https://hadoop.apache.org/) and [Apache Spark](https://spark.apache.org/)\n\
:small_blue_diamond:[Information retrieval](https://en.wikipedia.org/wiki/Information_retrieval)\n\
:small_blue_diamond:[Natural Language Processing](https://towardsdatascience.com/your-guide-to-natural-language-processing-nlp-48ea2511f6e1)\n\
:small_blue_diamond:[Databases](https://www.w3schools.in/dbms/database/)\n\
:small_blue_diamond:[Genetic Algorithms](https://www.geeksforgeeks.org/genetic-algorithms/)\n\
:small_blue_diamond:[Computer Vision](https://www.sciencedirect.com/science/article/pii/S1877050920308218)\n឵឵",
			inline = False)

		ml.add_field(name = ":notepad_spiral: FINAL NOTE",
			value = "\
The limit of what we think it is possible to do in the field of artificial intelligence is constantly moving forwards. \
If you want to follow the newest research I suggest reading some of the [papers published on the arXiv website by Cornell University](https://arxiv.org/corr/subjectclasses).",
			inline = False)
		await ctx.send(embed = ml)


	@resource.command(aliases = ["pro"])
	async def programming(self,ctx):
		pro = discord.Embed(title = "= =|:keyboard: PROGRAMMING RESOURCES :keyboard:|= =",
							description = "Here are some general resources that you all will find useful, they aren't based on one specific topic. So there should be something here for everyone.\n\
-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -")

		pro.add_field(name = ":pencil: TEXT EDITORS",
			value = "Text Editors are what allow us to write the code for our program. There are currently many great text editors in the market. Here are some options for you to choose from:\n\n\
<:vscode:814499769065799741> **VS Code**\n\
[Official website](https://code.visualstudio.com/) | [Tutorial](https://flaviocopes.com/vscode/)\n\n\
<:sublime:814475264330694746> **Sublime Text**\n\
[Official website](https://www.sublimetext.com/) | [Tutorial](https://www.tutorialspoint.com/sublime_text/index.htm)\n\n\
<:atom:814811145088008212> **Atom**\n\
[Official website](https://atom.io/) | [Tutorial](https://flight-manual.atom.io/getting-started/)\n\n\
<:vim:815301084473720832> **Vim**\n\
[Official website](https://www.vim.org/) | [Tutorial](https://danielmiessler.com/study/vim/)\n\n\
There are many more text editors, but these are some of the most popular ones.\n឵឵",
			inline = False)

		pro.add_field(name = ":books: FREE PROGRAMMING BOOKS",
			value = "Here you can find a total of 48 books, each of them covering a specific language. \n\
And then one extra book covering competitive programming. All of these can be downloaded in the form of a pdf:\n\n\
:small_blue_diamond:[48 Free Programming Books](https://books.goalkicker.com/)\n\
:small_blue_diamond:[Competitive Programmer's Handbook by Antti Laaksonen](https://github.com/pllk/cphb)\n឵឵",
			inline = False)

		pro.add_field(name = ":bulb: PROBLEM SOLVING",
			value = "\
Having problem solving skills is an invaluable asset everyone should know in general life also, not just in programming. \
Here is an article which should help you get an idea of what problem-solving skills are:\n\n\
:small_blue_diamond:[Problem-solving skills by Richard Reis](https://www.freecodecamp.org/news/how-to-think-like-a-programmer-lessons-in-problem-solving-d1d8bf1de7d2/)\n឵឵",
			inline = False)

		pro.add_field(name = ":art: DESIGN RESOURCES",
			value = "\
Here you will find lots of designing stuff, including but not limited to, UI Graphics, Fonts, Icons/Logos, CSS Animations, CSS Frameworks, and many more resources. Check it out for yourself:\n\n\
:small_blue_diamond:[Design resources for Developers by Bradtraversy](https://github.com/bradtraversy/design-resources-for-developers#css-animations)",
			inline = False)

		await ctx.send(embed = pro)

	@resource.command(aliases = ["li"])
	async def linux(self,ctx):

		li = discord.Embed(title = "= = = = =| <:linux:814863906756624384> Linux Guide <:linux:814863906756624384>|= = = = =",
			description = "Here is a guide to getting started with linux. Hope everyone will find it very useful.\n\
-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -")

		li.add_field(name = ":page_facing_up: STARTER",
			value = ":white_small_square:[What is Linux?](https://www.youtube.com/watch?v=6gqLWTSz6ck)\n\
:white_small_square:[What distribution to choose?](https://distrochooser.de/en)\n឵឵",
			inline = False)

		li.add_field(name = ":children_crossing: WAYS TO USE LINUX",
			value = "\
:one: Virtual Machine - [Article](https://www.addictivetips.com/ubuntu-linux-tips/set-up-linux-virtual-machine-on-windows/)/[Video](https://www.youtube.com/watch?v=lzRMYTf6X2o)\n\
:two: WSL(Windows Subsystem for Linux) - [Article](https://christitus.com/wsl2/)/[Video](https://youtu.be/VUW2pIjDpEk)\n\
:three: Full Installation\n឵឵",
			inline = False)

		li.add_field(name = ":cd: BOOTABLE MEDIA CREATION GUIDE",
			value = "\
:small_blue_diamond:[Guide](https://fossbytes.com/create-bootable-usb-media-rufus-install-windows-linux/) for using [Rufus](https://rufus.ie/) in a Windows desktop.\n\
:small_blue_diamond:[Guide](https://recalbox.gitbook.io/tutorials/utility/flashing-an-image/balena-etcher-tutorial) for using [Balena Etcher](https://www.balena.io/etcher/) in a Windows/Linux/MacOS desktop.\n឵឵",
			inline = False)

		li.add_field(name = ":tools: INSTALLATION GUIDES",
			value = "\
Here are installation guides for some popular Linux distributions\n\n\
:one: <:ubuntu:814858579222724618> Ubuntu - [Article](https://ubuntu.com/tutorials/install-ubuntu-desktop1-overview)/[Video](https://www.youtube.com/watch?v=G7ffzC4S0A4)\n\n\
:two: <:debian:814859002780581899> Debian - [Article](https://www.debian.org/releases/stable/installmanual)/[Video](https://www.youtube.com/watch?v=P4J_99cS7Bg)\n\n\
:three: <:arch:814858893993705542> Arch Linux - [Article](https://wiki.archlinux.org/index.php/Installation_guide)/[Video](https://www.youtube.com/watch?v=PQgyW10xD8s)\n\n\
:four: <:manjaro:814857561252823090> Manjaro - [Article](https://itsfoss.com/install-manjaro-linux/)/[Video](https://www.youtube.com/watch?v=4tGK9OCcSPk)\n឵឵")

		await ctx.send(embed = li)



	@commands.Cog.listener()
	async def on_message(self, message):

		#making the message.content lower case in order to make the commands case insensitive
		ex_1 = message.content.lower().replace(',','')
		ex_2 = ex_1.replace("?","")
		etxt = ex_2
		
		#splitting the exact_txt
		exact_txt_splitted = etxt.split(" ")



										###########################
										##   Wikipedia Command   ##
										###########################
		if etxt.startswith(".o wiki") or etxt.startswith(".o wikipedia"):
			cur.execute("SELECT*FROM WC")
			all = cur.fetchall()

			guilds = []
			channels = []
			ch = 0
			for i in all:
				guilds.append(i[0])
				channels.append(i[1])
				if i[0] == message.guild.id:
					ch = i[1]

			if message.guild.id in guilds:
				if message.channel.id in channels:
					msg = message
					au = message.author.id
					x1 = etxt.split(" ")
					words = [".o","wiki","wikipedia"]
					xwords = [i for i in x1 if i not in words]
					joined = ' '.join(xwords)

					try:
						await msg.channel.send(wiki.summary(joined, sentences=5))
					except wiki.exceptions.DisambiguationError as e:
						m='Search item couldn\'t be distinguished. Here is a list of search results: '
						await msg.channel.send(m)
						items=20
						pages=math.ceil(len(e.options)/items)

						for page in range(pages):
							p=''
							start = (page) * items
							end = min(start + items , len(e.options))
							for i, opt in enumerate(e.options[start:end], start=start):
								p += '**{0}. {1}** \n'.format(i + 1, opt)
							await msg.channel.send(p)
						await msg.channel.send('Now choose the index of your desired search result.')
						msgg=await self.client.wait_for('message')
						while not (msgg.author.id == au and msgg.channel.id == ch):
							msgg=await self.client.wait_for('message')
							pass
						if msgg.author.id == au:
							try:
								msg1 = [words for words in msgg.content.lower().split(" ") if words.isnumeric()]
								ind = int(msg1[0])
								if 1<=ind and ind<=len(e.options):
									await msgg.channel.send(wiki.summary(e.options[ind-1], sentences=5))
								else :
									await msgg.channel.send('The index does not exist. Start over again.')
							except:
								await msgg.channel.send('This page cannot be shown for some unknown reason.')

				if message.channel.id not in channels:
					ch = self.client.get_channel(ch)
					await message.channel.send(f"Please use this {ch.mention} channel.")
			else:
				await message.channel.send("No channel of this server is set as **Wikipedia Channel**.\nPlease set one using this command `.o set wiki (channel)`")

										###########################
										##  Wikipedia Search 2.0 ##
										###########################
		
		sq_1 = [["can", "ask", "question"],
			["something","to","ask"],
			["wanna","ask","something"]]
		
		x = 0
		for i in sq_1:
			for ii in i:
				if ii in exact_txt_splitted:
					x = x + 1
					if x == 3 :
						break
			if x == 3:
				break

		if (etxt.startswith("hey orion") or etxt.startswith("orion"))  and x == 3:
			cur.execute("SELECT*FROM WC")
			all = cur.fetchall()

			guilds = []
			channels = []
			ch = 0
			for i in all:
				guilds.append(i[0])
				channels.append(i[1])
				if i[0] == message.guild.id:
					ch = i[1]

			if message.guild.id in guilds:
				if message.channel.id in channels:
					au=message.author.id
					ch = message.channel.id
					await message.channel.send(random.choice(['Sure, why not?',
															"Sir just ask away",
															"Sure! Ask away."]))
					
					msg= await self.client.wait_for('message')
					while not (msg.author.id == au and msg.channel.id == ch):
						msg=await self.client.wait_for('message')
						pass

					ques=['hey','orion','what','is','are','a',"tell","me","who","about","would","you","mind","telling","where","what's"]
					if msg.author.id == au and msg.channel.id == ch:
						msg_words=msg.content.lower().replace('?','').split(" ")
						que_words=[word for word in msg_words if word not in ques]
						que=' '.join(que_words)
						print(que)
						try:
							await msg.channel.send(wiki.summary(que, sentences=5))
						except wiki.exceptions.DisambiguationError as e:
							m='Search item couldn\'t be distinguished. Here is a list of search results: '
							await msg.channel.send(m)
							items=20
							pages=math.ceil(len(e.options)/items)

							for page in range(pages):
								p=''
								start = (page) * items
								end = min(start + items , len(e.options))
								for i, opt in enumerate(e.options[start:end], start=start):
									p += '**{0}. {1}** \n'.format(i + 1, opt)
								await msg.channel.send(p)
							
							await msg.channel.send('Now choose the index of your desired search result.')
							msgg=await self.client.wait_for('message')
							while not (msgg.author.id == au and msgg.channel.id == ch):
								msgg=await self.client.wait_for('message')
								pass
							if msgg.author.id == au:
								try:
									msg1 = [words for words in msgg.content.lower().split(" ") if words.isnumeric()]
									ind = int(msg1[0])
									if 1<=ind and ind<=len(e.options):
										await msgg.channel.send(wiki.summary(e.options[ind-1], sentences=5))
									else :
										await msgg.channel.send('The index does not exist. Start over again.')
								except:
									await msgg.channel.send('This page cannot be shown for some unknown reason.')
				if message.channel.id not in channels:
					ch = self.client.get_channel(ch)
					await message.channel.send(f"Please use this {ch.mention} channel.")
			else:
				await message.channel.send("No channel of this server is set as **Wikipedia Channel**.\nPlease set one using this command `.o set wiki (channel)`")
			
		

def setup(client):
	client.add_cog(P1(client))