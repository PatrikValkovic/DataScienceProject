# What's new, Twitter?

This file suppose to be instructions about the *What's new, Twitter?* application. This application was developed as a project for the *Introduction to Data Science* subject at the University of Helsinki.

Project was developed by Jan Bína and Patrik Valkovič in winter semester 2018.

Following sections contain detailed instructions how to use and start the application on your own.

## Goal of the application

The *What's new, Twitter?* application is supposed to extract and analyze public tweets on platform *Twitter*. The application is quite limited because for now, it can only access the tweets via free Twitter API, which allows only a few requests per time span. However, with small or none modifications it can be used to analyze more tweets.

When is the application up and running, you can use it to analyze tweets from a specific region or worldwide based on the provided search query. Again, this is just the limitation of Twitter's free API.

The application then shows you lists of keywords, that were in the analyzed tweets with a link to the search engine for more information.

## Installation

The application depends on external tools and libraries. 
For the running of the application, you will need the following tools and libraries:
- *igraph* library, that can be downloaded from http://igraph.org/.
- *Python 3.6* programming environment, that can be downloaded from https://www.python.org/.
- *Pip* package manager, that is usually installed with *Python 3.6*.

Download the source code from Github here: https://github.com/PatrikValkovic/DataScienceProject.

Install dependencies for the project with `pip install -r requiremnts.txt` command.

Get Twitter's and Google's API keys and store them in the `properties.ini` file. A template is provided as `properties.ini.example` file. You can get Google developer account at https://developers.google.com/ and Twitter developer account a https://developer.twitte.com/. Please keep in mind that this process can take some time.

Then run the application with `python3 webapp.py` command. The application then should run locally. You can connect to the application with your browser by visiting webpage http://127.0.0.1:5000/.

## Usage

![](https://i.imgur.com/nMXJNFI.png)

You can put your query into the *Search query* field. Then, you can specify maximum number of tweets to analyze. You can also specify the area, where you want to analyze the tweet. You can change searching area by simply dragging the map and moving to a different location. Alternatively, you can check *Seach worldwide* box to ignore coordinates and search worldwide.

After you finish, click on the *Submit* button to start analyzing the tweets.

The application will return you lists of keywords under the *Submit* button. You can simply click on the list to view more information online. 
