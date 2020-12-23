Introduction

Final project for Ironhack (Oct.2020-Dic.2020). In this repository you'll find a full project for house prediction prices in the city of Valencia. From the adquisition of the data, to the modeling and it's results, this project covers every aspect that a project of this characteristics will have. 

The motivation and main objective of this project is to create an app that will help a user that wants to sell a house in the city of Valencia determine what will be a selling price for the property. In order to get that objective we need to train a model on housing data that will then take the input from a user and will provide the user with a predicted selling price. 

Dataset

One of the main motivations on creating this project was to use as many skills gained during the bootcamp at Ironhack as possible. That's why instead of choosing a location that might have a dataset ready I chose the city of Valencia, so the dataset used in the project it's a dataset gotten using web scraping techniques. 

The web page I decided to scrape due to the very little difficulties regarding data extraction is "pisos.com". I tried to scrape some other webpages with no succes: "Idealista.com", "Zoopla.com", "Fotocasa.com". Choosing "Pisos.com" was easier when aquiring the data, but the quality of the data and the amount of data that I was able to get was not as good as if Idealista or Fotocasa were scraped. 

Data cleaning

As you will encounter if you follow this project, the cleaning of the dataset has been specially demanding as the dataset was coming from web scrapping many values where missing, some others were types and some others weren't providing enough useful information. 

Explanatory Data Analysis

EDA in this project is not very exhaustive as the variables that we go are only a few. 

Modeling

The model I choose to perform this project was a Random Forest Machine Learning algorithm. 

