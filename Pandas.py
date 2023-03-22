# -*- coding: utf-8 -*-
"""Programming_assignment_1_10020770631.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hf7K5Z5BudhPgueWIwmos4oRxe5FDSGJ

## **Academic Honesty**
This assignment must be done individually and independently. You must implement the whole assignment by yourself. Academic dishonesty is not tolerated.

## **Requirements**
1. When you work on this assignment, you should make a copy of this notebook in Google Colab. This can be done using the option `File > Save a copy in Drive` in Google Colab. 

2. You should fill in your answer for each task inside the code block right under the task. 

3. You should only insert your code into the designated code blocks, as mentioned above. Other than that, you shouldn't change anything else in the notebook, unless otherwise instructed.

4.  For each code block, you are free to use multiple lines of code. 

5.   Even if you can only partially solve a task, you should include your code in the code block, which allows us to consider partial credit. 

6.   However, your code should not raise errors. Any code raising errors will not get partial credit. 

7.   We will test your code in Google Colab. Make sure your code runs in Google Colab. 

9. For classification, you are expected to use `scikit-learn` (http://scikit-learn.org/stable/supervised_learning.html#supervised-learning). Refer to our Colab on classification for a tutorial of how to use scikit-learn to build classification models. The Colab has been on the Syllabus page and has been explained during lectures [(its link)](https://colab.research.google.com/drive/1Mw-f0UB72GMdw6C6G9legcyxIiDBWjFg). You can also refer to our Colab on Linear Model [(its link)](https://colab.research.google.com/drive/18hXzJCPuLa6bLxIA2BuCD20w8EOnuKM7?usp=sharing).

10. To submit your assignment, download your Colab into a .ipynb file. This can be done using the option `Download > Download .ipynb` in Google Colab.

11. Submit the downloaded .ipynb file into the Programming Assignment 1 entry in Canvas.

## **Task1: Pandas:DataFrame**(40)
"""

import pandas as pd
import numpy as np

# DATA URL SOURCES ###############################
eng_url     = 'https://andybek.com/pandas-eng'
state_url   = 'https://andybek.com/pandas-state'
party_url   = 'https://andybek.com/pandas-party'
liberal_url = 'https://andybek.com/pandas-liberal'
ivies_url   = 'https://andybek.com/pandas-ivies'
##################################################

#Create 5 dataframes(eng,state,party,liberal,ivies) from the 5 csv files uploaded above.
eng = pd.read_csv(eng_url)
state = pd.read_csv(state_url)
party = pd.read_csv(party_url)
liberal = pd.read_csv(liberal_url)
ivies = pd.read_csv(ivies_url)

#Use a function to retreive information on the first 10 rows of your dataframe.
eng.head(10)

state.head(10)

party.head(10)

liberal.head(10)

ivies.head(10)

#Concatenate eng and ivies using the Pandas concatination function and give the shape of your dataframes
pd.concat([eng,ivies]).shape

#Concatenate the 5 dataframes and drop the duplicated values of 'School Name' in your output dataframe called schools
# initialize and empty dataFrame schools
schools = ({})
schools = pd.concat([eng,state,party,liberal,ivies])
schools.drop_duplicates(subset="School Name",keep=False, inplace=True)  # removing all duplicate values.
print(schools)

#Explain what this code implements when run.
schools.loc[0]
print("loc attribute allows indexing and slicing that always references the explicit index.\nThus all rows with index 0 are returned. In this case 4 rows are returned whose index was 0")

#Check if the index in schools is diplicated or not
if schools.index.is_unique:
  print(" Index in school are not duplicate")
else:
  print(" Index in school are duplicate")

# Does coding and running schools.loc[0:2] work? and why?
print("This gives an error because there are multiple rows with same index. So the loc attribute does not know which one to pick")

#Explain how to fix the duplicated index problem.
print("One way is to ignore the index using ignore_index  option.")
print("Another option is to use Multiindex;\nthe result will be a hierarchically indexed series containing the data")

# Create eng2 and ivies2 from eng and ivies where the index is Set to 'School Name'.
eng2 = eng.set_index('School Name')
eng2

ivies2 = ivies.set_index('School Name')
ivies2

