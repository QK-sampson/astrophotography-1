from flask import Flask, send_from_directory, request

app = Flask(__name__)


@app.route('/')
def capture():
	print(request.args)
	for key,value in request.args.items():
		print(key,value, type(value))
	return "asdf"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')