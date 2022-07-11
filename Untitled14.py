#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot
from sklearn.model_selection import train_test_split 
from sklearn import datasets, linear_model, metrics
from scipy.stats import norm
import statsmodels.api as sm
from flask import Blueprint,jsonify,request
UniRoute=Blueprint("rou ",__name__)
# In[2]:

raw_data = pd.read_excel('Combine Dataset aptitude.xlsx')


# In[3]:


raw_data.head()


# # Preprocessing

# In[4]:


raw_data = raw_data.replace([np.inf,np.NaN],0)


# In[5]:


raw_data.head()


# # Feature Selection

# In[6]:


data = raw_data[['Name Of University','Subject','Close Merit']]


# In[7]:


data = data.loc[(data != 0).any(axis=1)]


# In[8]:


data.tail()


# In[9]:


data.plot()
# pyplot.show()


# In[10]:


data.describe()


# In[11]:


universities = list(data['Name Of University'].unique())


# In[12]:


universities


# In[13]:


subjects = list (data['Subject'].unique())


# In[14]:


subjects


# # Splitting the Data 

# In[15]:


PU = data[data['Name Of University'] == 'University of Punjab']
QU = data[data['Name Of University'] == 'Quaid e Azam University']
ARID = data[data['Name Of University'] == 'Arid Agriculture University']
COMSATS = data[data['Name Of University'] == 'Comsats University']
UOSwabi = data[data['Name Of University'] == 'University of Swabi']
FAST  = data[data['Name Of University'] == 'Fast University']
LUMS  = data[data['Name Of University'] == 'Lums University']
AIR = data [data ['Name Of University'] == 'Air University']
UOS  = data[data['Name Of University'] == 'University of Sargodha']
UOM  = data[data['Name Of University'] == 'University of Malakand']
UOP  = data[data['Name Of University'] == 'University of Peshawar']
GC  = data[data['Name Of University'] == 'GC University Faislabad']
UOL  = data[data['Name Of University'] == 'University of Education Lahore']
HU  = data[data['Name Of University'] == 'Hamdard University']
SU  = data[data['Name Of University'] == 'Superior University']


# In[16]:


PU_subject_wise_data = []
for i in (subjects):
    PU_subject_wise_data.append(PU[PU['Subject'] == i])


# In[17]:


QU_subject_wise_data = []
for i in (subjects):
    QU_subject_wise_data.append(QU[QU['Subject'] == i])


# In[18]:


ARID_subject_wise_data = []
for i in (subjects):
    ARID_subject_wise_data.append(ARID[ARID['Subject'] == i])


# In[19]:


COMSATS_subject_wise_data = []
for i in (subjects):
    COMSATS_subject_wise_data.append(COMSATS[COMSATS['Subject'] == i])


# In[20]:


UOSwabi_subject_wise_data = []
for i in (subjects):
    UOSwabi_subject_wise_data.append(UOSwabi[UOSwabi['Subject'] == i])


# In[21]:


FAST_subject_wise_data = []
for i in (subjects):
    FAST_subject_wise_data.append(FAST[FAST['Subject'] == i])


# In[22]:


LUMS_subject_wise_data = []
for i in (subjects):
    LUMS_subject_wise_data.append(LUMS[LUMS['Subject'] == i])


# In[23]:


AIR_subject_wise_data = []
for i in (subjects):
    AIR_subject_wise_data.append(AIR[AIR['Subject'] == i])


# In[24]:


UOS_subject_wise_data = []
for i in (subjects):
    UOS_subject_wise_data.append(UOS[UOS['Subject'] == i])


# In[25]:


UOM_subject_wise_data = []
for i in (subjects):
    UOM_subject_wise_data.append(UOM[UOM['Subject'] == i])


# In[26]:


UOP_subject_wise_data = []
for i in (subjects):
    UOP_subject_wise_data.append(UOP[UOP['Subject'] == i])


# In[27]:


