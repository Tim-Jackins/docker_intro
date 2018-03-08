#These are all the packages I use
from flask import Flask
from flask import render_template
from flask import request, send_file, safe_join
from werkzeug import secure_filename
import os

app = Flask(__name__)

#Start the app and go to the download routine
@app.route('/')
@app.route('/file-downloads/')
def file_downloads():
	#load the download page
	return render_template('downloads.html')

#This is triggered when the button is pressed
@app.route('/return-files/')
def return_files():
	filename = 'sample.txt'#Select what the file you want
	filepath = '/mnt'#Select the path (check the -v flag in the run command for mount instructions)
	return send_file(filename_or_fp=safe_join(filepath, filename),\
                            mimetype='application/octet-stream',\#package and send it
                            as_attachment=True,\#This should be True because the API send so
                            attachment_filename=filename)#You can name the file that the client receives something different

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)#Run the flask app on the default internet port
