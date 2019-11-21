# evan johanns
# ex 41
# 11/21/19
import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/word.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%) :":
        "Make a class named %%% that is-a %%%.",
    "class%%%(object):\n\tdef___init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class%%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "set ***  to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else
    PHRASE_FIRST = False

# load up to the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

def convert(snippet, phrase):
    Class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names =
