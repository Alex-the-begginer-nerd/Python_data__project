# Introduction
This is a project based on python course of Luke Barousse. All the data used in this project was copiled by him or his team. There key difference is that this project is concentrated solely on Ireland.   

## Goals
1) Create an EDA (Explanatory Data Analysis) for data analyst jobs in Ireland.
2) Find out the most frequent skill appearing in jop postings.
3) Analyse the flactuations of demanded skills throughout the year.
4) Analyse salary distributions for data jobs.
5) Determine the most optimal skill for data analyst. 
## Tools I Used 
1) Python
2) VS Code
3) Git and Github
4) Anaconda
# The Analysis
## 1. EDA
#### At first I decided to reserch the most popular locations for data jobs. Here is my approach: 
[1_EDA_intro.ipynb](/Data_Analyst_project/1_EDA_intro.ipynb)
``` python 
df_plot = df_Irl_DA['job_location'].value_counts().head(10).to_frame()
sns.barplot(data=df_plot, x='count',y='job_location', hue='count', palette='dark:b_r', legend=False)
sns.set_theme(style='ticks')
sns.set_style("ticks")
sns.despine()
plt.ylabel(' ')
plt.xlabel('Number of Jobs')
plt.title('Counts of Job Locations for Data Analyst in Ireland')

```
![image_1](/Data_Analyst_project/output.png)

#### Afterwards I decided to check how many of job postings have health insurance offered, allowed to work from home, required a degree: 
```python
pie_dict = {
    'job_health_insurance' : 'Health insurance offered',
    'job_work_from_home' :  'Work from home',
    'job_no_degree_mention' : 'Degree required'
}
fig, ax = plt.subplots(1,3)
fig.set_size_inches((12,5))
for i, (column,title) in enumerate(pie_dict.items()):
    labels = df_Irl_DA[column].value_counts().index.astype(str)
    ax[i].pie(df_Irl_DA[column].value_counts(), autopct='%1.1f%%' , startangle=90,labels=labels)
    ax[i].set_title(title)
```
[1_EDA_intro.ipynb](/Data_Analyst_project/2_skill_count.ipynb)

Here are the resulting graphs.
![image_2](/Data_Analyst_project/output1.png)

#### At last I researched the most popular Irish data companies.
```python
df_plot = df_Irl_DA['company_name'].value_counts().head(10).to_frame()
sns.barplot(data=df_plot, x='count',y='company_name', hue='count', palette='dark:b_r', legend=False)
sns.set_theme(style='ticks')
sns.set_style("ticks")
sns.despine()
plt.ylabel(' ')
plt.xlabel('Number of Jobs')
plt.title('Counts of Company Appearing in Job Postings')
```
[1_EDA_intro.ipynb](Data_Analyst_project\1_EDA_intro.ipynb)
![image_3](/Data_Analyst_project/output2.png)

## 2. Frequent skills
Here is my aproach:

```python
fig, ax = plt.subplots(len(job_titles),1)
sns.set_theme(style='ticks')
for i, job_title in enumerate(job_titles):
    df_plot = df_skills_percent[df_skills_percent['job_title_short'] == job_title].head(5)  
    sns.barplot(data = df_plot, x='skill_perc',y='job_skills',ax=ax[i], hue='job_skills', palette='dark:b')
    ax[i].legend().set_visible(False)
    ax[i].set_ylabel('')
    ax[i].set_title(job_title)
    ax[i].set_xlim(0,60)
    ax[i].set_xlabel('')
    sns.set_style('ticks')
    for n, v in enumerate(df_plot['skill_perc']):
        ax[i].text(v,n,f'{v:.0f}%')

    if i != len(job_titles) - 1:
        ax[i].set_xticks([]) 

fig.suptitle('Percentage of Skill Occuring in Job Postings', fontsize=15)
plt.tight_layout(h_pad=0.5)
fig.set_size_inches(6,7)
plt.show()
```

![image_4](/Data_Analyst_project/output3.png)

## 3. Trending skills
Here is my aproach:

