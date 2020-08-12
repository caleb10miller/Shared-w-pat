import pandas as pd
import matplotlib
matplotlib.get_cachedir()
csv = pd.read_csv('Subset of STAT 201 - Spring 2020 - Project 2 data.txt')
csv['Q29 - Smoked Weed']=csv['Q29 - Smoked Weed'].map({'Yes':1, 'No':0})
print(csv['Q29 - Smoked Weed'])
#csv.plot('Q29 - Smoked Weed', 'Q6 - HS GPA', kind = 'scatter')
stoners = csv.loc[csv['Q29 - Smoked Weed'] == 1]['Q6 - HS GPA'].min()
christians = csv.loc[csv['Q29 - Smoked Weed'] == 0]['Q6 - HS GPA'].min()
if stoners > christians:
    print('Stoners win!')
else:
    print ('Christians win!')
#matplotlib.pyplot.show()