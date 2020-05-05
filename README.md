# Sentiment-Analysis
Create an api to take user input statement, clean the dataset, model the data, and classify the statement as positive, negative or neutral.

### Import libraries to process your data

```
import nltk
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
```

### Download twitter dataset for training your model
```nltk.download('twitter_samples')
from nltk.corpus import twitter_samples
```
### Libraries to clean your data
```import re, string
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('stopwords')
```

### Classifier
```
from nltk import classify, NaiveBayesClassifier
```
### Pickle file
We have used a pickle file to store our model, since it conumes a lot of time for cleaning and training our model.
```
import pickle as pickle
pickle.dump(classifier, open('models/final_prediction.pickle', 'wb'))
```

### Chcek results
First, run the Jupyter notebook file.
Second, open "test.py" file and run it in cmd. Server starts running and url is displayed, mostly - http://127.0.0.1:5000.
Open postman - and enter url with POST method: http://127.0.0.1:5000/sentiment
Request body: {
	"data": "I did not like the movie at all. It was so boring!!!"
}

For this classifier, I've used 1500 positive tweets, 1500 negative tweets and 3000 neutral tweets for training. 
The larger your dataset, the more accurate your model is.
