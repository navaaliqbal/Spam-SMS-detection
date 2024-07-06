# Spam SMS Detection

This repository contains a machine learning model to classify SMS messages as spam or ham (non-spam) using Natural Language Processing (NLP) techniques. The model is deployed using a Streamlit web application.

## Deployed Application

The application is deployed at: [Spam SMS Detection](https://spamsms-detection.streamlit.app/)

### Dataset

A public SMS Spam dataset is used, which is not a purely clean dataset. The data consists of :
- **context**: Refers to the SMS content.
- **class**: Indicates whether the SMS is 'spam' or 'ham'.

### Data Preprocessing

Before applying any supervised learning methods, several data cleansing operations were performed to clean the dataset. This was necessary to remove broken and messy contexts and ensure the data was ready for analysis.

### Text Preprocessing

1. **Tokenization**: Messages were tokenized into individual words.
2. **Removing Punctuation**: Punctuation was removed from the messages.
3. **Removing Stop Words**: Common stop words were removed to focus on meaningful words.
4. **Stemming**: Words were reduced to their root form using the Porter Stemmer.

### Feature Extraction

- **TF-IDF Vectorization**: The cleaned and preprocessed text data was converted into numerical features using the TF-IDF Vectorizer.

### Model Building and Fine-Tuning

1. **Random Forest Classifier**: A Random Forest Classifier was used to train the model on the training data.
2. **Hyperparameter Tuning**: The model's hyperparameters were fine-tuned using Grid Search Cross-Validation to find the best parameters.

### Model Saving

- **Pickle**: The trained model and vectorizer were saved using pickle to allow for easy loading and deployment in the Streamlit app.

### Web Application

- **Streamlit**: A web application was built using Streamlit to provide a user-friendly interface for predicting whether an SMS message is spam or ham.
- **Deployment**: The application was deployed to a cloud platform, making it accessible via the provided link.

## How to Use

1. **Clone the repository**.
2. **Install the required dependencies** using `pip install -r requirements.txt`.
3. **Run the Streamlit app** using `streamlit run app.py`.
4. **Navigate to the local URL** provided by Streamlit to use the app.

The web application allows users to input an SMS message and get a prediction of whether it is spam or ham.
