**This readme.md contains information on Codeup Data Science, Noether cohort, Project 1 : Classification (January 2023).**


_Project Goals :
1. To examine the Telco Churn database and, using visualisations in Tableau and statistical tests in the Python programming language.

2. To determine which factor or factors lead to customer churn.


_Initial Hypotheses : 
1. Customer age (Senior Citizens vs non-Senior Citizens) has an influence on churn rate (COUNTPLOT 5).
>>> Based on the chi-squared test, there does appear to be a relationship between senior citizen customers and churn rate.

2. Customer purchase of tech_support has an influence on churn rate (COUNTPLOT 1).
>>>  Based on the chi-squared test, there does appear to be a relationship between customer purchase of tech support and churn rate.

3. The internet_service_type (ie, DSL, Fiber optic, no internet service) has an influence on churn rate (COUNTPLOT 7).

4. Having paperless billing has an influence on churn rate (COUNTPLOT 3).
>>>  Based on the chi-squared test, there does appear to be a relationship between customer use of paperless billing and churn rate.

_Data Dictionary :
1. Tenure : Customer time with Telco company in months.

2. DF : Dataframe, here referring to the Telco dataset.

3. Target variable : The aspect of the data against which all other aspects will be evaluated. Here, it's 'churn'.

4. Churn : Customer churn, or, a yes (1) / no (0) representation of whether the customer has left the company.


_The Process :
1. Obtain and explore initial, tidied Telco data to examine numbers in the four hypotheses categories. Do this using simple Python coding.

2. Analyse the tidied data based on customer age, customer purchase of security add-ons, customer choice of internet service type, and customer purchase of phone service compared with and to customer purchase of internet service. (These are, also, the four hypotheses to be examined in essaying to determine customer churn rates.)

3. Model the data using comparative visualisations in Tableau.

4. Apply statistical modelling in Python to select data to determine mathematical probability as compared with visual indications.

_Exploration Summary :
1. After graphing the four hypotheses and using statistical testing on three of the hypotheses, it appears that there is an initial relationship between customer churn and the test variables, notably that churn is influence by being a senior citizen, or, separately, by the purchase of tech support, or, separately, by use of paperless billing.


--

compared with = similarities and differences
compared to = likening to  

--

For further exploration : If customer purchase of all security add-ons (online_security, online_backup, device_protection, tech_support) has an influence in churn rate.

For further modelling : Use scatter plots instead of bar plots to graph more than two variables at a time.

