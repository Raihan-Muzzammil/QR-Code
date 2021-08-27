from flask import Flask
bing = Flask(__name__)
@bing.route('/')
def thing():
    return ("bing bing, bong bong!")
if __name__ == "__main__" :
    bing.run(debug=True,port=8969)