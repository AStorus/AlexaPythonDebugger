from flask import Flask
from flask_ask import Ask, statement, question, session
import time
import json
import requests
import time
import sys
import pdb
import Directories


directories = Directories.Directories()

app = Flask(__name__)
ask = Ask(app, "/pdb")

@app.route('/')
def homepage():
    return "Python Debugger"

@ask.launch
def start_skill():
    welcome_message = "Starting Python Debugger"
    return statement(welcome_message)


@ask.intent('NumDirectories')
def get_num_directories():
	responseString = "There are "
	numdirs = directories.getNumDirs()
	responseString += numdirs
	responseString += " directories"
	return statement(responseString)

@ask.intent('CurrentDirectory')
def say_current_directory():
	currDir = directories.getCurrDir()
	return statement("The current directory is " + currDir)
		
@ask.intent('ListDirectories')
def list_directories(SortOrder):
	responseStr = "<speak> The sub directories are "
	subdirs = directories.listDirs(SortOrder)
	responseStr += subdirs
	responseStr += "</speak>"
	return statement(responseStr)

@ask.intent('FindFile')
def randomthing(Direction):
    stmt = "Success"
    return statement(stmt)


@ask.session_ended
def session_ended():
    return "Debugger turning off", 200


if __name__ == '__main__':
	app.run(debug=True)