GC_subject_wise_data = []
for i in (subjects):
    GC_subject_wise_data.append(GC[GC['Subject'] == i])


# In[28]:


UOL_subject_wise_data = []
for i in (subjects):
    UOL_subject_wise_data.append(UOL[UOL['Subject'] == i])


# In[29]:


HU_subject_wise_data = []
for i in (subjects):
    HU_subject_wise_data.append(HU[HU['Subject'] == i])


# In[30]:


SU_subject_wise_data = []
for i in (subjects):
    SU_subject_wise_data.append(SU[SU['Subject'] == i])


# # Predicting the subject wise merit of University of Punjab

# In[31]:


Predicted_merit_of_All_Universities =[]

predicted_merit_of_PU = []

for i in PU_subject_wise_data:
    endog = i['Close Merit']

    # Construct the AR model
    mod = sm.tsa.statespace.SARIMAX(endog, order=(1, 0, 0), trend='c')

    # Estimate the parameters
    res = mod.fit()

    predicted_merit = list(res.forecast(steps=1))
    predicted_merit_of_PU.append(predicted_merit[0])
Predicted_merit_of_All_Universities.append(predicted_merit_of_PU)


# # QU

# In[32]:


predicted_merit_of_QU = []

for i in QU_subject_wise_data:
    endog = i['Close Merit']

    # Construct the AR model
    mod = sm.tsa.statespace.SARIMAX(endog, order=(1, 0, 0), trend='c')

    # Estimate the parameters
    res = mod.fit()

    predicted_merit = list(res.forecast(steps=1))
    predicted_merit_of_QU.append(predicted_merit[0])
Predicted_merit_of_All_Universities.append(predicted_merit_of_QU)


# # ARID

# In[33]:


predicted_merit_of_ARID = []

for i in ARID_subject_wise_data:
    endog = i['Close Merit']

    # Construct the AR model
    mod = sm.tsa.statespace.SARIMAX(endog, order=(1, 0, 0), trend='c')

    # Estimate the parameters
    res = mod.fit()

    predicted_merit = list(res.forecast(steps=1))
    predicted_merit_of_ARID.append(predicted_merit[0])
Predicted_merit_of_All_Universities.append(predicted_merit_of_ARID)


# # Comsats

# In[34]:


predicted_merit_of_COMSATS = []

for i in COMSATS_subject_wise_data:
    endog = i['Close Merit']

    # Construct the AR model
    mod = sm.tsa.statespace.SARIMAX(endog, order=(1, 0, 0), trend='c')

    # Estimate the parameters
    res = mod.fit()

    predicted_merit = list(res.forecast(steps=1))
    predicted_merit_of_COMSATS.append(predicted_merit[0])
Predicted_merit_of_All_Universities.append(predicted_merit_of_COMSATS)


# # UoSwabi

# In[35]:


predicted_merit_of_UOSwabi = []

for i in UOSwabi_subject_wise_data:
    endog = i['Close Merit']

    # Construct the AR model
    mod = sm.tsa.statespace.SARIMAX(endog, order=(1, 0, 0), trend='c')

    # Estimate the parameters
    res = mod.fit()

    predicted_merit = list(res.forecast(steps=1))
    predicted_merit_of_UOSwabi.append(predicted_merit[0])
Predicted_merit_of_All_Universities.append(predicted_merit_of_UOSwabi)


# # FAST

# In[36]:


predicted_merit_of_FAST = []

for i in FAST_subject_wise_data:
    endog = i['Close Merit']

    # Construct the AR model
    mod = sm.tsa.statespace.SARIMAX(endog, order=(1, 0, 0), trend='c')

    # Estimate the parameters
    res = mod.fit()

    predicted_merit = list(res.forecast(steps=1))
    predicted_merit_of_FAST.append(predicted_merit[0])
Predicted_merit_of_All_Universities.append(predicted_merit_of_FAST)


# # LUMS

# In[37]:


predicted_merit_of_LUMS = []