#Concatenate eng and ivies by using the multi-index in order to remove the duplicated index issue.
pd.concat([eng,ivies], keys=['eng','ivies'])

#Use the append function to concatenate 'liberal' and 'party' dataframes
liberal.append(party)

regions_url = 'https://andybek.com/pandas-regions'

# Create the dataframe 'regions'  
regions = pd.read_csv(regions_url)
regions

# Merge the 2 dataframes schools and regions
pd.merge(schools,regions)

# Merge schools and regions on the column name 'School Name'
pd.merge(schools,regions,on='School Name')

income_url = 'https://andybek.com/pandas-mid'

#Create Dataframe (mid_career) from the file income 
mid_career = pd.read_csv(income_url)
mid_career

# Merge mid_career and schools on the arguments left_on and right_on and drop the duplicated column. 
pd.merge(mid_career,schools,left_on='school_name',right_on='School Name').drop('School Name', axis=1)

"""Q1: Concatenate the *liberal* and *state* schools into a new dataframe. How many unique school names are there?

"""

#Q1:Code
new_df = ({})
new_df = pd.concat([liberal,state])
new_df["School Name"].unique().size

"""Q2: What is the average median starting salary in the dataframe created above?"""

#Q2:Code
#CONVERT STRING TO INTEGER TO GET THE MEAN VALUE.
def return_integer(value):
  return int(value[1:-4].strip().replace(',',''))
new_df["Starting Median Salary"] = new_df["Starting Median Salary"].apply(return_integer)
new_df["Starting Median Salary"].mean()

"""Q3: Create a short dataframe that shows the top 3 *liberal* arts and *state* schools that produce the highest (mid-career) earning graduates. 

Show the *School Name* and *Mid-Career Median Salary* columns from each dataset, side by side, i.e. <ins>horizontally</ins>.

Nest the column labels within 'Liberal Arts' and 'State' labels.
"""

#Q3:Code
class display(object):
    """Display HTML representation of multiple objects"""
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""
    def __init__(self, *args):
        self.args = args
        
    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                         for a in self.args)
    
    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                           for a in self.args)

top3_liberal = liberal.sort_values(by=['Mid-Career Median Salary'], ascending=False).head(3)
top3_liberal = top3_liberal[['School Name','Mid-Career Median Salary']]
top3_state = state.sort_values(by=['Mid-Career Median Salary'], ascending=False).head(3)
top3_state = top3_state[['School Name','Mid-Career Median Salary']]

display('top3_liberal','top3_state')

# pd.concat([top3_liberal,top3_state],axis=1)
display('top3_liberal','top3_state')

"""Q4: Merge *liberal* arts schools with *regions* and assign the resulting dataframe to *dfm*. What region has the highest number of liberal arts schools?"""

#Q4:Code
dfm = pd.merge(liberal,regions)
dfm.groupby(['Region']).size()

print("Thus we can see that Northeastern has the highest number of libreal arts school")

"""Q5: Set *school_name* as the index of the *mid_career* dataframe. Do the operation inplace."""

#Q5:Code
mid_career.set_index('school_name',inplace=True)

"""Q6: Merge the *dfm* and *mid_career* dataframes. Is the join operation one-to-one?"""

#Q6:Code
pd.merge(dfm,mid_career,right_index=True,left_on='School Name')

print("yes its one to one join function")

"""Create dataframe games"""

#Dataframe creation
games_url = 'https://andybek.com/pandas-games'
games = pd.read_csv(games_url)
games

"""Q7: What are the total sales across all regions?"""

#Q7-Code
games['Global_Sales'].sum()

games.tail(10)

""" Q8: Find the total sales by region for X360 and PS3.

"""

#8-Code
new_games = games[(games["Platform"] == 'X360') | (games["Platform"] == 'PS3')]
new_games = new_games[['Platform','Global_Sales']]
new_games.groupby(['Platform']).sum()

"""Q9: How much does each platform sell across regions, on average?"""

#Q9-Code
new_games2 = games[['EU_Sales','NA_Sales','JP_Sales','Other_Sales','Global_Sales','Platform']]
new_games2.groupby(['Platform']).aggregate('mean')

