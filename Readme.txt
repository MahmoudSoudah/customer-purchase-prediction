🎓 Project Title:

Customer Purchase Prediction using Machine Learning



📌 Project Description:

This project uses Machine Learning to predict whether a customer will purchase a product based on their age and estimated salary.



📊 Dataset:

The dataset contains:
	•	Age (customer age)
	•	EstimatedSalary (customer income)
	•	Purchased (0 = Not Buy, 1 = Buy)


🤖 Model Used:

Logistic Regression

This is a classification algorithm used to predict binary outcomes (Yes/No).



📐 Mathematical Model:

The model uses the sigmoid function:

\sigma(z) = \frac{1}{1 + e^{-z}}

Where:
	•	z = β0 + β1(Age) + β2(Salary)



🧹 Steps Performed:
	1.	Load dataset using Pandas
	2.	Data cleaning (remove missing values & duplicates)
	3.	Split data into training and testing sets
	4.	Train Logistic Regression model
	5.	Test model performance
	6.	Evaluate accuracy



📊 Evaluation Metrics:
	•	Accuracy Score
	•	Confusion Matrix
	•	Classification Report



🎯 Results:

The model predicts whether a customer will buy or not with good accuracy based on training data.



🧠 Conclusion:

Logistic Regression is an effective method for binary classification problems such as customer purchase prediction.