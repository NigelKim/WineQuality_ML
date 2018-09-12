Machine Learning (cse517a) Example Application Project
======================================================

Machine Learning Spring 2018

Team: Kimcheese

Members:

Seunghwan “Nigel” Kim	431659		seunghwan.kim@wustl.edu

Andy Dohoon Kim		    435168		dohoon.kim@wustl.edu

Annie Chaehong Lee		444166		annie.lee@wustl.edu

Jaesang Ha			      419887		

Ryun Han			        429091		r.han@wustl.edu

GitHub: https://github.com/NigelKim/cse517project 



Motivation
----------
Coming from a country with the highest alcohol consumption rate, we decided as a whole to experiment and analyze the wine dataset imported from UCI Machine Learning Repository (http://archive.ics.uci.edu/ml/datasets/Wine+Quality).

Dataset
-------
The dataset is separated into white and red dataset, and includes approximately 6500 data points with the following 12 features:

1.	fixed acidity 
2.	volatile acidity 
3.	citric acid 
4.	residual sugar 
5.	chlorides 
6.	free sulfur dioxide 	7.	total sulfur dioxide 
8.	density 
9.	pH 
10.	sulfates 
11.	alcohol 
12.	quality (score between 0 and 10)

The dataset’s outputs—quality scores—are centered around the mean of 5 and does not include values outside of range [3,8]. We suspect this is because sommeliers are more inclined to give scores within the middle range rather than scoring them the extremes. 

Goals and application
--------------------- 
With the dataset, we proposed to find a model that can reliably predict wine’s quality solely from its chemical components. With a best performing algorithm, we can further develop an app that many wine consumers including chefs, restaurant owners, and hotel managers can use to select their choice of wine and evaluate through just taking a picture of a label.

Throughout the semester, we explored total of 8 different models of the following:

1.	Logistic Regression
2.	AdaBoost
3.	Decision Tree
4.	Random Forest	5.	Gaussian Process
6.	Kernel SVM
7.	DNN regressor

### Please look at MLSP18_FinalReport.pdf at this repository for a full final report on the project. ###
