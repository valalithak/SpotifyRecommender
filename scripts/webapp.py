from flask import Flask, redirect, url_for ,render_template,request
import sys
app = Flask(__name__)
import os
import pickle
import numpy as np 
import pandas as pd

@app.route('/',methods=["GET","POST"])
def hello_name():

	if request.method == "POST":
		req = request.form
		print(type(req['song']))
		song_string = req['song']
		
		cmd = "python3 final_script.py "+ '"'+str(song_string)+'"'
		print("command ",cmd)
		os.system(str(cmd))
		f = open('output.txt','r')
		lines = f.readlines()
		print(type(lines))
		return render_template('webui.html', song = lines)

	return render_template('webui.html')

if __name__ == '__main__':
   app.run(port=5555, debug = True, threaded = True)