import numpy as np
import pandas
test = pandas.read_csv('TestSetVals.csv', header=0)
trainingLabels = pandas.read_csv('TrainingSetLabels.csv', header=0)
train = pandas.read_csv('TrainingSetVals.csv', header=0)
print(test)

#####################Cleaning data###################################
test = test.drop(['date_recorded','num_private','recorded_by','region_code','extraction_type','extraction_type_group','payment','quantity_group','source_type','waterpoint_type_group'],axis=1)
train = train.drop(['date_recorded','num_private','recorded_by','region_code','extraction_type','extraction_type_group','payment','quantity_group','source_type','waterpoint_type_group'],axis=1)
#print(train)

#####################Preprocessing###################################
headers = ['funder','installer','wpt_name','basin','subvillage','region','lga','ward','public_meeting','scheme_management','scheme_name','permit','extraction_type_class','management','management_group','payment_type','water_quality','quality_group','quantity','source','source_class','waterpoint_type']
