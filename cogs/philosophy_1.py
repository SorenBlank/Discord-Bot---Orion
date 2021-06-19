import discord
from discord import Intents
from discord.ext import commands
from discord.ext import commands, tasks
import random
import asyncio
from discord.ext.commands.core import command
import wikipedia
import math
import os
import pymongo
from pymongo import MongoClient
import random

cluster = MongoClient("mongodb+srv://soren:cdD2_qWUYRk-d4G@orion.iztml.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
base = cluster["OrionDB"]


class P1(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    au = 0
    @commands.Cog.listener()
    async def on_ready(self):
        print("P1 is Loaded ----")

    @commands.group(invoke_without_command = True,case_insensitive=True,aliases = ["r","re","resources"])
    async def resource(self,ctx):
        rs = discord.Embed(color = 0x5865F2)
        rs.set_author(name = "LEARNING RESOURCES",icon_url= self.client.user.avatar_url)
        rs.add_field(name = "<:python:814811189241970718> PYTHON LEARNING RESOURCES",
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


        await ctx.send(embed = rs)


    @resource.command(aliases = ["py"])
    async def python(self,ctx):
        py = discord.Embed(
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
:small_blue_diamond: [Python Challenges on HackerRank](https://www.hackerrank.com/)\n\
:small_blue_diamond: [Python Challenges on CodeWars](https://www.codewars.com/)\n\
:small_blue_diamond: [Python Challenges on Exercism](https://exercism.io/tracks/python)",
                     inline = False)
        py.set_author(name = "PYTHON LEARNING RESOURCES",icon_url="https://cdn.discordapp.com/emojis/814811189241970718.png?v=1")
        await ctx.send(embed = py)

    @resource.command(aliases = ["webdev"])
    async def web(self,ctx):
        web = discord.Embed(
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
        web.set_author(name = "WEB DEV LEARNING RESOURCES",icon_url= "https://cdn.discordapp.com/emojis/815225352958771210.png?v=1")
        await ctx.send(embed = web)

    @resource.command(aliases = ["an","androiddev"])
    async def android(self,ctx):
        an = discord.Embed(
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
        an.set_author(name = "ANDROID DEV RESOURCES", icon_url= "https://cdn.discordapp.com/emojis/814849449570205736.png?v=1")

        await ctx.send(embed = an)



    @resource.command(aliases = ["iosdev"])
    async def ios(self,ctx):
        ios = discord.Embed(
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
        ios.set_author(name = "iOS DEV RESOURCES",icon_url= "https://cdn.discordapp.com/emojis/814846523128676372.png?v=1")
        await ctx.send(embed = ios)
    

    @resource.command(aliases = ["ml","machinelearning"])
    async def machine(self,ctx):
        ml = discord.Embed(
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
        ml.set_author(name = "MACHINE LEARNING RESOURCES",icon_url= "https://cdn.discordapp.com/emojis/814959323599077436.png?v=1")
        await ctx.send(embed = ml)


    @resource.command(aliases = ["pro"])
    async def programming(self,ctx):
        pro = discord.Embed(color = 0x5865F2,
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
        pro.set_author(name = "PROGRAMMING RESOURCES",icon_url= "https://cdn.discordapp.com/emojis/831229972169097257.png?v=1")
        await ctx.send(embed = pro)

    @resource.command(aliases = ["li"])
    async def linux(self,ctx):

        li = discord.Embed(
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
        li.set_author(name = "LINUX GUIDE",icon_url= "https://cdn.discordapp.com/emojis/814863906756624384.png?v=1")
        await ctx.send(embed = li)



    # @commands.command()
    # async def wiki(self,ctx,*,message):
    #     au = ctx.author.id
    #     ch = ctx.channel.id
    #     try:
    #         await ctx.channel.send(wiki.summary(message, sentences=5))
    #     except wiki.exceptions.DisambiguationError as e:
    #         m='Search item couldn\'t be distinguished. Here is a list of search results: '
    #         await ctx.channel.send(m)
    #         items=20
    #         pages=math.ceil(len(e.options)/items)

    #         for page in range(pages):
    #             p=''
    #             start = (page) * items
    #             end = min(start + items , len(e.options))
    #             for i, opt in enumerate(e.options[start:end], start=start):
    #                 p += '**{0}. {1}** \n'.format(i + 1, opt)
    #             await ctx.channel.send(p)
    #         await ctx.channel.send('Now choose the index of your desired search result.')
    #         msgg=await self.client.wait_for('message')
    #         while not (msgg.author.id == au and msgg.channel.id == ch):
    #             msgg=await self.client.wait_for('message')
    #             pass
    #         if msgg.author.id == au:
    #             try:
    #                 msg1 = [words for words in msgg.content.lower().split(" ") if words.isnumeric()]
    #                 ind = int(msg1[0])
    #                 if 1<=ind and ind<=len(e.options):
    #                     await msgg.channel.send(wiki.summary(e.options[ind-1], sentences=5))
    #                 else :
    #                     await msgg.channel.send('The index does not exist. Start over again.')
    #             except:
    #                 await msgg.channel.send('This page cannot be shown for some unknown reason.')
    
    @commands.command(aliases = ["wikipedia"])
    async def wiki(self,ctx,*,message):
        try:
            x = wikipedia.search(message)
            page = wikipedia.page(x[0])
            #summary = wikipedia.summary(page.title, sentences = 5)
            summary = page.summary
            summary = summary.split(".")
            summary = ". ".join(summary[:5])
            embed = discord.Embed(color = 0x5865F2,title = page.title, url = page.url,
            description = f"{summary}......[more]({page.url})")
            embed.set_author(name="Wikipedia", icon_url="https://cdn.discordapp.com/attachments/777124925219536911/829261559216734218/1200px-Wikipedia-logo-v2.svg.png")
            
            await ctx.send(embed = embed)
        except wikipedia.exceptions.DisambiguationError as e:
            count = 0
            full = e.options
            all_pages = []
            s = []
            for i in full:
                if count != 10:
                    s.append(i)
                    count += 1
                else:
                    all_pages.append(s)
                    s = []
                    count = 0
            page = 0
            pages = len(all_pages)
            text = ""
            num = 1
            for i in all_pages[page]:
                text = text + str(num) +' - '+ i + "\n"
                num += 1
            embed = discord.Embed(color = 0x5865F2,description = "Use the command `.o wiki <search>` to search.")
            embed.set_author(name="Wikipedia", icon_url="https://cdn.discordapp.com/attachments/777124925219536911/829261559216734218/1200px-Wikipedia-logo-v2.svg.png")
            embed.add_field(name = f'"{message}" might refer to-',
            value = text,
            inline= False)
            link_msg = await ctx.send(embed = embed)

            def react_check(reaction, user): #reaction check function
                emojis = ["🚫","➡️","⬅️"]
                return user.id == ctx.author.id and reaction.message.id == link_msg.id and str(reaction.emoji) in emojis
            
            
            clean_emoji = True

            while True: # looping between pages
                if page == 0:
                    if not clean_emoji:
                        for i in emojis:
                            await link_msg.clear_reaction(i) # remove emoji if exists

                    emojis = ["🚫","➡️"]
                    for emoji in emojis:
                        await link_msg.add_reaction(emoji) # add emoji to link_msg
                
                    clean_emoji = True
                    
                elif page == pages-1:
                    if not clean_emoji:
                        for i in emojis:
                            await link_msg.clear_reaction(i) # remove emoji if exists

                    emojis = ["⬅️","🚫"]
                    for emoji in emojis:
                        await link_msg.add_reaction(emoji)
                    
                    clean_emoji = True
                else:
                    if clean_emoji:
                        for i in emojis:
                            await link_msg.clear_reaction(i) # remove emoji if exists

                    emojis = ["⬅️","➡️"]
                    for emoji in emojis:
                        await link_msg.add_reaction(emoji)
                
                    clean_emoji = False
                
                try: # to handle timeout error
                    user_react,user = await self.client.wait_for("reaction_add", check = react_check, timeout=60)
                    
                    if user_react.emoji == "➡️" and page != pages-1:
                        page += 1
                        num = str(page)+"1"
                        num = int(num)
                        text = ""
                        for i in all_pages[page]:
                            text = text + str(num) +' - '+ i + "\n"
                            num += 1

                        embed = discord.Embed(description = text)
                        embed.set_author(name="Wikipedia", icon_url="https://cdn.discordapp.com/attachments/777124925219536911/829261559216734218/1200px-Wikipedia-logo-v2.svg.png")
                        await link_msg.edit(embed = embed)
                        await link_msg.remove_reaction(user_react, user)

                    if user_react.emoji == "⬅️" and page > 0:
                        page -= 1
                        num = str(page)+"1"
                        num = int(num)
                        text = ""
                        for i in all_pages[page]:
                            text = text + str(num) +' - '+ i + "\n"
                            num += 1
                        if page == 0:
                            embed = discord.Embed(description = "Use the command `.o wiki <search>` to search.")
                            embed.set_author(name="Wikipedia", icon_url="https://cdn.discordapp.com/attachments/777124925219536911/829261559216734218/1200px-Wikipedia-logo-v2.svg.png")
                            embed.add_field(name = f'"{message}" might refer to-',
                            value = text,
                            inline= False)
                        else:
                            embed = discord.Embed(description = text)
                            embed.set_author(name="Wikipedia", icon_url="https://cdn.discordapp.com/attachments/777124925219536911/829261559216734218/1200px-Wikipedia-logo-v2.svg.png")
                        await link_msg.edit(embed = embed)
                        await link_msg.remove_reaction(user_react, user)
                    
                    if user_react.emoji == "🚫":
                        if react_check(user_react,user):
                            await link_msg.clear_reactions()
                            break
                        
                
                except asyncio.TimeoutError:
                    try:
                        for emoji in link_msg.reactions:
                            await link_msg.clear_reaction(emoji)
                    except:
                        pass
    @commands.command(aliases = ["umma","ummma","ummmma","ummmmma","ummmmmma","ummmmmmma","ummmmmmmma","ummmmmmmmma","ummmmmmmmmma"])
    async def kiss(self,ctx,*, name=""):
        if name:
            try:
                user = ctx.message.mentions[0]
            except IndexError:
                user = ctx.guild.get_member_named(name)
            if not user:
                try:
                    user = ctx.guild.get_member(int(name))
                except:
                    pass
            if not user:
                await ctx.send('Argument ERROR! Please tag someone.')
                return
        else:
            await ctx.send('Argument ERROR! Please tag someone.')
            return
        
        kiss = ["https://cdn.weeb.sh/images/r1VWnTuPW.gif","https://cdn.weeb.sh/images/ryoW3T_vW.gif",
                "https://cdn.weeb.sh/images/SJ3dXCKtW.gif","https://cdn.weeb.sh/images/SJSr3TOv-.gif",
                "https://cdn.weeb.sh/images/Skv72TuPW.gif","https://cdn.weeb.sh/images/r1cB3aOwW.gif",
                "https://cdn.weeb.sh/images/BJLP3a_Pb.gif","https://cdn.weeb.sh/images/S1qZksSXG.gif",
                "https://cdn.weeb.sh/images/HJ5khTOP-.gif","https://cdn.weeb.sh/images/B13D2aOwW.gif",
                "https://cdn.weeb.sh/images/S1E1npuvb.gif","https://cdn.weeb.sh/images/S1PCJWASf.gif",
                "https://cdn.weeb.sh/images/SJn43adDb.gif","https://cdn.weeb.sh/images/Bkuk26uvb.gif",
                "https://cdn.weeb.sh/images/HJYghpOP-.gif","https://cdn.weeb.sh/images/rkFSiEedf.gif",
                "https://cdn.weeb.sh/images/BkLQnT_PZ.gif","https://cdn.weeb.sh/images/Skc42pdv-.gif",
                "https://cdn.weeb.sh/images/SJ8I2Tuv-.gif","https://cdn.weeb.sh/images/H1e7nadP-.gif",
                "https://cdn.weeb.sh/images/SkQIn6Ovb.gif","https://cdn.weeb.sh/images/ByVQha_w-.gif",
                "https://cdn.weeb.sh/images/rkv_mRKF-.gif","https://cdn.weeb.sh/images/r1H42advb.gif",
                "https://cdn.weeb.sh/images/B1yv36_PZ.gif","https://cdn.weeb.sh/images/Sy6Ai6ODb.gif",
                "https://cdn.weeb.sh/images/ryFdQRtF-.gif"]
        
        messages = [f"{ctx.author.name} kissed {user.name}!!?",f"Did just {ctx.author.name} kissed {user.name}!!? OwO",f"{ctx.author.name} kissed {user.name}!!? Really?",f"{ctx.author.name} just kissed {user.name}. >//<", f"Awwww {ctx.author.name} kissed {user.name}."]
        gif = random.choice(kiss)
        embed = discord.Embed(color = 0x5865F2)
        embed.set_author(name = random.choice(messages))
        embed.set_image(url = gif)
        await ctx.send(embed = embed)

    @commands.command()
    async def pat(self,ctx,*,name = ""):
        if name:
            try:
                user = ctx.message.mentions[0]
            except IndexError:
                user = ctx.guild.get_member_named(name)
            if not user:
                try:
                    user = ctx.guild.get_member(int(name))
                except:
                    pass
            if not user:
                await ctx.send('Argument ERROR! Please tag someone.')
                return
        else:
            await ctx.send('Argument ERROR! Please tag someone.')
            return

        pat = ["https://cdn.weeb.sh/images/Sk2FyQHpZ.gif","https://cdn.weeb.sh/images/Sk2f7J39G.gif",
               "https://cdn.weeb.sh/images/ryXj1JKDb.gif","https://cdn.weeb.sh/images/ry1tlj2AW.gif",
               "https://cdn.weeb.sh/images/SJS1lyYwW.gif","https://cdn.weeb.sh/images/rkl1xJYDZ.gif",
               "https://cdn.weeb.sh/images/H1s5hx0Bf.gif","https://cdn.weeb.sh/images/SJmW1RKtb.gif",
               "https://cdn.weeb.sh/images/BkJBQlckz.gif","https://cdn.weeb.sh/images/SkksgsnCW.gif",
               "https://cdn.weeb.sh/images/SJva1kFv-.gif","https://cdn.weeb.sh/images/S1ja11KD-.gif",
               "https://cdn.weeb.sh/images/SkVNXac-G.gif","https://cdn.weeb.sh/images/r1Y5L6NCZ.gif",
               "https://cdn.weeb.sh/images/Byd3kktw-.gif","https://cdn.weeb.sh/images/HJGQlJYwb.gif",
               "https://cdn.weeb.sh/images/ryXj1JKDb.gif","https://cdn.weeb.sh/images/HyqTkyFvb.gif",
               "https://cdn.weeb.sh/images/SJLaWWRSG.gif","https://cdn.weeb.sh/images/B1D9J1tvZ.gif",
               "https://cdn.weeb.sh/images/B1TQcTNCZ.gif","https://cdn.weeb.sh/images/HkZqkyFvZ.gif",
               "https://cdn.weeb.sh/images/HyG2kJKD-.gif","https://cdn.weeb.sh/images/rJMskkFvb.gif",
               "https://cdn.weeb.sh/images/Bk4Ry1KD-.gif","https://cdn.weeb.sh/images/HyxG31ktDb.gif",
               "https://cdn.weeb.sh/images/SktIxo20b.gif","https://cdn.weeb.sh/images/rytzGAE0W.gif",
               "https://cdn.weeb.sh/images/rkADh0sqM.gif","https://cdn.weeb.sh/images/rkbblkYvb.gif",
               "https://cdn.weeb.sh/images/rybs1yFDb.gif","https://cdn.weeb.sh/images/HyWlxJFvb.gif",
               "https://cdn.weeb.sh/images/B1FqkJKPW.gif","https://cdn.weeb.sh/images/rkSN7g91M.gif",
               "https://cdn.weeb.sh/images/rkTC896_f.gif","https://cdn.weeb.sh/images/HkJ2VknqG.gif",
               "https://cdn.weeb.sh/images/rkZbJAYKW.gif","https://cdn.weeb.sh/images/rktsca40-.gif",
               "https://cdn.weeb.sh/images/SJmW1RKtb.gif","https://cdn.weeb.sh/images/r180y1Yvb.gif",
               "https://cdn.weeb.sh/images/rkBZkRttW.gif","https://cdn.weeb.sh/images/r12R1kYPZ.gif",
               "https://cdn.weeb.sh/images/B1PnJJYP-.gif","https://cdn.weeb.sh/images/SyFmqkFwW.gif",
               "https://cdn.weeb.sh/images/Sky1x1YwW.gif","https://cdn.weeb.sh/images/BJnD9a4Rb.gif",
               "https://cdn.weeb.sh/images/B1SOzCV0W.gif","https://cdn.weeb.sh/images/r1lVQgcyG.gif",
               "https://cdn.weeb.sh/images/H1jgekFwZ.gif","https://cdn.weeb.sh/images/H1XkAyYNM.gif "]
        
        messages = [f"Awww {ctx.author.name} just pat {user.name}'s head. >.<",f"Adorable >.< {ctx.author.name} just gave {user.name} a head pat.",f"{ctx.author.name} pats {user.name}! So cute! >//<"]
        gif = random.choice(pat)
        embed = discord.Embed(color = 0x5865F2)
        embed.set_author(name = random.choice(messages))
        embed.set_image(url = gif)
        await ctx.send(embed = embed)


    @commands.command()
    async def hug(self,ctx,*,name = ""):
        if name:
            try:
                user = ctx.message.mentions[0]
            except IndexError:
                user = ctx.guild.get_member_named(name)
            if not user:
                try:
                    user = ctx.guild.get_member(int(name))
                except:
                    pass
            if not user:
                await ctx.send('Argument ERROR! Please tag someone.')
                return
        else:
            await ctx.send('Argument ERROR! Please tag someone.')
            return

        hug = ["https://cdn.weeb.sh/images/Sk80wyhqz.gif","https://cdn.discordapp.com/attachments/777124925219536911/831630665749233664/tenor_32.gif",
               "https://cdn.discordapp.com/attachments/777124925219536911/831630757578801222/tenor_30.gif","https://cdn.discordapp.com/attachments/777124925219536911/831630950042959892/tenor_3.gif",
               "https://cdn.discordapp.com/attachments/777124925219536911/831630876981985350/tenor_2.gif","https://cdn.discordapp.com/attachments/777124925219536911/831631027432194058/tenor_4.gif",
               "https://cdn.discordapp.com/attachments/777124925219536911/831631100664741918/tenor_5.gif","https://cdn.discordapp.com/attachments/777124925219536911/831631144167407616/tenor_7.gif",
               "https://cdn.discordapp.com/attachments/777124925219536911/831631245715701801/tenor_8.gif","https://cdn.discordapp.com/attachments/777124925219536911/831631357687496754/tenor_11.gif",
               "https://cdn.discordapp.com/attachments/777124925219536911/831631318004662292/tenor_10.gif","https://cdn.discordapp.com/attachments/777124925219536911/831631343192244254/tenor_9.gif",
               "https://cdn.discordapp.com/attachments/777124925219536911/831631484553003058/tenor_12.gif","https://cdn.discordapp.com/attachments/777124925219536911/831631548574728262/tenor_13.gif",
               "https://cdn.discordapp.com/attachments/777124925219536911/831631571710115840/tenor_14.gif","https://cdn.discordapp.com/attachments/777124925219536911/831631603812794438/tenor_16.gif",
               "https://cdn.discordapp.com/attachments/777124925219536911/831631612416229386/tenor_15.gif","https://cdn.discordapp.com/attachments/777124925219536911/831631631105130556/tenor_17.gif",
               "https://cdn.discordapp.com/attachments/777124925219536911/831631984198418432/tenor_18.gif","https://cdn.discordapp.com/attachments/777124925219536911/831632008069382184/tenor_19.gif",
               "https://cdn.discordapp.com/attachments/777124925219536911/831632090361626654/tenor_20.gif","https://cdn.discordapp.com/attachments/777124925219536911/831632174704492604/tenor_21.gif",
               "https://cdn.discordapp.com/attachments/777124925219536911/831632311102603304/tenor_24.gif","https://cdn.discordapp.com/attachments/777124925219536911/831632407115071568/tenor_25.gif",
               "https://cdn.discordapp.com/attachments/777124925219536911/831632432024780840/tenor_26.gif","https://cdn.discordapp.com/attachments/777124925219536911/831632451742335006/tenor_29.gif",
               "https://cdn.discordapp.com/attachments/777124925219536911/831632595073630298/tenor_30.gif","https://cdn.weeb.sh/images/SJZ-Qy35f.gif",
               "https://cdn.weeb.sh/images/rkN2u_XP-.gif","https://cdn.weeb.sh/images/BkFnJsnA-.gif",
               "https://cdn.weeb.sh/images/rko9O_mwW.gif","https://cdn.weeb.sh/images/SywetdQvZ.gif",
               "https://cdn.weeb.sh/images/rkx1dJ25z.gif","https://cdn.weeb.sh/images/ByPGRkFVz.gif",
               "https://cdn.weeb.sh/images/Hk3ox0tYW.gif","https://cdn.weeb.sh/images/rJnKu_XwZ.gif",
               "https://cdn.weeb.sh/images/ryCG-OatM.gif","https://cdn.weeb.sh/images/HkfgF_QvW.gif",
               "https://cdn.weeb.sh/images/r1G3xCFYZ.gif","https://cdn.weeb.sh/images/rkIK_u7Pb.gif"]

        messages = [f"Awww {ctx.author.name} hugged {user.name}. >.<",f"Cute! >.< {ctx.author.name} just hugged {user.name}.",f"{ctx.author.name} Squeeze harder! >//<", f"AWWWW! {ctx.author.name} {user.name}, you are so cute."]
        gif = random.choice(hug)
        embed = discord.Embed(color = 0x5865F2)
        embed.set_author(name = random.choice(messages))
        embed.set_image(url = gif)
        await ctx.send(embed = embed)

    @commands.command()
    async def lick(self,ctx,*,name = ""):
        if name:
            try:
                user = ctx.message.mentions[0]
            except IndexError:
                user = ctx.guild.get_member_named(name)
            if not user:
                try:
                    user = ctx.guild.get_member(int(name))
                except:
                    pass
            if not user:
                await ctx.send('Argument ERROR! Please tag someone.')
                return
        else:
            await ctx.send('Argument ERROR! Please tag someone.')
            return

        lick = ["https://cdn.discordapp.com/attachments/777124925219536911/831830324392230912/tenor.gif","https://cdn.discordapp.com/attachments/777124925219536911/831830377432612885/tenor_2.gif",
                "https://cdn.discordapp.com/attachments/777124925219536911/831830872054562846/tenor_1.gif","https://cdn.discordapp.com/attachments/777124925219536911/831831446976987156/tenor_3.gif",
                "https://cdn.discordapp.com/attachments/777124925219536911/831831778778939442/tenor_4.gif","https://cdn.discordapp.com/attachments/777124925219536911/831832455174029362/tenor_5.gif",
                "https://cdn.discordapp.com/attachments/777124925219536911/831832802664120330/tenor_6.gif","https://cdn.discordapp.com/attachments/777124925219536911/831833736932884521/tenor_7.gif",
                "https://cdn.discordapp.com/attachments/777124925219536911/831834187208196126/tenor_8.gif","https://cdn.discordapp.com/attachments/777124925219536911/831834746849853440/tenor_9.gif",
                "https://cdn.discordapp.com/attachments/777124925219536911/831834805619654656/tenor_10.gif","https://cdn.discordapp.com/attachments/777124925219536911/831834897881890816/tenor_11.gif",
                "https://cdn.discordapp.com/attachments/777124925219536911/831835781303631892/tenor_13.gif","https://cdn.discordapp.com/attachments/777124925219536911/831835480311726080/tenor_12.gif",
                "https://cdn.discordapp.com/attachments/777124925219536911/831836087843946506/tenor_14.gif","https://cdn.discordapp.com/attachments/777124925219536911/831836444087025694/tenor_15.gif",
                "https://cdn.discordapp.com/attachments/777124925219536911/831837059328245781/tenor_16.gif","https://cdn.discordapp.com/attachments/777124925219536911/831837614461157426/tenor_17.gif",
                "https://cdn.discordapp.com/attachments/777124925219536911/831838684298739722/tenor_18.gif","https://cdn.discordapp.com/attachments/777124925219536911/831838854474104882/tenor_19.gif",
                "https://cdn.discordapp.com/attachments/777124925219536911/831838997252407296/tenor_20.gif","https://cdn.discordapp.com/attachments/777124925219536911/831839608823611392/tenor_22.gif",
                "https://cdn.discordapp.com/attachments/777124925219536911/831839579316289556/tenor_21.gif","https://cdn.weeb.sh/images/rykRHmB6W.gif",
                "https://cdn.weeb.sh/images/ryGpGsnAZ.gif","https://cdn.weeb.sh/images/rkBbBQS6W.gif",
                "https://cdn.weeb.sh/images/Bkxge0uPW.gif","https://cdn.weeb.sh/images/H1EJxR_vZ.gif",
                "https://cdn.weeb.sh/images/BkvTBQHaZ.gif","https://cdn.weeb.sh/images/rJ6hrQr6-.gif",
                "https://cdn.discordapp.com/attachments/777124925219536911/831844451311550494/tenor_23.gif"]

        messages = [f"Awww {ctx.author.name} licked {user.name}. >.<",f"Cute! >.< {ctx.author.name} just licked {user.name} so hard.",f"{ctx.author.name} don't lick too much! >//<", f"AWWWW! {ctx.author.name} {user.name}, stop licking. ><"]
        gif = random.choice(lick)
        embed = discord.Embed(color = 0x5865F2)
        embed.set_author(name = random.choice(messages))
        embed.set_image(url = gif)
        await ctx.send(embed = embed)

    @commands.command(aliases = ["sob"])
    async def cry(self,ctx):
        cry = ["https://cdn.weeb.sh/images/rknUmIXD-.gif","https://cdn.weeb.sh/images/rkpoLqadG.gif",
               "https://cdn.weeb.sh/images/HJIpry35M.gif","https://cdn.weeb.sh/images/r1itBRFTZ.gif",
               "https://cdn.weeb.sh/images/rkoNQ8mP-.gif","https://cdn.weeb.sh/images/BJJkFTN0b.gif",
               "https://cdn.weeb.sh/images/Sk5a01cyf.gif","https://cdn.weeb.sh/images/SkbN7LQv-.gif",
               "https://cdn.weeb.sh/images/H1nGQ8Qw-.gif","https://cdn.weeb.sh/images/ByuM1x5Jz.gif",
               "https://cdn.weeb.sh/images/B1N87IQDZ.gif","https://cdn.weeb.sh/images/Bk_fmL7wZ.gif",
               "https://cdn.weeb.sh/images/HyiGQUmPb.gif","https://cdn.weeb.sh/images/r1WMmLQvW.gif",
               "https://cdn.weeb.sh/images/Hy4QmU7PZ.gif","https://cdn.weeb.sh/images/SJ08mUXwZ.gif",
               "https://cdn.weeb.sh/images/HkxLXIQvb.gif","https://cdn.weeb.sh/images/r1UGQLXvb.gif",
               "https://cdn.weeb.sh/images/rJ5IX8XPZ.gif","https://cdn.weeb.sh/images/rkXImUQDW.gif",
               "https://cdn.weeb.sh/images/ByF7REgdf.gif","https://cdn.weeb.sh/images/ryi8787vW.gif",
               "https://cdn.weeb.sh/images/ryVBX8mw-.gif","https://cdn.weeb.sh/images/BJJPXLQPW.gif",
               "https://cdn.discordapp.com/attachments/777124925219536911/831932064324255794/tenor.gif","https://cdn.discordapp.com/attachments/777124925219536911/831932227906175056/tenor_1.gif",
               "https://cdn.discordapp.com/attachments/777124925219536911/831932511121834004/tenor_2.gif","https://cdn.discordapp.com/attachments/777124925219536911/831932778672422912/tenor_3.gif",
               "https://cdn.discordapp.com/attachments/777124925219536911/831932963230449755/tenor_4.gif","https://cdn.discordapp.com/attachments/777124925219536911/831933101482835998/tenor_5.gif",
               "https://cdn.discordapp.com/attachments/777124925219536911/831933178477936670/tenor_6.gif","https://cdn.discordapp.com/attachments/777124925219536911/831933552571842610/tenor_7.gif",
               "https://cdn.discordapp.com/attachments/777124925219536911/831933884442083379/tenor_8.gif","https://cdn.discordapp.com/attachments/777124925219536911/831933926066356275/tenor_9.gif",
               "https://cdn.discordapp.com/attachments/777124925219536911/831934188142985277/tenor_10.gif","https://cdn.discordapp.com/attachments/777124925219536911/831934212226678856/tenor_11.gif",
               "https://cdn.discordapp.com/attachments/777124925219536911/831934228282998874/tenor_12.gif","https://cdn.discordapp.com/attachments/777124925219536911/831934612678508576/tenor_13.gif",
               "https://cdn.discordapp.com/attachments/777124925219536911/831934618298875934/tenor_14.gif","https://cdn.discordapp.com/attachments/777124925219536911/831934669171196024/tenor_15.gif",
               "https://cdn.discordapp.com/attachments/777124925219536911/831934680034443334/tenor_16.gif","https://cdn.discordapp.com/attachments/777124925219536911/831935024055844914/tenor_17.gif"]

        messages = [f'{ctx.author.name} is crying. :"(', f'{ctx.author.name} needs a warm hug.',f"{ctx.author.name} don't cry. Everything will be alright.",f"{ctx.author.name} is crying. Somebody hug...",f"{ctx.author.name} please don't cry. ;-; I am here."]
        gif = random.choice(cry)
        embed = discord.Embed(color = 0x5865F2)
        embed.set_author(name = random.choice(messages))
        embed.set_image(url = gif)
        await ctx.send(embed = embed)

    @commands.command()
    async def tickle(self,ctx,*,name = ""):
        if name:
            try:
                user = ctx.message.mentions[0]
            except IndexError:
                user = ctx.guild.get_member_named(name)
            if not user:
                try:
                    user = ctx.guild.get_member(int(name))
                except:
                    pass
            if not user:
                await ctx.send('Argument ERROR! Please tag someone.')
                return
        else:
            await ctx.send('Argument ERROR! Please tag someone.')
            return
        
        tickle = ["https://cdn.weeb.sh/images/HyjNLkXiZ.gif","https://cdn.weeb.sh/images/H1p0ByQo-.gif",
                  "https://cdn.weeb.sh/images/rybRByXjZ.gif","https://cdn.weeb.sh/images/rkPzIyQi-.gif",
                  "https://cdn.weeb.sh/images/SyQHUy7oW.gif","https://cdn.discordapp.com/attachments/777124925219536911/831997960623095828/tenor.gif",
                  "https://cdn.discordapp.com/attachments/777124925219536911/831997960614838322/tenor_1.gif","https://cdn.discordapp.com/attachments/777124925219536911/831997921003438090/tenor_2.gif",
                  "https://cdn.discordapp.com/attachments/777124925219536911/831998244586389574/tenor_3.gif","https://cdn.discordapp.com/attachments/777124925219536911/831998277204312104/tenor_4.gif",
                  "https://cdn.discordapp.com/attachments/777124925219536911/831998348814581760/tenor_5.gif"]
        
        messages = [f'{ctx.author.name} is tickling {user.name} ><!',f'{ctx.author.name} is tickling {user.name} ><! Save her!',f'{ctx.author.name} is tickling hard {user.name} :))',f'{user.name} RIP. :))']
        gif = random.choice(tickle)
        embed = discord.Embed(color = 0x5865F2)
        embed.set_author(name = random.choice(messages))
        embed.set_image(url = gif)
        await ctx.send(embed = embed)
    
    @commands.command()
    async def flip(self,ctx):
        embed = discord.Embed(color = 0x5865F2)
        embed.set_author(name = "Flipping......", icon_url = "https://cdn.discordapp.com/emojis/842024350948392990.gif?v=1")
        link_msg = await ctx.send(embed = embed)
        await asyncio.sleep(3)
        win = random.choice(["Heads","Tails"])
        temp = discord.Embed(color = 0x5865F2)
        temp.set_author(name = f"Winner: {win}")
        await link_msg.edit(embed = temp)

    @commands.command()
    async def topic(self,ctx,option = ""):
        starter = ["Tell me about yourself.","Have you done anything exciting lately?",
                   "What made you smile today?","What’s your favorite form of social media?",
                   "What was the last good book you read?","Do you listen to any podcasts? Which is your favorite?",
                   "What do you think is the best show on Netflix right now?","Have you been on any interesting trips lately?",
                   "What do you think has been the best movie of the year so far?","What song do you wish you could put on right now?",
                   "Are you a cat person or a dog person?","Do you think you’re an introvert or an extrovert?",
                   "What’s your strangest hidden talent?","What is something people are always surprised to learn about you?",
                   "Where do you want to be in five years?","What superpower do you wish you could have?",
                   "Where would you go on vacation if you had no budget?","If you could travel back in time, what decade would you choose to live in?",
                   "What’s the last concert you went to?","What is one thing you can’t live without?",
                   "What’s the strangest dream you’ve had recently?","What is your favorite book of all time?",
                   "How many countries have you been to?","Would you rather travel via plane or boat?",
                   "Would you rather be really hot or really cold?","Who is your favorite celebrity couple ever?",
                   "What’s your favorite sport?","What sport do you wish you were really good at?",
                   "How did you spend your last birthday?","Do you believe men and women can ever just be friends?",
                   "What’s one interesting thing about yourself no one really knows?","What’s the best food you’ve had so far?",
                   "What is your biggest regret in life?","Tell me about the most life-changing piece of advice you’ve ever heard.",
                   "When are you the most happy?","Who is the most important person in your life right now?",
                   "What do you wish your phone could do?","Who in your life is the worst at using technology?",
                   "What makes you really certain about that you are not wasting your time and life?","What’s the best / worst thing about your work/school?",
                   "What do you think the world will be like 20 years in the future?","What is something you’ve failed at recently?",
                   "Have you ever played Valorant? Do you like it? If you do then why?","Do you ever sing in the shower?",
                   "What is the worst piece of advice you’ve ever gotten?","",
                   "What’s the most embarrassing thing that’s happened to you recently?","Tell me about the worst pickup line you’ve ever gotten.",
                   "What is your favorite celebrity scandal right now?","What’s the worst thing you’ve ever worn?",
                   "What is the stupidest joke you’ve ever heard?","When was the last time you laughed so hard you cried?",
                   "What’s the best prank you’ve ever played on someone?","Who/What always makes you laugh, even when you’re upset?",
                   "Who is your favorite comedian?","Is a hot dog a sandwich?",
                   "What’s the weirdest thing you loved as a child?","What is something that’s really popular right now that will be ridiculous in five years?",
                   "Describe your perfect weekend.","What’s the biggest risk you’ve ever taken?",
                   "What are your long-term goals?","Tell me three fun facts about yourself.",
                   "If you could make up a school subject, what would it be?","What do you most like about yourself?",
                   "Do you know anyone who is living their life to the fullest?","What does success mean to you?",
                   "What scares you most about your future?","",
                   "If you could be famous, would you want to? Why?","Have you ever lost a friend? Why?",
                   "If you had $100, what would you spend it on?","If you could go anywhere in the world, where would you choose and why?",
                   "What is something you wish you could do everyday?","Have you ever stalked someone on social media?",
                   "Do you prefer texting or talking over voice call? And why?"]
        deep = ["What has been the lowest point of your life?","If you could ask for a miracle, what would it be?",
                "Where do you see yourself in five years?","Do you know anyone who is living their life to the fullest?",
                "What is the biggest risk you’ve ever taken?","What is your idea of the perfect day?",
                "What book had a big influence on you?","Who has been the most influential person in your life and why?",
                "What does success mean to you?","What is the most difficult thing you’ve ever done?",
                "What scares you most about your future?","What keeps you up at night?",
                "What are your long-term goals?","Who is your role model?",
                "What did you want to be when you were a kid?","What is your biggest regret in life?",
                "What are the top three things on your bucket list?","What has been your biggest accomplishment so far?",
                "What is one thing you wish you could do that you know you probably never will?","What are you most afraid of?",
                "What’s the biggest risk you’ve ever taken?","Tell me about the most life-changing piece of advice you’ve ever heard.",
                "When are you the most happy?","What always calms you down when you’re really stressed out and upset?",
                "Who in your life has had the most influence on you?","What’s the hardest thing you’ve ever done?",
                "How have your priorities changed in the last 10 years?","What’s the nicest thing anyone has ever done for you?",
                "Describe your perfect weekend.","What’s the most controversial opinion you have?",
                "If you could change one thing about your personality, what would it be?","What’s the first thing you would do if you won the lottery?",
                "If you could invite one famous person to dinner, who would it be?","Who do you miss the most from your past?",
                "If you could go back in time, what is one situation you would do differently?","Who is the most important person in your life right now?",
                "What did you think you would be doing at this age when you were a kid?","What piece of technology could you live without?",
                "What do you think the world will be like 20 years in the future?","What is something you’ve failed at recently?",
                "What would you change about yourself if you could?","What motivates you to work hard?",
                "What form of public transportation do you prefer? (air, boat, train, bus, car, etc.)","What’s the most spontaneous thing you’ve done lately?",
                "What two radio stations do you listen to in the car the most?","If you could hire someone to help you, would it be with cleaning, cooking, or yard work?",
                "If you could live anywhere, where would it be?","Who is your hero? ",
                "What is your family member’s proudest accomplishment?","What is your favorite book to read?",
                "What are your hobbies?","What is your biggest fear?",
                "If you could choose to do anything for a day, what would it be?","What is the best gift you have been given?",
                "If you could choose to do anything for a day, what would it be?","In the evening, would you rather play a game, visit a relative, watch a movie, or read?",
                "What is your favorite game or sport to watch and play?","Would you rather have one wish granted today or 10 wishes granted 20 years from now?",
                "Would you rather be criticized or be ignored?","Would you rather be so afraid of heights that you can’t go to the second floor of a building or be so afraid of the sun that you can only leave the house on rainy days?",
                "Would you rather be color blind or lose your sense of taste?","Would you rather know when you’re going to die or how you’re going to die?",
                "What makes you think that you are not wasting your life?","Do you have any dream? If you have then what is it? or What are they?"]
        funny = ["Do you ever sing in the shower?","What is the worst piece of advice you’ve ever gotten?",
                 "What’s the most embarrassing thing that’s happened to you recently?","Tell me about the worst pickup line you’ve ever gotten.",
                 "What is your favorite celebrity scandal right now?","What’s the worst thing you’ve ever worn?",
                 "If you could do anything illegal without getting in trouble, what would it be?","What is the stupidest joke you’ve ever heard?",
                 "When was the last time you laughed so hard you cried?","What’s the best prank you’ve ever played on someone?",
                 "What do you think is the funniest movie ever?","What always makes you laugh, even when you’re upset?",
                 "Who is your favorite comedian?","What weird conspiracy theory do you believe?",
                 "Is a hot dog a sandwich?","Which celebrity would play you in a movie about your life?",
                 "What’s the worst trend you’ve ever taken part in?","What’s the weirdest thing you loved as a child?",
                 "Which celebrity would play you in a movie about your life?","Toilet paper, over or under?",
                 "How many chickens would it take to kill an elephant?","Which body part do you wish you could detach and why?",
                 "What used to be considered trashy but now is very classy?","What’s the weirdest thing a guest has done at your house?",
                 "What is the weirdest thing you have seen in someone else’s home?","What would be the worst thing for the government to make illegal?",
                 "If peanut butter wasn’t called peanut butter, what would it be called?","If valorant wasn't called valorant, what would it be called?",
                 "What two totally normal things become really weird if you do them back to back?","What set of items could you buy that would make the cashier the most uncomfortable?",
                 "What would be the creepiest thing you could say while passing a stranger on the street?","What is something that you just recently realized that you are embarrassed you didn’t realize earlier?",
                 "What would be the best-worst name for different types of businesses? (dry cleaners, amusement parks, etc.)","Who do you know that really reminds you of a character in a TV show or movie?",
                 "What would the world be like if it was filled with male and female copies of you?","What are some things that are okay to occasionally do but definitely not okay to do every day?",
                 "If you were arrested with no explanation, what would your friends and family assume you had done?","You’re a mad scientist, what scientific experiment would you run if money and ethics weren’t an issue?",
                 "What are some fun ways to answer everyday questions like “how’s it going” or “what do you do”?","If your five-year-old self suddenly found themselves inhabiting your current body, what would your five-year-old self do first?",
                 "First think of a product. Now, what would be the absolute worst brand name for one of those products?","What movie completely changes its plot when you change one letter in its title? What’s the new movie about?",
                 "If the all the States in the USA were represented by food, what food would each state be represented by?","What is something that is really popular now, but in 5 years everyone will look back on and be embarrassed by?",
                 "If you were transported 400 years into the past with no clothes or anything else, how would you prove that you were from the future?","",
                 "Who is the messiest person you know?","What’s the most useless talent you have?",
                 "What celebrity would you rate as a perfect 10?","What’s a body part that you wouldn’t mind losing?",
                 "What is the dumbest way you’ve been injured?","If you had to change your name, what would your new name be, and why would you choose that name?",
                 "What’s your biggest screw up in the kitchen?","What are some things that sound like compliments but are actually insults?",
                 "When did you screw everything up, but no one ever found out it was you?","What’s something your brain tries to make you do and you have to will yourself not to do it?",
                 "If you could know the absolute and total truth to one question, what question would you ask?","What ridiculous thing has someone tricked you into doing or believing?"]

        options = [starter,funny,deep]

        if not option:
            main = random.choice(options)
            await ctx.send(f"> {random.choice(main)}")

        if option:
            if option.lower() == "starter":
                await ctx.send(f"> {random.choice(random)}")

            if option.lower() == "deep":
                await ctx.send(f"> {random.choice(deep)}")

            if option.lower() == "funny":
                await ctx.send(f"> {random.choice(funny)}")

            if option.lower() != "starter" and option.lower() != "deep" and option.lower() != "funny":
                embed = discord.Embed(color = 0x5865F2, description = "Please provide required arguments.")
                embed.set_author(name = "Argument EROOR",icon_url = self.client.user.avatar_url)
                await ctx.send(embed = embed)

def setup(client):
    client.add_cog(P1(client))