for i in LUMS_subject_wise_data:
    endog = i['Close Merit']

    # Construct the AR model
    mod = sm.tsa.statespace.SARIMAX(endog, order=(1, 0, 0), trend='c')

    # Estimate the parameters
    res = mod.fit()

    predicted_merit = list(res.forecast(steps=1))
    predicted_merit_of_LUMS.append(predicted_merit[0])
Predicted_merit_of_All_Universities.append(predicted_merit_of_LUMS)


# # AIR

# In[38]:


predicted_merit_of_AIR = []

for i in AIR_subject_wise_data:
    endog = i['Close Merit']

    # Construct the AR model
    mod = sm.tsa.statespace.SARIMAX(endog, order=(1, 0, 0), trend='c')

    # Estimate the parameters
    res = mod.fit()

    predicted_merit = list(res.forecast(steps=1))
    predicted_merit_of_AIR.append(predicted_merit[0])
Predicted_merit_of_All_Universities.append(predicted_merit_of_AIR)


# # UOS

# In[39]:


predicted_merit_of_UOS = []

for i in UOS_subject_wise_data:
    endog = i['Close Merit']

    # Construct the AR model
    mod = sm.tsa.statespace.SARIMAX(endog, order=(1, 0, 0), trend='c')

    # Estimate the parameters
    res = mod.fit()

    predicted_merit = list(res.forecast(steps=1))
    predicted_merit_of_UOS.append(predicted_merit[0])
Predicted_merit_of_All_Universities.append(predicted_merit_of_UOS)


# # UOM

# In[40]:


predicted_merit_of_UOM = []

for i in UOM_subject_wise_data:
    endog = i['Close Merit']

    # Construct the AR model
    mod = sm.tsa.statespace.SARIMAX(endog, order=(1, 0, 0), trend='c')

    # Estimate the parameters
    res = mod.fit()

    predicted_merit = list(res.forecast(steps=1))
    predicted_merit_of_UOM.append(predicted_merit[0])
Predicted_merit_of_All_Universities.append(predicted_merit_of_UOM)


# # UOP

# In[41]:


predicted_merit_of_UOP = []

for i in UOP_subject_wise_data:
    endog = i['Close Merit']

    # Construct the AR model
    mod = sm.tsa.statespace.SARIMAX(endog, order=(1, 0, 0), trend='c')

    # Estimate the parameters
    res = mod.fit()

    predicted_merit = list(res.forecast(steps=1))
    predicted_merit_of_UOP.append(predicted_merit[0])
Predicted_merit_of_All_Universities.append(predicted_merit_of_UOP)


# # GC

# In[42]:


predicted_merit_of_GC = []

for i in GC_subject_wise_data:
    endog = i['Close Merit']

    # Construct the AR model
    mod = sm.tsa.statespace.SARIMAX(endog, order=(1, 0, 0), trend='c')

    # Estimate the parameters
    res = mod.fit()

    predicted_merit = list(res.forecast(steps=1))
    predicted_merit_of_GC.append(predicted_merit[0])
Predicted_merit_of_All_Universities.append(predicted_merit_of_GC)


# # UOL

# In[43]:


predicted_merit_of_UOL = []

for i in UOL_subject_wise_data:
    endog = i['Close Merit']

    # Construct the AR model
    mod = sm.tsa.statespace.SARIMAX(endog, order=(1, 0, 0), trend='c')

    # Estimate the parameters
    res = mod.fit()

    predicted_merit = list(res.forecast(steps=1))
    predicted_merit_of_UOL.append(predicted_merit[0])
Predicted_merit_of_All_Universities.append(predicted_merit_of_UOL)


# # HU

# In[44]:


predicted_merit_of_HU = []

for i in HU_subject_wise_data:
    endog = i['Close Merit']

    # Construct the AR model
    mod = sm.tsa.statespace.SARIMAX(endog, order=(1, 0, 0), trend='c')

    # Estimate the parameters
    res = mod.fit()

    predicted_merit = list(res.forecast(steps=1))
    predicted_merit_of_HU.append(predicted_merit[0])
