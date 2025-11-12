#!/usr/bin/env python
# coding: utf-8

# In[22]:

#import builtin datasets
from tensorflow.keras.datasets import mnist


# In[23]:


#devide dataset in 
(train_images, train_lables), (test_images, test_lables) = mnist.load_data()


# In[24]:


print("Train Images Lables:", train_images.shape)
print("test Lables        :", test_lables.shape)
print("Train Lables       :", train_lables.shape)


# In[25]:


train_images[1].shape


# In[26]:


train_lables[1]


# In[27]:


import matplotlib.pyplot as plt
digit = train_images[1]
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()


# In[28]:


#Method 1 if we create layers inside of model
from tensorflow import keras
from tensorflow.keras import models, layers
model = keras.Sequential([
    layers.Dense(512, activation='relu'),
    layers.Dense(10, activation='softmax')
])


# In[29]:


#method 2 if we create a blank model then add layers to it
from tensorflow.keras import models, layers
model = keras.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(784,)))
model.add(layers.Dense(10, activation='softmax', input_shape=(786,)))


# In[30]:


model.compile(optimizer='rmsprop', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


# In[31]:


#convert 2d array into 1d array 784 instead of 28x28        #normlize every image pixels size from 0 to 1 (0-1)
#2step work for both train images and test images
train_images = train_images.reshape((60000,784))
train_images = train_images.astype('float32')/255

test_images = test_images.reshape((10000,784))
test_images = test_images.astype('float32')/255


# In[32]:


model.fit(train_images, train_lables, epochs=5, batch_size=128)


# In[48]:


loss, acc =model.evaluate(test_images,test_lables)


# In[37]:
import streamlit as st
st.set_page_config('std_form', layout = 'centered')
st.title('hand digit clasifier')
st.write('Dear student, pleasr input the desired imaged and press submit')


with st.form ('Marksheet_correction_fomr'):
    name =  st.image('please select image')
    inp = name.reshape(1,784)
    submit= st.form_submit_button('Submit')




# In[36]:


test_lables[5]


# In[39]:


model.predict(inp).argmax()
test_digit = test_images[0:10]
prediction = model.predict(test_digit)
for p in prediction:
    print(p.argmax())




test_lables[0:10]


# In[1]:


#confusion metrix and acuracy score khud nikalna hai


# In[ ]:




