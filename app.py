from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def add_subscriber():
	if request.method == 'POST':
		return "eh."
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



