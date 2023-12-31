# Email-Spam-Classifier

## Introduction

In today's modern digital landscape, the relentless influx of email spam has become a pervasive issue, demanding innovative solutions. This project, building an 'Email Spam Classifier' using Machine Learning, addresses this challenge by leveraging cutting-edge machine learning techniques. This project's core objective is to develop a highly accurate spam filter capable of distinguishing genuine emails from spam messages. By training our machine learning model on extensive datasets, we have crafted a robust system that promises to enhance email communication by automatically filtering out unwanted and potentially harmful content, ultimately streamlining the email experience and bolstering online security.

## Project Objective

The primary objective of this email spam classifier machine learning project is to develop an efficient and accurate model capable of automatically classifying incoming emails as either "spam" or "not spam" (ham). By leveraging machine learning algorithms and a diverse dataset of labeled emails, the project aims to create a robust classifier that can effectively filter out unwanted and potentially harmful spam messages, thereby enhancing the user's email experience and security. Additionally, the project aims to explore various feature engineering techniques and model architectures to achieve the highest possible classification accuracy and minimize false positives, ensuring that legitimate emails are not mistakenly marked as spam. Ultimately, the project's success will be measured by its ability to significantly reduce the influx of spam emails in a user's inbox while maintaining a high level of precision and recall in classification.

## Data Description

In the dataset there are only two columns. One contains the email/sms text and other one contains the "ham" or "spam" tag denoting if the text is spam or not a spam.
Aim is to train a model on this data and create a ML model that will take text as an input to classify that input is a "Spam" or "Not Spam".

