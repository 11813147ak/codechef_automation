#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[198]:


from selenium import webdriver


# In[238]:


browser1="C:/Users/HP/Desktop/chromedriver.exe"


# In[239]:


browser=webdriver.Chrome(browser1)


# In[240]:


browser.get('https://codechef.com')
usename_element=browser.find_element_by_id('edit-name')
usename_element.send_keys('akarsh123_')
password_element=browser.find_element_by_id('edit-pass')
password_element.send_keys('Akarsh123_')
browser.find_element_by_id('edit-submit').click()



# In[246]:



browser.get('https://www.codechef.com/submit/HS08TEST')
browser.implicitly_wait(10)


# In[248]:



browser.find_element_by_id('edit_area_toggle_checkbox_edit-program').click()


# In[249]:


with open('C:/Users/HP/Desktop/solution.cpp','r') as f:
    code=f.read()


# In[250]:


code


# In[ ]:





# In[251]:


code_element=browser.find_element_by_id('edit-program')
code_element.send_keys(code)


# In[253]:


browser.find_element_by_id('edit-submit-1').click()


# In[ ]:





# In[ ]:





# In[ ]:




