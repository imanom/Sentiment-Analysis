import nltk, flask
import pickle as pickle
from flask import request
nltk.download('wordnet')
from sklearn.feature_extraction.text import TfidfVectorizer
app = flask.Flask(__name__)
app.config["DEBUG"] = True


def combine():
	tokenizer = nltk.tokenize.TreebankWordTokenizer()
	data= request.json['data'].strip()
	tokens = tokenizer.tokenize(data)
	prediction = model.classify(dict([token, True] for token in tokens))
	
	return prediction



@app.route('/sentiment', methods=['POST'])
def home():
	if not request.json or not 'data' in request.json:
		abort(400)
	return(combine())

	
if __name__ == '__main__':
	modelfile = 'models/final_prediction.pickle'
	model = pickle.load(open(modelfile, 'rb'))
	app.run()
	
