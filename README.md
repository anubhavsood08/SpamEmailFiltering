# Spam SMS Detection

This repository contains a project for detecting spam SMS messages using a machine learning model. The project includes a Jupyter Notebook for model training and evaluation, a Python script for deploying the model, and a dataset of SMS messages.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Spam SMS detection is a common problem in natural language processing (NLP). This project aims to develop a machine learning model to classify SMS messages as spam or ham (non-spam). The project includes data preprocessing, feature extraction, model training, and evaluation.

## Dataset

The dataset (`spam.csv`) contains SMS messages labeled as spam or ham. The dataset has the following columns:
- `v1`: Indicates whether the message is spam or ham.
- `v2`: The content of the SMS message.
- Additional unnamed columns which may contain noise or irrelevant data.

Here are the first few rows of the dataset:

| v1   | v2                                                                                      | Unnamed: 2 | Unnamed: 3 | Unnamed: 4 |
|------|-----------------------------------------------------------------------------------------|------------|------------|------------|
| ham  | Go until jurong point, crazy.. Available only in bugis n great world la e buffet...     | NaN        | NaN        | NaN        |
| ham  | Ok lar... Joking wif u oni...                                                           | NaN        | NaN        | NaN        |
| spam | Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121... | NaN        | NaN        | NaN        |
| ham  | U dun say so early hor... U c already then say...                                       | NaN        | NaN        | NaN        |
| ham  | Nah I don't think he goes to usf, he lives around here though...                        | NaN        | NaN        | NaN        |

## Project Structure

The repository includes the following files:
- `spam.csv`: The dataset used for training and evaluating the model.
- `spam-sms-detection.ipynb`: A Jupyter Notebook containing the data preprocessing, model training, and evaluation code.
- `app.py`: A Python script for deploying the trained model and making predictions on new SMS messages.

## Installation

To run this project, you need to have Python installed along with the necessary libraries. You can install the required libraries using the following command:

## Usage

### Jupyter Notebook

You can run the Jupyter Notebook to see the entire workflow of data preprocessing, model training, and evaluation.


The notebook covers the following steps:

1. Data loading and encoding detection
2. Data cleaning and preprocessing
3. Exploratory data analysis
4. Feature extraction
5. Model training and evaluation
6. Python script deployment

## Python Script

The `app.py` script can be used to deploy the trained model and make predictions on new SMS messages. Here are the steps to run the script:

1. **Ensure you have the trained model saved:** The script expects a trained model to be loaded. Ensure you have completed the model training and saved the model appropriately in the notebook.

2. **Predict a new SMS message:** The script will provide a function or prompt for entering new SMS messages to predict whether they are spam or ham.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to create a pull request or open an issue.
