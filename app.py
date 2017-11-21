from flask import Flask, request
import os, requests


app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def add_subscriber():
	if request.method == 'POST':
		url = "https://api.sendgrid.com/v3/contactdb/recipients"
		header = {'Authorization': "Bearer "+ os.environ['SENDGRID_API_KEY']}
		data = [{"email": request.form.get("email")}]
		response = requests.post(url, headers=header, json=data)
		return response.text
	else:
		return '''
		<div style=\"position:relative; height:90%; width:100%; text-align:center;\">
			<div style=\"position:absolute; top:25%; left:0; right:0;\">
				Nothing to see here.
				<br>
				<br>
				<img src=\"https://media1.giphy.com/media/10RgsuetO4uDkY/giphy.gif\">
			</div>
		</div>"
		'''



