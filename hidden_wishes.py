
# coding: utf-8

# # A tiny birthday hack
# 
# ## Which author sent me the largest amount of secret birthday wishes?
# 
# Programming on my birthday in the back of a car, after driving and walking around :)

# In[1]:

import nltk
from nltk.corpus import gutenberg as gb
import re


# In[4]:

# shopping for ingredients
all_books = gb.fileids()


# In[71]:

def get_ingredients(booktitle):
    """selects only the best ingredients for the cake"""
    happy_regex = re.compile(r"(?i)[^hapybirthd]")
    text = gb.raw(fileids=booktitle)
    dough = re.sub(happy_regex, "", text)
    return dough

def knead(dough):
    """kneads <span>s into the dough, wherever wishes match."""
    # two-step regex
    b_regex = re.compile(r"happy")
    d_regex = re.compile(r"birthday")
    # stats for fun
    nr_happies = len(re.findall(b_regex, dough))
    nr_birthdays = len(re.findall(d_regex, dough))
    icing = (nr_happies, nr_birthdays)
    # mark the occurances with <span>s
    b_text = re.sub(b_regex, "<span>" + b_regex.pattern + "</span>", dough)
    d_text = re.sub(d_regex, "<span>" + d_regex.pattern + "</span>", b_text)
    cake = d_text
    return cake, icing

def bake(cake, icing, ingredients):
    """bakes a HTML page from the highlighted dough."""
    with open("bd_" + ingredients + ".html", 'w') as f:
        pretty_file = """<DOCTYPE html>
<html>
<head>
  <title>""" + ingredients + """</title>
  <style>
    body {
      max-width: 800px;
      margin: auto;
      word-wrap: break-word;
    }
    span {
      background: lightgreen;
    }
  </style>
</head>
<body>
  <h1>Birthday Wishes hidden in """ + ingredients + """</h1>
  <h2># of happies: """ + str(icing[0]) + """</h2>
  <h2># of birthdays: """ + str(icing[1]) + """</h2>
  <div>""" + cake + """</div>
</body>
</html>"""
        f.write(pretty_file)
        
def tons_of_wishes(book_list):
    """makes a lot of cakes at once. because age."""
    for book in book_list:
        ingredients = book
        cake, icing = knead(get_ingredients(ingredients))
        bake(cake, icing, ingredients)


# In[80]:

# happy birthday to myself :)
tons_of_wishes(all_books)


# I uncovered the largest number of hidden wishes in `edgeworth-parents.txt`. Thanks mum and dad 😊

# In[46]:

# interesting challenge: try using regex groups for matching and replacing!
#birth_regex = re.compile(r"(happy)\w*(birthday)")
#m = re.match(r"(happy)\w*(birthday)", dough)
#m.groups()