"""Q10: Create a smaller dataframe from *games*, selecting only the Publisher, Genre, Platform, and NA_Sales columns. Assign this dataframe to the variable *publishers*."""

#Q10-Code
publishers = games[['Publisher','Genre','Platform','NA_Sales']]
publishers

"""Q11: From the *publishers* dataframe, find the top 10 game publishers in North America by total sales."""

#Q11-Code
NA_Sales_df = publishers.groupby("Publisher")["NA_Sales"].sum().reset_index()
NA_Sales_df.sort_values(by = "NA_Sales", ascending=False).head(10)

"""Q12: What is the gaming platform that has attracted the most sales in North America?"""

#Q12:Code
Platform_NA_Sales = publishers.groupby("Platform")["NA_Sales"].sum().reset_index()
Platform_NA_Sales.sort_values(by="NA_Sales", ascending=False).head(1)

#Create Dataframe sat 
sat_url = 'https://andybek.com/pandas-sat'
sat = pd.read_csv(sat_url)
sat

"""Q13: Starting with our main dataframe (*sat*), create a pivot table that summarizes the <ins>total</ins> student enrollment (Student Enrollment) across all 5 boroughs (*Borough*). 

Which boroughs have the highest and lowest high school student bodies?
"""

#Q13
table = pd.pivot_table(sat,values = 'Student Enrollment', index= 'Borough', aggfunc=np.sum)
print(table)
print("highest school students bodies : ",table.idxmax()[0])
print("lowest school students bodies : " , table.idxmin()[0])

"""Q14: Modify the pivot table from the step above to also reflect the average student body size (*Student Enrollment*) across boroughs, in the same pivot table."""

#Q14
pd.pivot_table(sat,values='Student Enrollment', index='Borough', aggfunc={'Student Enrollment':[np.sum,np.mean]})

"""Q15: Create a pivot table of high schools from the Queens borough (*Borough*), containing the SAT section scores (*SAT Section*, *Score*) as columns and the school name (*School Name*) as index. Sort the table in descending order by math section scores."""

#Q15
pivt = sat[(sat['Borough']=='Queens')]
pd.pivot_table(pivt,index='School Name',columns= 'SAT Section', values='Score',aggfunc={'Score':np.sum}).sort_values('Math',ascending=False)

"""## **Task2: Compute the distance between data points (30 points)**

This task uses a set of 10 data points, as given by the code block below. The numerical features of these data points are stored in a pandas `DataFrame` with the name `data`. The features are given the column names `x` and `y`. Their class labels are in a list `class_labels`. For example, the label of data point `[9,2]` is 1.
"""

import pandas as pd

data = pd.DataFrame([[9,2], [2,3], [3,8], [4,4], [5,1], [6,7], [7,9], [8,4], [9,5], [4,7]], columns=["x","y"])
class_labels = [1, 1, 2, 1, 1, 2, 2, 2, 1, 2]

"""**(2.1)** - Write a piece of code to plot the 10-point dataset in a scatter plot using the `matplotlib` library  (https://matplotlib.org/3.5.1/api/_as_gen/matplotlib.pyplot.scatter.html). Points in class 1 should be represented in orange and those in class 2 should be in blue. Furthermore, show a new data point `[5,6]` in red. 

The code block below already provides the first several lines and the last line. Don't change these lines. Instead, fill in your code between them. 

The code on this page can give you some ideas about how to plot points in different colors https://www.codegrepper.com/code-examples/python/how+to+plot+two+different+class+in+different+colour+in+python. 
"""

# Code for 2.1
import matplotlib
import matplotlib.pyplot as plt

plt.figure(figsize=(5, 5))  
plt.xlim(0, 10)
plt.ylim(0, 10)
# DO NOT CHANGE ANYTHING ABOVE. FILL IN YOUR CODE BELOW.

# plot existing points
plt.scatter(data['x'], data['y'], c=class_labels, cmap=matplotlib.colors.ListedColormap(['orange','blue']))
#add new point [5,6] to scatter plot
plt.scatter(5, 6, c=3 ,cmap=matplotlib.colors.ListedColormap(['red']))

# DO NOT CHANGE ANYTHING BELOW. FILL IN YOUR CODE ABOVE.
plt.show()

