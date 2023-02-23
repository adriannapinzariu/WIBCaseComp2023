#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


# In[2]:


# Load the data
data = pd.read_csv('influencers_data.csv')


# In[ ]:


# Split the data into training and testing sets
X = data.drop(['engagement'], axis=1)
y = data['engagement']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a random forest regression model
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Evaluate the model on the testing set
y_pred = rf.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# Use the trained model to predict engagement levels of new influencers
new_data = pd.read_csv('new_influencers_data.csv')
new_X = new_data.drop(['engagement'], axis=1)
new_y_pred = rf.predict(new_X)

# Get the top 10 influencers with the highest predicted engagement level
new_data['predicted_engagement'] = new_y_pred
top_influencers = new_data.sort_values(by='predicted_engagement', ascending=False).head(10)
print(top_influencers)

