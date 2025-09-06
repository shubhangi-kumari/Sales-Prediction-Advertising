#!/usr/bin/env python
# coding: utf-8

# # Sales Prediction

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# # Load dataset

# In[3]:


import pandas as pd
data = pd.read_csv("advertising.csv")
print(data.head())


# In[7]:


data = data.drop(columns=["Unnamed: 0"])


# In[8]:


print("Missing values:\n", data.isnull().sum())


# In[9]:


print(data.describe())


# In[10]:


plt.figure(figsize=(6,4))
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


# In[11]:


X = data[["TV", "Radio", "Newspaper"]] # independent variables
y = data["Sales"] # target variable


# Split into train & test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[12]:


model = LinearRegression()
model.fit(X_train, y_train)


# In[13]:


y_pred = model.predict(X_test)


# In[15]:


import numpy as np
print("R² Score:", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))


# In[16]:


coefficients = pd.DataFrame({
'Feature': X.columns,
'Coefficient': model.coef_
})
print(coefficients)


# # Plot feature importance

# In[17]:


plt.figure(figsize=(6,4))
sns.barplot(x='Feature', y='Coefficient', data=coefficients)
plt.title("Impact of Advertising Spend on Sales")
plt.show()


# # Actionable insights

# In[18]:


print("\nActionable Insights:")
print("1. Higher coefficient means stronger impact on sales.")
print("2. TV and Radio usually have higher coefficients, showing more impact than Newspaper.")
print("3. Businesses should prioritize ad spend on TV and Radio for better sales outcomes.")
print("4. Diminishing returns: keep in mind that increasing spend does not always linearly increase sales.")


# In[ ]:




