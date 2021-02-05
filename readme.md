# Glassdoor Data Science Jobs Salary Prediction: Overview
* Created a tool that estimates the salary of data scientist (MAE ~ $11K). This can help data scientist to be able to negotiate about their salary.
* Scrapped over 1000 job advertisements from glassdoor.com using Python and Selenium.
* Engineered features from each job description to quantify the value each company put on various skills such as python, excel, aws, and spark.
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.
* Built a client facing API using flask. 

# Web Scraping
I used Selenium to scrape over 1000 data scientist job advetrisement from glassdoor.com. For each job, I obtained the following:
* Job title
* Salary Estimate
* Job Description
* Rating
* Company
* Location
* Company Headquarters
* Company Size
* Company Founded Date
* Type of Ownership
* Industry
* Sector
* Revenue
* Competitors

# Data Cleaning and Feature Engineering
As data should be in a proper format to be able to use for prediction model, I need to clean it.  The following changes has been applied to the data and following variables are created:
* Numeric data is parsed out of Salary Estimate
* New columns are made for employers provided salary and hourly wages.
* Company ratings are parsed out of company text
* New column is built for company state
* Founded date of the company is transformed to the company age
* New columns are made for if the following skills were listed in the job description:
  * Python
  * R
  * AWS
  * Excel
  * Spark
* New columns are made for title of the job (whether it is data scientist, data analyst, ML engineer, etc) and seniority.
* New column are made for the length of job description

# Model Building
To build prediction models, I transformed categorical features to dummy variables. I have also split the data into training set (80%) and test set (20%).
I built three different models and evaluated them using Mean Absolute Error (MAE) as this metric is easy to interpret.
The models that are used are as follows:
+ **Linear regression** - This is the baseline model
+ **Lasso regression** - As the data is sparse because of dummy variables obtained from encoding categorical features, I this linear regression with l1-norm penalty can address this sparsity. 
+ **Random forest** - Again, due to the sparsity in the data this could be a good model. Further, random forest can capture the nonlinearity in the data. 

# Perfomance of the models
Random forest outperforms two other models on the validation and test set. 

+ **Random forest**: MAE = 10.55
+ **Lasso regression**: MAE = 18.63 
+ **Linear regression**: MAE = 47.55

# Productionization

In this step, I built a flask API endpoint that was hosted on a local webserver. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.