Predicted_merit_of_All_Universities.append(predicted_merit_of_HU)


# # SU

# In[45]:


predicted_merit_of_SU = []

for i in SU_subject_wise_data:
    endog = i['Close Merit']

    # Construct the AR model
    mod = sm.tsa.statespace.SARIMAX(endog, order=(1, 0, 0), trend='c')

    # Estimate the parameters
    res = mod.fit()

    predicted_merit = list(res.forecast(steps=1))
    predicted_merit_of_SU.append(predicted_merit[0])
Predicted_merit_of_All_Universities.append(predicted_merit_of_SU)


# # Calculating the Merit  according to Universities Criteria

# In[59]:


# Fscmarks = int(input("ENTER FSC MARKS"))
# matric = int(input ("ENTER Matric Marks"))
# Testmarks = int(input("Enter Testmarks"))
# Subject = input ("Enter SUBJECT")
@UniRoute.route("/uni",methods=['POST'])
def get_uni():
    Fscmarks = int(request.form['fsc_marks'])
    matric=int(request.form['matic_marks'])
    Testmarks=int(request.form['Score'])
    Subject=request.form['field']
    print(Fscmarks,matric,Testmarks,Subject)

# In[60]:


    Calculated_meritlist_of_All_universities = []
    Calculated_meritlist_of_All_universities.append(((matric/1100*0.30+(Fscmarks/1100*0.30)+(Testmarks/50*0.40))))
    Calculated_meritlist_of_All_universities.append((((Fscmarks/1100*0.70)+(Testmarks/50*0.30))))
    Calculated_meritlist_of_All_universities.append((((Fscmarks/1100*0.50)+(Testmarks/50*0.50))))
    Calculated_meritlist_of_All_universities.append(((matric/1100*0.10+(Fscmarks/1100*0.40)+(Testmarks/50*0.50))))
    Calculated_meritlist_of_All_universities.append((((Fscmarks/1100*0.50)+(Testmarks/50*0.50))))
    Calculated_meritlist_of_All_universities.append((((Fscmarks/1100*0.50)+(Testmarks/50*0.50))))
    Calculated_meritlist_of_All_universities.append((((Fscmarks/1100*0.70)+(Testmarks/50*0.30))))
    Calculated_meritlist_of_All_universities.append((((Fscmarks/1100*0.50)+(Testmarks/50*0.50))))
    Calculated_meritlist_of_All_universities.append(((matric/1100*0.35+(Fscmarks/1100*0.35)+(Testmarks/50*0.43))))
    Calculated_meritlist_of_All_universities.append((((Fscmarks/1100*0.45)+(Testmarks/50*0.55))))
    Calculated_meritlist_of_All_universities.append((((Fscmarks/1100*0.45)+(Testmarks/50*0.55))))
    Calculated_meritlist_of_All_universities.append((((Fscmarks/1100*0.50)+(Testmarks/50*0.50))))
    Calculated_meritlist_of_All_universities.append((((Fscmarks/1100*0.50)+(Testmarks/50*0.50))))
    Calculated_meritlist_of_All_universities.append((((Fscmarks/1100*0.50)+(Testmarks/50*0.50))))
    Calculated_meritlist_of_All_universities.append((((Fscmarks/1100*0.50)+(Testmarks/50*0.50))))


# In[61]:


    Calculated_meritlist_of_All_universities


# In[62]:


    Predicted_merit_of_All_Universities [0]


# In[63]:


    Eligibal_Universities = []
    for i in range(len(universities)):
        for j in range(len(Predicted_merit_of_All_Universities[i])):
           if(Subject == subjects[j]):
               if(Calculated_meritlist_of_All_universities[i] >= Predicted_merit_of_All_Universities[i][j]):
                    Eligibal_Universities.append(universities[i])

    return jsonify(Eligibal_Universities)
# In[64] :




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




