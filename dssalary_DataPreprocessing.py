#glass door jobs #predict salary

import pandas as pd

df=pd.read_csv("/Users/arjunrumba/Documents/ds_project/glassdoor_jobs.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#salary parsing
df['Hourly']=df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['Provided Salary']=df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate']!='-1']
salary=df['Salary Estimate'].apply(lambda x : x.split("(")[0])
kd_minus=salary.apply(lambda x: x.replace("K", " ").replace("$"," "))
hour_min=kd_minus.apply(lambda x: x.lower().replace('per hour',' ').replace('employer provided salary:',' '))
df['Min_Salary']=hour_min.apply(lambda x: int(x.split("-")[0]))
df['Max_Salary']=hour_min.apply(lambda x: int(x.split("-")[1]))
df['Avg_Salary']=(df['Min_Salary']+df['Max_Salary'])/2

#company name text only
df['Company_txt']=df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-4], axis =1)

#state field
df['Location_Name']=df['Location'].apply(lambda x: x.split(',')[1])
df['Same_State']=df.apply(lambda x: 1 if x['Location']==x['Headquarters'] else 0, axis=1)

#age of company
df['Age']=df['Founded'].apply(lambda x: x if x<1 else 2020 - x)

#parsing of job description (python, etc.)
#python
df['Python']=df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
print(df['Python'].value_counts())
#statistics
df['Statistics']=df['Job Description'].apply(lambda x: 1 if 'statistics' in x.lower() else 0)
print(df['Statistics'].value_counts())
#web-scrapping
df['Web_Scrapping']=df['Job Description'].apply(lambda x: 1 if 'scrapping' in x.lower() else 0)
print(df['Web_Scrapping'].value_counts())
#tableau
df['Tableau']=df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
print(df['Tableau'].value_counts())
#sql
df['SQL']=df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
print(df['SQL'].value_counts())
#R studio
df['R_Studio']=df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() else 0)
print(df['R_Studio'].value_counts())
#power bi
df['Power_BI']=df['Job Description'].apply(lambda x: 1 if 'power bi' in x.lower() else 0)
print(df['Power_BI'].value_counts())
#aws
df['AWS']=df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
print(df['AWS'].value_counts())
#excel
df['Excel']=df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
print(df['Excel'].value_counts())


df_final=df.drop('Unnamed: 0', axis =1)
print(df_final.columns)

def title_simplifier(title):
	if 'data scientist' in title.lower():
		return 'data scientist'
	elif 'data engineer' in title.lower():
		return 'data engineer'
	elif 'business analyst' in title.lower():
		return 'business analyst'
	elif 'analyst' in title.lower():
		return 'analyst'
	elif 'machine learning' in title.lower():
		return 'machine learning'
	elif 'manager' in title.lower():
		return 'manager'
	elif 'director' in title.lower():
		return 'director'
	elif 'marketing analyst' in title.lower():
		return 'marketing analyst'
	elif 'research analyst' in title.lower():
		return 'research analyst'
	else:
		return 'na'

def seniority(title):
	if 'sr' in title.lower() or 'senior' in title.lower() or 'lead' in title.lower() or 'principal' in title.lower():
	 	return 'senior'
	if 'jr' in title.lower() or 'junior' in title.lower() or 'jr.' in title.lower():
		return 'junior'
	else:
		return 'na'

#job title and seniority
df['Job_Simp']=df['Job Title'].apply(title_simplifier)
print(df.Job_Simp.value_counts())

df['Seniority']=df['Job Title'].apply(seniority)
print(df.Seniority.value_counts())

#Fix state Los Angeles
df['Job_State']=df.Location_Name.apply(lambda x: x.strip() if x.strip().lower()!='los angeles' else 'CA')
print(df.Job_State.value_counts())

#Job description length
df['Desc_Len']=df['Job Description'].apply(lambda x: len(x))
print(df['Desc_Len'])

#Competitor count
df['Num_Comp']=df['Competitors'].apply(lambda x: len(x.split(',')) if x!='-1' else 0)
print(df['Num_Comp'])

#hourly wage to annual
df['Min_Salary']=df.apply(lambda x: x.Min_Salary*2 if x.Hourly==1 else x.Min_Salary, axis=1)
df['Max_Salary']=df.apply(lambda x: x.Max_Salary*2 if x.Hourly==1 else x.Max_Salary, axis=1)
print(df[df.Hourly==1][['Hourly','Min_Salary','Max_Salary']])

final_cleaned=df.drop(['Unnamed: 0'], axis=1)

print(final_cleaned.columns)

final_cleaned.to_csv("ds_salary_cleaned.csv", index=0)
