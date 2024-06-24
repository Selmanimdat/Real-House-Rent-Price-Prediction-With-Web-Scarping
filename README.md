# Real House Rent Price Prediction With Web Scarping

This repository contains a project for performing regression analysis with data obtained from web scraping. The project includes data cleaning, model training, and a Streamlit app for model prediction.

## Project Structure

Regression with Web Scraping/<br>
├── Data cleaning.ipynb # Jupyter notebook for data cleaning <br>
├── Regression_.ipynb # Jupyter notebook for regression analysis<br>
├── WEB scarping.ipynb # Jupyter notebook for web scraping<br>
├── best_et_model.pkl # Trained Extra Trees model<br>
├── clean_data.pickle # Cleaned data in pickle format<br>
├── rent_houses.csv # Dataset<br>
└── app.py # Streamlit application script

## Requirements

To run the notebooks and the Streamlit app, you need to have the following packages installed:

- Python 3.8+
- pandas
- numpy
- scikit-learn
- pycaret
- streamlit

You can install the necessary packages using pip:

pip install pandas numpy scikit-learn pycaret matplotlib seaborn streamlit

# Usage

## Web Scraping
Open the WEB scarping.ipynb notebook and run the cells to scrape data from the web. The scraped data will be saved as rent_houses.csv.

## Data Cleaning
Open the Data cleaning.ipynb notebook and run the cells to clean the data. The cleaned data will be saved in clean_data.pickle.

## Regression Analysis
Open the Regression_.ipynb notebook and run the cells to perform regression analysis. The trained model will be saved as best_et_model.pkl.

## Streamlit Application
To run the Streamlit application, navigate to the Streamlit directory and execute the following command:

## Contributing
If you wish to contribute to this project, please fork the repository and create a pull request with your changes.

##License
This project is licensed under the MIT License. See the LICENSE file for more details.
