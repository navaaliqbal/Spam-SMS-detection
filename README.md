# Spam-SMS-detection

## Project Description

The Spam SMS Detection project is designed to classify SMS messages as either spam or legitimate (ham) using machine learning techniques. The project leverages Natural Language Processing (NLP) methods for data preprocessing and a Random Forest classifier for model training and prediction.

## Methodology

### Data Cleaning
- **Stopwords Removal**: Commonly used words that do not contribute to the model's predictive power are removed.
- **Stemming**: Reducing words to their base or root form.
- **Tokenization**: Splitting text into individual words or tokens.

### Feature Extraction
- **TF-IDF (Term Frequency-Inverse Document Frequency)**: This technique is used to convert the SMS corpus into numerical feature vectors that represent the importance of each word in the dataset.

### Model Training
- **Random Forest Classifier**: An ensemble learning method used for classification tasks.
- **Grid Search with Cross-Validation**: This technique is employed to find the optimal hyperparameters for the Random Forest classifier, ensuring the best model performance.

## Results
- The model achieves high accuracy and reliability in classifying SMS messages as spam or ham. Detailed results and model evaluation metrics can be found in the `model_training.ipynb` notebook.

