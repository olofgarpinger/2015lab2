# You tell Python that you want to use a library with the import statement.
import requests


# Get the HU Wikipedia page
req = requests.get("https://en.wikipedia.org/wiki/Harvard_University")
req
type(req)

# dir can be used to list all properties of an object
dir(req)

page = req.text
page

from bs4 import BeautifulSoup

soup = BeautifulSoup(page, 'html.parser')
soup

type(page)
type(soup)

print soup.prettify()

soup.title
"title" in dir(soup)

soup.p
len(soup.find_all("p"))

soup.table["class"]

[t["class"] for t in soup.find_all("table") if t.get("class")]

my_list = []
for t in soup.find_all("table"):
    if t.get("class"):
        my_list.append(t["class"])
my_list

table_html = str(soup.find("table", "wikitable"))
from IPython.core.display import HTML
HTML(table_html)

aa = soup.find_all("table", "wikitable")
rows = [row for row in aa[2].find_all("tr")]
rows

rem_nl = lambda s: s.replace("\n", " ")

def power(x, y):
    return x**y
power(2, 3)



def print_greeting():
    print "Hello!"

print_greeting()

def get_multiple(x, y = 1):
    return x*y
print "With x and y: ", get_multiple(10, 2)
print "With x only: ", get_multiple(10, 1)

def print_special_greeting(name, leaving = False, condition = "nice"):
    print "Hi", name
    print "How are you doing in this", condition, "day?"
    if leaving:
        print "Please come back!"

print_special_greeting("John")
print_special_greeting("John", True)
print_special_greeting("John", True, "rainy")
print_special_greeting("John", condition = "horrible")

def print_siblings(name, *siblings):
    print name, "has the following siblings:"
    for sibling in siblings:
        print sibling
    print

print_siblings("John", "Ashley", "Lauren", "Arthur")

def print_brothers_sisters(name, **siblings):
    print name, "has the following siblings:"
    for sibling in siblings:
        print sibling, ":", siblings[sibling]
    print

print_brothers_sisters("John", Ashley="sister", Lauren="sister", Arthur="brother")

columns = [rem_nl(col.get_text()) for col in rows[0].find_all("th") if col.get_text()]
columns

indexes = [row.find("th").get_text() for row in rows[1:]]
indexes

to_num = lambda s: s[-1] == "%" and int(s[:-1]) or None

values = [to_num(value.get_text()) for row in rows[1:] for value in row.find_all("td")]
values

zip([1,2,3],[4,5,6])

stacked_values = zip(*[values[i::3] for i in range(len(columns))])
stacked_values

def print_args(arg1, arg2, arg3):
    print arg1, arg2, arg3

print_args(1,2,3)

print_args([1,10], [2,20], [3,30])

parameters = [100, 200, 300]
p1 = parameters[0]
p2 = parameters[1]
p3 = parameters[2]

print_args(p1, p2, p3)
print_args(*parameters)

{ind: value for ind, value in zip(indexes, stacked_values)}

import pandas as pd
df = pd.DataFrame(stacked_values, columns=columns, index=indexes)
df

data_dicts = [{col: val for col, val in zip(columns, col_values)} for col_values in stacked_values]
data_dicts

pd.DataFrame(data_dicts, index=indexes)

stacked_by_col = [values[i::3] for i in range(len(columns))]
stacked_by_col

data_lists = {col: val for col, val in zip(columns, stacked_by_col)}
data_lists
pd.DataFrame(data_lists, index = indexes)

df.dtypes

df.dropna()

df.dropna(axis=1)

df_clean = df.fillna(0).astype(int)
df_clean
df_clean.dtypes

df_clean.describe()

import numpy as np

df_clean.values
type(df_clean.values)

np.mean(df_clean['Undergraduate'])
np.std(df_clean)
np.median(df_clean)

df_clean["Undergraduate"]
df_clean.Undergraduate

df_clean.loc["Asian/Pacific Islander"]
df_clean.iloc[0]
df_clean.ix["Asian/Pacific Islander"]

df_clean.loc["White/non-Hispanic", "Graduate and professional"]
df_clean.iloc[3, 1]
df_clean.ix[3, "Graduate and professional"]

df_flat = df_clean.stack().reset_index()
df_flat.columns = ["race", "source", "percentage"]
df_flat

grouped = df_flat.groupby("race")
grouped.groups

type(grouped)

mean_percs = grouped.mean()
mean_percs
type(mean_percs)

for name, group in df_flat.groupby("source", sort = True):
    print name
    print group

mean_percs.plot(kind="bar")