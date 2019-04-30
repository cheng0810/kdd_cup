import pandas as pd
import numpy as np
from os import listdir

#Loading train_queries.csv Data
rawTrainQueriesData = pd.read_csv('C:/Users/jerry/Desktop/CNN/rawData/train_queries.csv',encoding = 'utf8')
#rawTrainQueriesData.replace('', np.nan, inplace=True)
rawTrainQueriesData['pid'].replace(np.nan, 0, inplace=True)
#rawTrainQueriesData.dropna(inplace=True)
rawTrainQueriesData.sort_values(by='sid',inplace=True)
rawTrainQueriesData.reset_index(drop=True, inplace=True)

#Loading train_plans.csv Data
rawTrainPlansData = pd.read_csv('C:/Users/jerry/Desktop/CNN/rawData/train_plans.csv',encoding = 'utf8')
#rawTrainPlansData.replace('', np.nan, inplace=True)
#rawTrainPlansData.dropna(inplace=True)
rawTrainPlansData.sort_values(by='sid',inplace=True)
rawTrainPlansData.reset_index(drop=True, inplace=True)

#Loading profiles.csv Data
rawProfilesData = pd.read_csv('C:/Users/jerry/Desktop/CNN/rawData/profiles.csv',encoding = 'utf8')
#rawProfilesData.replace('', np.nan, inplace=True)
#rawProfilesData.dropna(inplace=True)
pid0={'pid':0,
      'p0':0,'p1':0,'p2':0,'p3':0,'p4':0,'p5':0,'p6':0,'p7':0,'p8':0,'p9':0,
      'p10':0,'p11':0,'p12':0,'p13':0,'p14':0,'p15':0,'p16':0,'p17':0,'p18':0,'p19':0,
      'p20':0,'p21':0,'p22':0,'p23':0,'p24':0,'p25':0,'p26':0,'p27':0,'p28':0,'p29':0,
      'p30':0,'p31':0,'p32':0,'p33':0,'p34':0,'p35':0,'p36':0,'p37':0,'p38':0,'p39':0,
      'p40':0,'p41':0,'p42':0,'p43':0,'p44':0,'p45':0,'p46':0,'p47':0,'p48':0,'p49':0,
      'p50':0,'p51':0,'p52':0,'p53':0,'p54':0,'p55':0,'p56':0,'p57':0,'p58':0,'p59':0,
      'p60':0,'p61':0,'p62':0,'p63':0,'p64':0,'p65':0,
     }
rawProfilesData = rawProfilesData.append(pid0,ignore_index=True)
rawProfilesData.sort_values(by='pid',inplace=True)
rawProfilesData.reset_index(drop=True, inplace=True)

#Loading train_clicks.csv Data
rawTrainClicksData = pd.read_csv('C:/Users/jerry/Desktop/CNN/rawData/train_clicks.csv',encoding = 'utf8')
#rawTrainClicksData.replace('', np.nan, inplace=True)
#rawTrainClicksData.dropna(inplace=True)
rawTrainClicksData.sort_values(by='sid',inplace=True)
rawTrainClicksData.reset_index(drop=True, inplace=True)

#Merge rawTrainData
rawTrainMergeData = rawTrainQueriesData.merge(rawTrainPlansData,left_on='sid',right_on='sid')
rawTrainMergeData = rawTrainMergeData.merge(rawProfilesData,left_on='pid',right_on='pid')
rawTrainMergeData = rawTrainMergeData.merge(rawTrainClicksData,left_on='sid',right_on='sid')
rawTrainMergeData .sort_values(by='sid',inplace=True)
rawTrainMergeData.reset_index(drop=True, inplace=True)
rawTrainMergeData.to_csv('C:/Users/jerry/Desktop/CNN/rawData/train_merges.csv',index=False)


#Loading test_queries.csv Data
rawTestQueriesData = pd.read_csv('C:/Users/jerry/Desktop/CNN/rawData/test_queries.csv',encoding = 'utf8')
#rawTestQueriesData.replace('', np.nan, inplace=True)
rawTestQueriesData['pid'].replace(np.nan, 0, inplace=True)
#rawTestQueriesData.dropna(inplace=True)
rawTestQueriesData.sort_values(by='sid',inplace=True)
rawTestQueriesData.reset_index(drop=True, inplace=True)

#Loading test_plans.csv Data
rawTestPlansData = pd.read_csv('C:/Users/jerry/Desktop/CNN/rawData/test_plans.csv',encoding = 'utf8')
#rawTestPlansData.replace('', np.nan, inplace=True)
#rawTestPlansData.dropna(inplace=True)
rawTestPlansData.sort_values(by='sid',inplace=True)
rawTestPlansData.reset_index(drop=True, inplace=True)

#Merge rawTestData
rawTestMergeData = rawTestQueriesData.merge(rawTestPlansData,left_on='sid',right_on='sid')
rawTestMergeData = rawTestMergeData.merge(rawProfilesData,left_on='pid',right_on='pid')
rawTestMergeData .sort_values(by='sid',inplace=True)
rawTestMergeData.reset_index(drop=True, inplace=True)
rawTestMergeData.to_csv('C:/Users/jerry/Desktop/CNN/rawData/test_merges.csv',index=False)