# Email-Spam-Classifier

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##Demo

![image](https://github.com/anmolkumarfromspn/Email-Spam-Classifier-using-Machine-Learning/assets/128449996/15775101-55e8-4897-900f-d5d6ea933548)

![image](https://github.com/anmolkumarfromspn/Email-Spam-Classifier-using-Machine-Learning/assets/128449996/11226571-f20f-4577-823d-57b400821f67)

There is a text box on the project page in which a user can type or paste his email text.
By Clicking on predict model will classify if this mail is spam or not spam.

##Wroking

Used 5000 Emails to train this model
Performed Data Preporocessing - Data Cleaning, EDA, Stemming, removing stopwords using NLTK and NLP

Generated a WordCloud:

![image](https://github.com/anmolkumarfromspn/Email-Spam-Classifier-using-Machine-Learning/assets/128449996/e6f2a185-a0a4-4fb1-a275-6900873540ee)

Used TFIDF Vectorizer to reduce the less frequently used words in spam and ham emails.
Also analyzed most common words used in spam and ham mails.

![image](https://github.com/anmolkumarfromspn/Email-Spam-Classifier-using-Machine-Learning/assets/128449996/e3ecd99c-d4b3-415e-bb78-95530e0e896c)

###Model Building (Naive Bayes Classifier):

I experimented through all possible combinations of CountVectorizer and TFIDF Vectorizer with GaussianNB, MultinomialNB, BernoulliNB.
I get highest precision score in Tfidf Vectorization technique and in Multinomial Naive Bayes. So I built my model with this combination.

Stored model using Pickle module.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Tools used

![image](https://github.com/anmolkumarfromspn/Instahyre-Job-Analytics-Job-Finder/assets/128449996/541d02e0-3d09-4070-825d-f799e6367866)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*Contact Mail: aktwenty5@gmail.com*
*Linkedin: https://bit.ly/45XlMKn*


![image](https://github.com/anmolkumarfromspn/Christmas-Sales-Analysis/assets/128449996/58a5eea1-07ac-459c-bd55-e5748181530b)







