from flask import render_template 
from flask import Flask, request

app = Flask(__name__) 

# Disable caching 
@app.after_request
def set_response_headers(response): 
	response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
	response.headers['Pragma'] = 'no-cache'
	response.headers['Expires'] = '0'
	return response


@app.route('/') 
def hello():
	user_email = requests.headers.get('X-Goog-Authenticated-User-Email') # IAP headers
	user_id = requests.headers.get('X-Goog-Authenticated-User-ID') # IAP headers 
	return render_template("hello.html", name="KGB", email=user_email, id=user_id) 




if __name__ == "__main__": 
	app.run()