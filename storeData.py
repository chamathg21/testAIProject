import numpy as np
import pandas as pd
from sklearn import preprocessing

test = pd.read_csv('TestSetVals.csv', header=0)
trainingLabels = pd.read_csv('TrainingSetLabels.csv', header=0)
train = pd.read_csv('TrainingSetVals.csv', header=0)
lab_encode = preprocessing.LabelEncoder()

#####################Cleaning data###################################
test = test.drop(['date_recorded','num_private','recorded_by','region_code','extraction_type','extraction_type_group','payment','quantity_group','source_type','waterpoint_type_group'],axis=1)
train = train.drop(['date_recorded','num_private','recorded_by','region_code','extraction_type','extraction_type_group','payment','quantity_group','source_type','waterpoint_type_group'],axis=1)

#####################Preprocessing###################################

blankStrings = ['funder', 'installer', 'subvillage', 'scheme_name', 'scheme_management']
for header in blankStrings:
    test[header] = test[header].fillna('NAN')

print(test)
headers = ['funder','installer','wpt_name','basin','subvillage','region','lga','ward','public_meeting','scheme_management','scheme_name','permit','extraction_type_class','management','management_group','payment_type','water_quality','quality_group','quantity','source','source_class','waterpoint_type']

for header in headers:
    test[header] = lab_encode.fit_transform(test[header])

print(test)