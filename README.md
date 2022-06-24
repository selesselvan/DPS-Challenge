# DPS Challenge

This repository contains my submission to DPS challenge. I will try to explain what I have done in this readme. 

The data that we are assigned is a publicly available dataset from Munich. This data contains the number of accidents for specific categories per month. 

I have tried to incorporate standard machine learning pipeline for dealing with the given challenge. This pipeline includes the following steps 
- EDA
- Data pre-processing
- Feature selection (skipped, as it was already given in the problem statement)
- Model selection 
- Hyperparameter Tuning
- Model training

In addition to this, I also tested a hypothesis of mine. As the given challenge is concentrated on the alcohol-based accidents, I wanted to test, whether the number of accidents increases during the winter period, where alcohol consumption is supposed to increase due to the cold weather. In order to test this hypothesis, I utiziled Augmennted Dickey-Fuller testing for stationarity of the data. This test assumes a null-hypothesis where the data is not stationary, which essentially means that the data is likely to contain seasonality. In my testing, I discovered that the given dataset might contain seasonal effect as I failed to reject the null hypothesis of the aforementioned test.

However, in building the model, tried to explore the data first. This revealed a couple of properties of the data, e.g. there are 84 NaN values on the target variable (WERT). Furthermore, I also discovered the presence of 'Summe' in the MONAT field. In order to pre-process the data, I had to fix this issues. So, EDA helped me in designing the pre-processing of the dataset. I did not use any specialized libraries for data pre-processing; typical pandas operations were sufficient for this purpose. 

As I mentioned before, the important features for the dataset was given in the challenge, so I did not had to utilize methods like chi-square test for determining the important features. Rather, I focused on Model Selection so that I can develop a better solution. 

To perform model selection, I utilized a library named PyCaret. This library is capable of fitting the data to a variety of algorithms, which can be sorted according to our preferred evalution metric. For this challenge, I resorted to Mean Absolute Error (MAE), which utilizes l1-norm. In my experiment, I realized LightGBM outperformed all the other models. So, I decided to use this algorithm for my prediction. 

To build the model, at first, I truncated the future data, i.e. data greater than 2020. This data (ground truth) was eventually used to calculate the generalization error of my final model. To arrive to this model, I decided to utilize Nested Cross Validation, since I have a very small data and I do not wish to overfit my model by leaking the data during hyperparamter tuning. 

The tuned hyperparameter provided me a model that had a MAE of 8.732374065957297 on the ground truth.

After this, I used RESTful framework provided by Flask to serve the model I created. This was then deployed to Heroku and a public URL was exposed for accessing the model. 

Finally, to access the netlify web address of DPS Challenge, I created a script on simple javascript where I used hotpTotpGenerator and then I used POSTMAN to send the POST request of Mission 3. I have also attached the textual version of the sent request in post.txt file. 

Thank you for providing me this opportunity to participate on this challenge. It was a really exhilaring experience for me.