# Datascience Salary Prediction: Overview

This project predicts salary of a data scientist. This project is redoing of the project by Ken Jee, PlayingNumbers/ds_salary_proj. I would like to thank Ken Jee for his contribution in data science learning. His Youtube videos and the contents have really helped the beginners like me to do a data science project. I followed his video and learned many data analysis techniques and prediction modules. His Data Science Project from Scratch is informative and in case of me, motivated me to build a project.  

# Code and Resources Used

* Python Version: 3.7
* Packages: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
* Ken Jee's youtube video link (Data Science Project from Scratch): https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t 

I have uploaded scraped data in csv format.

# Data Preprocessing 

This .py file shows how data cleaning is done. The parsing of numeric data out of salary is done. The hourly wages were separated from salary columnn. I made columns for employer provided salary and hourly wages. The rows without salary were removed. The rating was parsed out of company text. A new column for company state is created. A column for headquarters is created. The founded date is converted into age of company. This gives how old is company. I made columns for if different skills were listed in the job description. I added few other new skills. They are Python, R, Excel, AWS, Tableau, Power BI, Statistics and Web Scraping. 
The columns for simplified job title and Seniority and description length are created. 

# Exploratory Data Analysis

The shape of distribution of the variables Rating, Avg_Salary and Age are plotted. This is to check if they are normally distributed. I plotted boxplots on different variables to check outliers, median and ranges. Heatmap is plotted to know how all the variables are correlated to each other and to the target variable i.e salary. The categorical variables are analyzed by plotting barplots. This helps in analyzing groups under a variable. Some pivot tables are created to understand summary of relationship to the target variable. 

# Model Building

The relevent independent variables are selected and  transformed the categorical variables into dummy variables. The data is splitted into training set and test set with a test size of 20%.

Three different models are used; Multiple Linear Regression, LASSO Regression and Random Forest. The models are evaluated using one of the evaluation metrics that is Mean Absolute Error. MAE is easy to interpret and outliers aren’t particularly bad in for this type of model. This is the easiest of the metrics to understand, since it's just the average error.

The Random Forest model performs better (MAE = 11.11) than other models on the test and validation sets.

* Linear Regression : MAE = 822877862.1200092
* LASSO Regression : MAE = 23.40219396588572
* Random Forest : MAE = 11.115277777777775
