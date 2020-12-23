Model

The model we used to predict the house prices in the city of Valencia was the Random Forest. In order to test and try different results we followed two different approaches:

    1. Using the whole dataset(the properties which we could determine and exact location and those which we had to use the neighbourhood as location):
        - dummifying "district", "neighbouhood" and "new_construction".
        - note that none of the data was standarize, normalized or log transformed as we're using a random forest.

        Results:

                           Mean Absolute Error: 30009.21
                           Mean Squared Error: 2168290628.98
                           Root Mean Squared Error: 46564.91
                           R2: 0.78
                           Adjusted R2: 0.767
                           Relative Error: 18.2 %


    2. Using only the properties that provide an exact location for the property. Althought we'll be working with a smaller dataset I assume that the information provided for each property is going to be more accurate and more         significant. 
        - dummifying "district", "neighbouhood" and "new_construction".
        - note that none of the data was standarize, normalized or log transformed as we're using a random forest.


            Results:

                           Mean Absolute Error: 31494.38
                           Mean Squared Error: 2186998156.75
                           Root Mean Squared Error: 46765.35
                           R2: 0.80
                           Adjusted R2: 0.794
                           Relative Error: 18.9 %


                       
After training and testing both models, we end up with mixed results. On one side, the first approach shows an smaller MAE, RMSE and relative error than on the second approach. On the other side, our second approach was giving a better R2. Which model should we choose then? Since the difference between both RMSE is no that significant (only by 200 euros), we'll choose the second approach as it'll be a better model to predict the price for standard houses, while it won't be as good when predicting outliers.    
    
                       
                       
                       
        

                           
                           