""" **(2.2)** - Write a piece of code to compute the Euclidean distance between the new data point `[5,6]` and all 10 points in the dataset. Save the distances in a list named `distances`. Note that you are required to implement the Euclidean distance function, and you are not allowed to use any existing implementation of it in any Python library. 
 
The code block below already provides the first line and the last several lines, in order to print out the values in the list `distances`. You are required to fill in your code inside the block. Your output should be essentially the same as the output under the code block below.
"""

`

"""*(2.3)** - Using the 10-point dataset, find the class label for the new data point `[5,6]` by applying the idea of 3-nearest neighbor classification. Save its class label in a variable `class_label`. Judging by the plot from (2.1), you can tell this point should be classified as blue, i.e., class 2. 

Note that you are required to implement 3-nearest neighbor classification for `[5,6]`, instead of calling any existing implementation. 

The code block below already provides the first line and the last line. The first line is to hard-code the content of `distances` so that you can successfully work on this task even if you couldn't manage to accomplish (2.2). The last line prints out the class label of the new data point. Your output should be the same.
"""

# Code for 2.3
distances = [5.657, 4.243, 2.828, 2.236, 5, 1.414, 3.606, 3.606, 4.123, 1.414]
# DO NOT CHANGE ANYTHING ABOVE. FILL IN YOUR CODE BELOW.

print("Looking at the scatter plot we can easily conclide that the new point[5,6] belongs to class 2(blue color) \n")
k_indices = np.argsort(distances)[:3]  #fetch 3 nearest negihbour index
k_labels = [class_labels[x] for x in k_indices]
class_label = max(k_labels)

# DO NOT CHANGE ANYTHING BELOW. FILL IN YOUR CODE ABOVE.
print("class label : ", class_label)

"""## **Task3: Compute the Gini Impurity,entropy and Information Gain (30 points)**

**(3.1)** - Write a piece of code to compute Gini Impurity, Entropy
and Information Gain for each split.

Save the Gini Impurity in a list named `gini`,
save the Information Gain in a list named `Informationgain`. Note that you are required to implement a function for each, and you are not allowed to use any existing implementation of it in any Python library.
The data that is represented in the code block below are factors that affect whether you would go out to play golf or not.
"""

from pandas.core.internals.construction import dataclasses_to_dicts
import pandas as pd

data = pd.DataFrame([['Rainy','Hot','High','False'],['Rainy','Hot','High','True'],['Overcast','Hot','High','False'],['Sunny','Mild','High','False'],['Sunny','Cool','Normal','False'],['Sunny','Cool','Normal','True'],['Overcast','Cool','Normal','True'],['Rainy','Mild','High','False'],['Rainy','Cool','Normal','False'],['Sunny','Mild','Normal','False'],['Rainy','Mild','Normal','True'],['Overcast','Mild','High','True'],['Overcast','Hot','Normal','False'],['Sunny','Mild','High','True']], columns=["Outlook","Temperature","Humidity","Windy"])
class_labels = ['No', 'No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
class_labels
col_list = list(data.columns)

data['class_labels']=class_labels
data['index1'] = data.index
print(data)

# Code for 3.1
import numpy as np 

def gini_impurity(df_column):
  gini_sub_branch = {}
  count_sub_feature = {}
  for sub_feature in df_column.unique():
    yes_count,no_count,total_count = 0,0,0
    for index in range(len(df_column)):
      if df_column[index]==sub_feature:
        total_count+=1
        if class_labels[index]=='Yes':
          yes_count+=1
        else:
          no_count+=1
      
    count_sub_feature[sub_feature] = total_count
    gini_value_of_sub_feature = 1 - (yes_count/(yes_count+no_count))**2 - (no_count/(yes_count+no_count))**2
    gini_sub_branch[sub_feature] = round(gini_value_of_sub_feature,2)

  total_gini_impurity = 0
  for sub_feature in gini_sub_branch:
    total_gini_impurity += (count_sub_feature[sub_feature]/len(df_column))*gini_sub_branch[sub_feature]
  return round(total_gini_impurity,2), gini_sub_branch

def entropy(y):
  y = pd.Series(y)
  a = y.value_counts()/y.shape[0]
  entropy = np.sum(-a*np.log2(a))
  return(entropy)

def information_gain(df_column):
  entropy_sub_branch = {}
  count_sub_feature = {}
  for sub_feature in df_column.unique():
    sub_class_labels = []
    total_count = 0
    for index in range(len(df_column)):
      if df_column[index]==sub_feature:
        total_count+=1
        sub_class_labels.append(class_labels[index])
      
    count_sub_feature[sub_feature] = total_count
    entropy_value_of_sub_feature = entropy(sub_class_labels)
    entropy_sub_branch[sub_feature] = round(entropy_value_of_sub_feature,2)
    
  total_info_impurity = entropy(class_labels)
  for sub_feature in entropy_sub_branch:
    total_info_impurity -= (count_sub_feature[sub_feature]/len(df_column))*entropy_sub_branch[sub_feature]
  return round(total_info_impurity,2),entropy_sub_branch

gini = {}
Informationgain = {}
for col in col_list:
  print("Entropy of ",col, entropy(data[col]))
  value,other_branches = gini_impurity(data[col])
  gini[col] = {value:other_branches}
  value2,other_branches2 = information_gain(data[col])
  Informationgain[col] = {value2:other_branches2}
  print("--------------------")
print("gini",gini)
print("Informationgain",Informationgain)

"""# **(3.2)** -  Perform the First Split using the  Information Gain

1.   List item
2.   List item


"""

# Code for 3.2
# print(Informationgain)
def get_key(keyss):
  return list(keyss.keys())[0]
  
sorted_info_gain_dict = dict(sorted(Informationgain.items(), key = lambda x:get_key(x[1]),reverse=True))
for key,value in sorted_info_gain_dict.items():
  print("First Split Node :",key,sorted_info_gain_dict[key])
  break

"""# **(3.3)** -Perform a further Split using the  Information Gain and complete the Decision Tree"""

# Code for 3.3
def information_gain2(feature):
  # print("feature",feature)
  dict_3 = {}
  for col in col_list:
    # print("col",col)
    entropy_sub_branch = {}
    count_sub_feature = {}
    total_count_2 = 0
    new_class_labels = []
    for sub_feature in data[col].unique():
      # print("-------------------------------------------")
      # print("sub_feature",sub_feature)
      sub_class_labels = []
      total_count = 0
      for i,j in data.iterrows():
        if j['Outlook']==feature and j[col]==sub_feature:
          total_count+=1
          total_count_2+=1
          sub_class_labels.append(class_labels[i])
          new_class_labels.append(class_labels[i])
      
      # print("sub_class_labels",sub_class_labels)
      count_sub_feature[sub_feature] = total_count
      entropy_value_of_sub_feature = entropy(sub_class_labels)
      # print("entropy_value_of_sub_feature",entropy_value_of_sub_feature)
      entropy_sub_branch[sub_feature] = round(entropy_value_of_sub_feature,2)

    total_info_impurity = entropy(new_class_labels)
    for sub_feature in entropy_sub_branch:
      total_info_impurity -= (count_sub_feature[sub_feature]/total_count_2)*entropy_sub_branch[sub_feature]

    dict_3[col] = {round(total_info_impurity,2):entropy_sub_branch}
    # print(dict_3)
  return dict_3

try:
  col_list.remove('Outlook')
except:
  pass

Informationgain = {}
for feature in ['Rainy','Overcast','Sunny']:
  
  Informationgain[feature] = information_gain2(feature)
  # print("--------------------")
print("Informationgain",Informationgain)

""" **(3.4)**

Using the Information Gain , find the class label for the new data point ['Sunny','Hot','High','False']. Save its class label in a variable called class_label. Note that you are required to implement a Decision Tree, instead of calling any existing implementation.

"""

# Code for 3.4
def _predict(a):
  for i in range(len(a)):
    if a[i] == 'Rainy':
      if a[i+2] == 'High':
        return 'Yes'
      else:
        return 'No'
    elif a[i] == 'Sunny':
      if a[i+3] == 'False':
        return 'Yes'
      else:
        return 'No'
    else:
      return 'Yes'

class_label = _predict(['Sunny','Hot','High','False'])
print(class_label)