```python

df_DA_Irl_exp['Month'] = pd.to_datetime(df_DA_Irl_exp['job_posted_date']).dt.strftime('%B')
df_pivot = df_DA_Irl_exp.pivot_table(columns='job_skills',index='Month',aggfunc='size',fill_value=0)
df_pivot.reset_index(inplace=True)
df_pivot['month_no'] = pd.to_datetime(df_pivot['Month'],format='%B').dt.month
df_pivot = df_pivot.sort_values(by='month_no', ascending= True)
df_pivot.set_index('Month', inplace= True)
df_pivot = df_pivot.drop(columns='month_no')
df_pivot.loc['counts']  = df_pivot.sum()
df_pivot = df_pivot[df_pivot.loc['counts'].sort_values(ascending= False).index]
df_pivot = df_pivot.drop(index='counts')
df_pivot = df_pivot.div(jobs_total['count']/100, axis=0)
df_pivot = df_pivot.iloc[:, :5]
sns.lineplot(data=df_pivot, dashes= False, palette= 'tab10')
plt.rcParams['figure.figsize'] = (12,6)
sns.set_theme(style='ticks')
plt.ylabel('Likelihood in Job Postings')
plt.xlabel('2023')
plt.title('Trending top skills for Data Analyst in Ireland')
plt.legend().remove()
sns.despine()
ax = plt.gca()
from matplotlib.ticker import PercentFormatter 
ax.yaxis.set_major_formatter(PercentFormatter(decimals=0))
for i in range(5):
    plt.text(2,df_pivot.iloc[3,i], df_pivot.columns[i])
plt.show()
```

![](/Data_Analyst_project/output4.png)

## 4. Salary analisis 
The goal of this section was to find out salary year distributions among data jobs. Here is my approach:
```python
sns.boxplot(data=df_Irl_top6, x='salary_year_avg', y='job_title_short', palette='dark:g',order=job_order)
x = plt.FuncFormatter(lambda y, pos: f'${int(y/1000)}K')
plt.gca().xaxis.set_major_formatter(x)
sns.set_theme(style='ticks')
plt.xlabel('USD')
plt.ylabel('')
plt.title('Salary Distributions in Ireland')
```
[4_salary_analysis](/Data_Analyst_project/4_salary_analisis.ipynb)

![](/Data_Analyst_project/output6.png)

## 5. Optimal skills for data analutics
Here is my approach:
```python
from adjustText import adjust_text
sns.scatterplot(
    data=df_plot,
    x = 'skill_perc',
    y = 'median_salary',
    hue='tech'
)
sns.set_theme(style='ticks')
sns.despine()
x = plt.FuncFormatter(lambda x, pos: f'{int(x)}%')
plt.gca().xaxis.set_major_formatter(x)
y = plt.FuncFormatter(lambda y, pos: f'${int(y/1000)}K')
plt.gca().yaxis.set_major_formatter(y)
plt.xlabel('Likelyhood of Skill Appearing in Job Posting')
plt.ylabel('Associated Median Salary')
plt.title('Optimal Skills for Data Analyst in Ireland')
texts = []
for i, txt in enumerate(df_DA_exp.index):
    texts.append(plt.text(df_DA_exp['skill_perc'].iloc[i], df_DA_exp['median_salary'].iloc[i],  txt))
    plt.tight_layout()
```

![](/Data_Analyst_project/output7.png)

# Conclusions
### 1. EDA
- The majority of jobs are situated in Dublin.
- Health insurance was offered in all postings.  (Most likely due to inssuficient data)
- Option of working from home was present in a minority of postings, only about 7%.
- Degree was offered in most job postings about 56%. 

- The largest companies were the folloing:
1) Morgan McKinly
2) UntitledHealth Group  
3) Kolle Rebbe
### 2. Frequent skills
- SQL is an essential tool for all **Data Scientists**, **Engineers** and **Analyst**.
- Python is also incredibly popular, yet not so needed for **Data Analysts**.
### 3. Trending skills
- Skills flactuate greatly throughout the year, but **Sql** remained the most popular no matter what.
- It's hard to draw other conclusions presumably due to insufficient data.
### 4. Salary Analysis
- Highest paying data jobs
1) Machine Learning Engineer
2) Senior Data Scientist 
3) Data Engineer/Senior Data engineer.
### 5. Optimal skills for Data Analyst
- Programming skills group is the most relevant for Data Analysts.
- SQL proves to be one of the most important skills (if not the most important one) not only amoung programming group but also about every group.
- Tableu holds the second place.