from flask import render_template 
from flask import Flask, request

app = Flask(__name__) 



@app.route('/') 
def hello():
	user_email = request.headers.get('X-Goog-Authenticated-User-Email') # IAP headers
	user_id = request.headers.get('X-Goog-Authenticated-User-ID') # IAP headers 
	return render_template("hello.html", name="KGB", email=user_email, id=user_id) 




if __name__ == "__main__": 
	app.run()