![image](https://github.com/anmolkumarfromspn/Email-Spam-Classifier-using-Machine-Learning/assets/128449996/3ea55fed-e350-4680-bf8b-d249be078eeb)

## Data Cleaning & Preprocessing

Performed several necessary data cleaning steps in python using string functions with the help of Pandas library
![image](https://github.com/anmolkumarfromspn/Email-Spam-Classifier-using-Machine-Learning/assets/128449996/730966a6-6eba-4aff-83b1-c9ff7fa659b3)

Performed data Preprocessing to prepare data for model training and development
![image](https://github.com/anmolkumarfromspn/Email-Spam-Classifier-using-Machine-Learning/assets/128449996/9764c8e0-2a2a-4791-b834-c7f9ca9cd3a3)

## EDA

Perfomed a brief Data Analysis as there is not much to explore in the dataset.
![image](https://github.com/anmolkumarfromspn/Email-Spam-Classifier-using-Machine-Learning/assets/128449996/730f2f1c-de31-472a-8955-2ef00eed3da7)

Segregating emails based on text length: -
![image](https://github.com/anmolkumarfromspn/Email-Spam-Classifier-using-Machine-Learning/assets/128449996/393269f1-e618-4cd2-b3c7-ca10dcea32c6)

### Wordcloud

![image](https://github.com/anmolkumarfromspn/Email-Spam-Classifier-using-Machine-Learning/assets/128449996/a8c36bc6-8618-4f94-b51b-62888c227fa4)

![download](https://github.com/anmolkumarfromspn/Email-Spam-Classifier-using-Machine-Learning/assets/128449996/a8c9ef61-e40a-4296-bf21-3fb3966513d1)

### Top 30 words in Ham and Spam Messages

![image](https://github.com/anmolkumarfromspn/Email-Spam-Classifier-using-Machine-Learning/assets/128449996/c8166216-7c7b-487e-8dc1-97defe841b94)

![download](https://github.com/anmolkumarfromspn/Email-Spam-Classifier-using-Machine-Learning/assets/128449996/4abc21fe-a620-4ecd-927e-112e6a20931b)

## Choosing best ML Model

Tried Naive Bayes Classifier - GaussianNB, MultinomialNB, BernoulliNB and chose one with the highest precision score for this model 
and for converting text to vectors checked for Bag of words (count vectorizer) and tfidf vectorizer techniques and chose one with the highest precision_score.

![image](https://github.com/anmolkumarfromspn/Email-Spam-Classifier-using-Machine-Learning/assets/128449996/f6e59bb3-c793-49ad-94e4-f7554f2ae99f)

### Evaluation Metrics

I get highest precision score in Tfidf Vectorization technique and in Multinomial Naive Bayes. I will build my model with this combination.
![WhatsApp Image 2023-09-21 at 21 23 57](https://github.com/anmolkumarfromspn/Email-Spam-Classifier-using-Machine-Learning/assets/128449996/e1db6ab9-fccb-4ee0-890c-bd897121296f)

## Email Spam Classifier Demo

![image](https://github.com/anmolkumarfromspn/Email-Spam-Classifier-using-Machine-Learning/assets/128449996/15775101-55e8-4897-900f-d5d6ea933548)
There is a text box on the project page in which a user can type or paste his email text.

![image](https://github.com/anmolkumarfromspn/Email-Spam-Classifier-using-Machine-Learning/assets/128449996/11226571-f20f-4577-823d-57b400821f67)
By Clicking on predict model will classify if this mail is spam or not spam.

## Future Scope

The email spam classifier machine learning project opens up several avenues for future development and enhancement. Firstly, there is a potential for continuous improvement in model performance through the acquisition of more extensive and diverse email datasets, including new types of spam and evolving email threats. Additionally, incorporating natural language processing techniques and deep learning architectures can further enhance the model's ability to detect subtle nuances in spam emails. Integration with real-time email systems, such as email clients and servers, could make the classifier more practical for end-users. Moreover, exploring user-specific customization options, such as allowing users to define their own spam criteria, can enhance the user experience. Lastly, research into cross-platform compatibility and mobile integration can extend the reach of the spam classifier to a wider audience, ensuring email security across various devices and email platforms. In essence, the future scope of this project involves ongoing refinement and expansion to adapt to the evolving landscape of email spam and user needs.

## Limitations

1. Limited Training Data: This is a small-scale project which suffer from a lack of sufficient training data. This can lead to overfitting, where the model performs well on the training data but poorly on new, unseen data.
2. Generalization: A small-scale project may struggle with generalization to different types of spam emails or emails with varying formats and languages. So this model may not perform well on emails that differ significantly from the training data.
3. Computational Resources: Complex machine learning models require substantial computational resources for training and inference. In a small-scale project, user may be limited by the computational power available, which can restrict the complexity of models you can use.
4. Evolving Spam Techniques: Spam email techniques are constantly evolving. So this model may become less effective over time as spammers develop new tactics that this model hasn't seen during training.
5. User Feedback and Adaptation: In real-world applications, user feedback is crucial for improving spam classifiers. This project does not have access to user feedback data to adapt and enhance the model.

## Challenges

1. Gathering high number of records of spam and ham email samples was a challenging task.
2. Training model on different combinations of count vectorizer and TFIDF Vectorizer with all Naive Bayes models and choosing best model with highest accuracy score was a complex task in this project's training phase.
3. Building a strong frontend to project the model working with a user friendly interface and great user experience was also another great challenge.

## Key Learnings

Machine Learning Expertise: Gained a deeper understanding of machine learning algorithms, including supervised learning, feature engineering, model selection, and evaluation metrics. This project likely exposed me to various techniques for text data preprocessing and feature extraction specific to email content.

Data Handling Skills: Dealing with email data often involves data cleaning, preprocessing, and dealing with class imbalance. I have honed my skills in data wrangling, which is a crucial aspect of any machine learning project.

Model Evaluation: I have learned how to properly evaluate the performance of machine learning models, especially in the context of binary classification tasks. Metrics like accuracy, precision, recall, and F1-score are familiar to me.

Domain Knowledge: I have acquired domain-specific knowledge related to email spam. Understanding the characteristics of spam emails and the evolving techniques used by spammers can be valuable in other cybersecurity-related projects.

Practical Application: This project likely provided me with hands-on experience in deploying machine learning models for real-world use cases, such as email filtering. Understanding how to integrate my model into existing systems or applications is a valuable skill.

Problem-Solving Skills: I have encountered various challenges throughout the project, from data quality issues to model tuning. These experiences have improved my problem-solving skills and my ability to troubleshoot issues.

Project Management: Managing a machine learning project involves planning, data collection, modeling, evaluation, and potentially deployment. I have gained experience in project management and time management.

Iterative Development: I have learned the importance of iteration in machine learning projects. Models often require fine-tuning and refinement, and my project have taught me the value of continuous improvement.

Communication: Explaining my project and its results, both to technical and non-technical stakeholders, is a crucial skill. I have improved my ability to communicate complex technical concepts in a clear and understandable manner.

Ethical Considerations: Dealing with email data involves privacy and ethical considerations. I have a better understanding of the importance of data privacy and the ethical implications of machine learning projects.

## Tools used

![image](https://github.com/anmolkumarfromspn/Instahyre-Job-Analytics-Job-Finder/assets/128449996/541d02e0-3d09-4070-825d-f799e6367866)

## Conclusion

This project has been a testament to the power of machine learning in addressing real-world problems and has provided us with a solid foundation for future endeavors in the field of data science and artificial intelligence. It serves as a reminder that the pursuit of knowledge and innovation in the realm of technology is an ongoing journey, and we are better equipped to navigate it thanks to the insights gained from this project.

*Contact Mail: aktwenty5@gmail.com*

*Linkedin: https://bit.ly/45XlMKn*






