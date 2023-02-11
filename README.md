<h1 align="center" style="margin-top: 0px;">Australia Rainfall Prediction</h1>


## Brief:
Used Random Forest Classification Machine Learning algorithm to predict whether it will rain tomorrow or not, based on given inputs.

Accuracy score = 88.6%


## Links
### [Australia Rainfall Predictor App Link](https://51shubhamchand-ml-australia-rainfall-predictio-streamlit-k7apmb.streamlit.app/)
### [Australia Rainfall Analysis Dashboard Link](https://public.tableau.com/app/profile/shubham.chand3035/viz/AustraliaRainfallDashboard/RainfallAnalysis?publish=yes)


## Preview of App:
<img width="717" alt="Screenshot 2023-02-05 at 5 15 36 PM" src="https://user-images.githubusercontent.com/36957216/216816812-cf7fb80c-9530-4fcd-8fe8-fce6345d8fa1.png">


## Preview of Dashboard:


## Challenges:
1. Poor quality of data : Data was having a lot of NULL value for multiple columns.

2. Removing NULL values : Two processes were used to remove the NULL values-
  * Populating the missing values with MODE of that column
  * Predicting the missing values using MACHINE LEARNING algorithm (Random Forest Algorithm : For categorical data columns 
  and Linear Regression : For continous data columns)
  
  NOTE : Predicting missing values using ML was used for columns having more than 35% missing values

3. Remove unimportant data : The DATE column was having data in the format of YYYY-MM-DD, so we kept only MM and removed others

4. Final model selection : Tried multiple models mentioned below-
  * Logistict regression
  * K-Neighbour algorithm
  * Decision tree
  * Adaboost classifier
  * XGB classifier
  
  But the best model came out to be Random Forest Algorithm.

5. Predicting value of any new data : This was the most difficult task and took most the effort.
  * Tried to save the model in Pipeline, along with encoding and scaling but it failed.
  Reason being only few columns were supposed to be encoded and some needed to be scaled, but in a Pipeline all the columns are impacted. So, had to leave this process.
  * Tried to do encoding and scaling again in Streamlit.py but it took much effort. Also, for completing again same data had to be unloaded and encoding and scaling codes were supposed to be written down. So, skipped this process.
  * Finally, saved the mapping of encoding and scaling in a csv file and used that to encode and scale any new input data. Then already saved pickel of model was used to predict the data.

6. Compressed Pickle file : The original '.pkl' file was having a size of 160MB, which cannot be uploaded to Github due to limitations of maximum size of any file to be of 25MB only. So, used another library "bz2" to compress the '.pkl' file and later uncompress to use the same.


## Data source:
https://www.kaggle.com/datasets/jsphyg/weather-dataset-rattle-package


## Tools used:
* Google Colab
* Pycharm
* Streamlit


## References:
* https://www.youtube.com/watch?v=uHGOnDdKpK4&list=PLZoTAELRMXVOFnfSwkB_uyr4FT-327noK


## Regards:
**Shubham Chand**
- Github: [@51shubhamchand](https://github.com/51shubhamchand)
- LinkedIn: [@shubham-chand-12100189](https://www.linkedin.com/in/shubham-chand-12100189)
