[![Beerware License](https://img.shields.io/badge/license-Beerware-yellow)](https://github.com/SlawCzech/url_shortener/blob/master/LICENSE)

# Document classification

Document classification is an application designed for prediction of scanned documents to 21 predefined categories. It is based on two-step pipeline. First, after reading the document, it is assessed by trained Linear Regression model to find out a probability of prediction. If it is above 90%, the predicted class is returned. Otherwise, the object is transferred to Convolutional Neural Network model for final prediction. 

The line of reasoning is shown on the flow diagram below (alas in Polish only).

The prediction accuracy for Linear Regression model is 73% (weighted average) and 93.3% for CNN model. See screenshots below fo details.

The app was designed and written during [HackING](https://challengerocket.com/hacking) 24h hackathon. It was awarded 4th place out of 27 teams. 

To download training data please refer to the [HackING data webpage](https://challengerocket.com/hacking/resources#go-pagecontent).




## Tech Stack

**Server:** Python, Pytesseract, PyTorch, Scikit-Learn, NLTK.


## How to run

Download relevant data and upload to `data` folder.

Run jupyter notebooks as necessary for scan recognition, data cleaning, spell check, ML prediction and/or CNN prediction.

Feel free to reproduce our results.
## App flow diagram

In Polish only.

![Flow diagram](https://github.com/SlawCzech/docs_classification_ML/blob/master/screenshots/flow_diagram.jpeg?raw=true)


## Prediction accuracy

### Logistic Regression model:
![Logistic Regression](https://github.com/SlawCzech/docs_classification_ML/blob/master/screenshots/log_reg_accuracy.png?raw=true)

### CNN model:
![CNN](https://github.com/SlawCzech/docs_classification_ML/blob/master/screenshots/nn_accuracy.png?raw=true)

## Authors

- [@pawelkonior](https://github.com/pawelkonior)
- [@SlawCzech](https://github.com/SlawCzech)
- [@AdiQ777](https://github.com/AdiQ777)
- [@maciejrum](https://github.com/maciejrum)
- [@BartekSzymik](https://github.com/BartekSzymik)


