'''
Remove stop words from a text file.
Tested on Win7 and Linux Mint 19.1.
'''
import os
import requests
import operator
import re
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
#from stop_words import stops
from collections import Counter
import nltk
from nltk.corpus import stopwords
from flask import send_file, send_from_directory, safe_join, abort

application = Flask(__name__)
#application.config.from_object(os.environ['application_SETTINGS'])
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(application)

#from models import Result


@application.route('/', methods=['GET', 'POST'])
def index():
# Get nltk stopword list into a set.
	stop_words = set(stopwords.words('english'))
	 
	# Open and read in a text file.
	txt_file = open("book1.txt",encoding="utf8")
	txt_line = txt_file.read()
	txt_words = txt_line.split()
	 
	# stopwords found counter.
	sw_found = 0
	 
	# If each word checked is not in stopwords list,
	# then append word to a new text file.
	
	for check_word in txt_words:
		if not check_word.lower() in stop_words:
			# Not found on stopword list, so append.
			appendFile = open('stopwords-removed.txt','a')
			appendFile.write(" "+check_word)
			appendFile.close()
		else:
			# It's on the stopword list
			sw_found +=1
			print(check_word)
	 
	print(sw_found,"stop words found and removed")
	print("Saved as 'stopwords-removed.txt' ")

	return render_template('index.html', sw_found=sw_found)
	
@application.route('/new', methods=['GET', 'POST'])
def download_file():
	path = "./static/stopwords-removed.txt"
	return send_file(path, attachment_filename=True, mimetype='txt')
#	return send_file(io.BytesIO(obj.logo.read()),
 #                attachment_filename='./static/stopwords-removed.txt',
  #               mimetype='txt')
  



if __name__ == '__main__':
    application.run()