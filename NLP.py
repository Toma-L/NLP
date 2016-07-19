#Natural Language Processing with Python

#1.1

import nltk
#nltk.download()
#download book
from nltk.book import *
text1
text2
text1.concordance("monstrous")
text2.concordance("affection")

text1.similar("monstrous")
text2.similar("monstrous")

text2.common_contexts(["monstrous", "very"])

text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

text3.generate() #not working any more
len(text3)
sorted(set(text3)) #sorted: from ,./ to abc, from A to Z, from a to z
len(set(text3)) #2789 unique symbols and words

from __future__ import division
text3.count("smote")
100 * text4.count("a") / len(text4) #1.46% of text4 is "a"

text5.count("lol") #704
text5.count("lol") / len(text5) * 100 #1.56% of text5 is "lol"

def lexical_diversity(text):
    return len(text) / len(set(text))
    
def percentage(count, total):
    return 100 * count / total

lexical_diversity(text3)
lexical_diversity(text5)
percentage(4, 5)
percentage(text4.count('a'), len(text4))

#1.2