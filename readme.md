**This readme.md contains information on Codeup Data Science, Noether cohort, Project 1 : Classification (January 2023).**

_Title : 
Analysing Customer Churn At Telco
_Author :
Magdalena Rahn



_Project Description :
1. Telco, a phone and internet service provider to general consumers, has been experiencing a high rate of customer loss, or, churn. This project seeks to determine factors contributing to the high rate of churn, and provide suggestions to overcome this customer loss.

2. The future of Telco rests on its ability to maintain and grow its customer base. Such a high rate of churn as is presently being experienced not only decreases company revenue, it also decreases employee, customer and public image confidence.




_Project Goals :
1. To examine the Telco Churn database and, using visualisations (charts) and statistical tests in the Python programming language.

2. To determine which factor or factors lead to customer churn.



_Initial Questions :
1. Does customer age have an influence on churn rate ?

2. Do customers with tech support churn more or less than customers without tech support ?

3. Do customers without internet, with DSL or with fiber optic internet churn more or less than customers with a different internet service ?

4. Do customers with paperless billing churn more or less than customers without paperless billing ?




_Initial Hypotheses : 
1. Customer age (Senior Citizens vs non-Senior Citizens) has an influence on churn rate (COUNTPLOT 1).
>>> Based on the chi-squared test, there does appear to be a relationship between senior citizen customers and churn rate.

2. Customer purchase of tech_support has an influence on churn rate (COUNTPLOT 3).
>>>  Based on the chi-squared test, there does appear to be a relationship between customer purchase of tech support and churn rate.

3. The internet_service_type (ie, DSL, Fiber optic, no internet service) has an influence on churn rate (COUNTPLOT 4).
>>> No statistical test was run on this hypothesis.

4. Having paperless billing has an influence on churn rate (COUNTPLOT 2).
>>>  Based on the chi-squared test, there does appear to be a relationship between customer use of paperless billing and churn rate.




_Data Dictionary :
1. Tenure : Customer time with Telco company in months.

2. DF : Dataframe, here referring to the Telco dataset.

3. Target variable : The aspect of the data against which all other aspects will be evaluated. Here, it's 'churn'.

4. Churn : Customer churn, or, a yes (1) / no (0) representation of whether the customer has left the company.

5. TN, FP, FN, TP : True negative, false positive, false negative, true positive. Use to describe the data in confusion matrices.



_The Process / Project Plan :
1. Obtain and explore initial, tidied Telco data to examine numbers in the four hypotheses categories. Do this using simple Python coding.

2. Analyse the tidied data based on customer age, customer purchase of security add-ons, customer choice of internet service type, and customer purchase of phone service compared with and to customer purchase of internet service. (These are, also, the four hypotheses to be examined in essaying to determine customer churn rates.)

3. Model the data using comparative visualisations in Python (Seaborn and MatPlotLib).

4. Apply statistical modelling in Python to select data to determine mathematical probability as compared with visual indications.

5. Provide suggestions and next steps.



_Exploration Summary :
1. After graphing the four hypotheses and using statistical testing on three of the hypotheses, it appears that there is an initial relationship between customer churn and the test variables, notably that churn is influence by being a senior citizen, or, separately, by the purchase of tech support, or, separately, by use of paperless billing.

2. General takeaways are that the variables so far analysed (paperless billing, tech support, being a senior citizen) do have an influence on increased customer churn rates that lead rates.

3. Going forward, modelling will be done on these four variables, compared with the baseline of no-churn. The modelling seeks to 


***
_For further exploration : If customer purchase of all security add-ons (online_security, online_backup, device_protection, tech_support) has an influence in churn rate.

_For further modelling : Use scatter plots instead of bar plots to graph more than two variables at a time.
***


_Steps To Reproduce :

1. Assure the presence of a Python environment on your computer.

1. Import :
        - Python libraries pandas, numpy, matplotlib, seaborn and scipy, 
        - The Telco database from https://www.kaggle.com/datasets/yeanzc/telco-customer-churn-ibm-dataset and 
            save the file locally, 
        - Pre-existing or self-created data 'acquire' and 'prepare' modules,

2. Tidy the data.

3. Explore using charts, statistical evaluation and modelling.

4. Evaluate, analyse and form conclusions and recommendations.

5. Create a .csv file of the final evaluated data and predictions, consisting of customer ID, probability of not churning and prediction of remaining a customer.