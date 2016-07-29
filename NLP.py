#Natural Language Processing with Python

#1.1====================

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


#1.2====================

sent1 = ["Call", "me", "Ishmael", "."]
sent1
lexical_diversity(sent1)

ex1 = ["Monty", "Python", "and", "the", "Holy", "Grail"]
sorted(set(ex1))
len(set(ex1))
ex1.count("Monty")

["Monty", "Python"] + ["and", "the", "Holy", "Grail"]

sent4 + sent1

sent1.append("Some") #add one item to sent1

len(sent1)
sent1

text4[173] #call number 173 word of text4
text4.index("awaken")

text5[16715:16735]
text6[1600:1625] #actually 1600~1624

sent = ["word1", "word2", "word3", "word4", "word5", "word6", "word7", "word8", "word9", "word10"]
sent[0]
sent[9]

sent[10] #Error but not Syntax Error

sent[5:8]
sent[5]
sent[7]

sent[:3] #0~2
text2[141525:]

sent[0] = "First"
sent[9] = "Last"
sent

sent1 = ["Call", "me", "Ishmael", "."]
my_sent = ["Bravely", "bold", "Sir", "Robin", ",", "rode", "forth", "from", "Camelot", "."]
noun_phrase = my_sent[1:4]
noun_phrase
wOrDs = sorted(noun_phrase)
wOrDs

not = "Camelot" #Error

vocab = set(text1)
vocab_size = len(vocab)
vocab_size

name = "Monty"
name[0]
name[:4]

name * 2
name + "!"

" ".join(["Monty", "Python"])
"Monty Python".split()


#1.3====================

saying = ["After", "all", "is", "said", "and", "done", "more", "is", "said", "than", "done"]
tokens = set(saying)
tokens = sorted(tokens)
tokens[-2:] #count from backward

fdist1 = FreqDist(text1)
fdist1
vocabulary1 = list(fdist1.keys())
vocabulary1[:50] #Freq top 50 words

fdist1['whale']


fdist2 = FreqDist(text2)
fdist2
vocabulary2 = list(fdist2.keys())
vocabulary2[:50]

fdist1.plot(50, cumulative = True)
fdist2.plot(50, cumulative = True)

fdist1.hapaxes() #words only appear once

V = set(text1)
long_words = [w for w in V if len(w) > 15] #long words
sorted(long_words)

vocab = set(text1)
long_words = [word for word in vocab if len(word) > 15]
sorted(long_words)


fdist5 = FreqDist(text5)
sorted([w for w in set(text5) if len(w) > 7 and fdist5[w] > 7]) #nchar > 7 and freq > 7

list(bigrams(['more', 'is', 'said', 'than', 'done'])) #bigrams() isn't working! WHY


text4.collocations()
text8.collocations()

[len(w) for w in text1]
fdist = FreqDist([len(w) for w in text1])
fdist
fdist.keys()

fdist.items()
fdist.max()
fdist[3]
fdist.freq(3)

fdist['monstrous']
fdist.N()
fdist.tabulate()
fdist.plot()
fdist.max()
fdist.plot(cumulative = True)
fdist1 < fdist2


#1.4====================

sent7
[w for w in sent7 if len(w) < 4]
[w for w in sent7 if len(w) <= 4]
[w for w in sent7 if len(w) == 4]
[w for w in sent7 if len(w) != 4]

sent7[0].startswith("P")
sent7[0].endswith("t")
"e" in sent7[0]
sent7[0].islower()
sent7[0].isupper()
sent7[0].isalpha()
sent7[0].isalnum()
sent7[3].isdigit()
sent7[0].istitle()

sorted([w for w in set(text1) if w.endswith('ableness')])
sorted([term for term in set(text4) if 'gnt' in term])
sorted([item for item in set(text6) if item.istitle()])
sorted([item for item in set(sent7) if item.isdigit()])

sorted([w for w in set(text7) if '-' in w and 'index' in w])
sorted([wd for wd in set(text3) if wd.istitle() and len(wd) > 10])
sorted([t for t in set(text2) if 'cie' in t or 'cei' in t])

[len(w) for w in text1]
[w.upper() for w in text1]

len(text1)
len(set(text1))
len(set([word.lower() for word in text1])) #eliminate the difference between upper & lower
len(set([word.lower() for word in text1 if word.isalpha()])) #only alpha left

word = 'cat'
if len(word) < 5:
    print ('word length is less than 5')

if len(word) >=5:
    print ('word length is greater than or equal to 5')

for word in ['Call', 'me', 'Ishmael', '.']:
    print (word)

sent1 = ['Call', 'me', 'Ishmael', '.']
for xyzzy in sent1:
    if xyzzy.endswith('l'):
        print (xyzzy)

for token in sent1:
    if token.islower():
        print (token, 'is a lowercase word')
    elif token.istitle():
        print (token, 'is a titlecase word')
    else:
        print (token, 'is punctuation')

tricky = sorted([w for w in set(text2) if 'cie' in w or 'cei' in w])
for word in tricky:
    print (word),


#2.1====================

import nltk
nltk.corpus.gutenberg.fileids()
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
len(emma)
emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
emma.concordance('surprize')

#another way to do this

from nltk.corpus import gutenberg
gutenberg.fileids()
emma = gutenberg.words('austen-emma.txt')

for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    print (int(num_chars/num_words), int(num_words/num_sents)) #avg word & sentence length and the diversity of words

macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
macbeth_sentences #load sentences of Macbeth
macbeth_sentences[1037]
longest_len = max([len(s) for s in macbeth_sentences])
[s for s in macbeth_sentences if len(s) == longest_len] #find longest sentence

from nltk.corpus import webtext
for fileid in webtext.fileids():
    print (fileid, webtext.raw(fileid)[:65], '...')

from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
chatroom[123]

from nltk.corpus import brown
brown.categories()
brown.words(categories = 'news') 
brown.words(fileids = ['cg22'])

from nltk.corpus import brown
news_text = brown.words(categories = 'news')
fdist = nltk.FreqDist([w.lower() for w in news_text])
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print (m + ':', fdist[m],)

cfd = nltk.ConditionalFreqDist(
        (genre, word)
        for genre in brown.categories()
        for word in brown.words(categories = genre))

genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfd.tabulate(conditions = genres, samples = modals)

from nltk.corpus import reuters
reuters.fileids()
reuters.categories()

reuters.categories('training/9865')
reuters.categories(['training/9865', 'training/9880'])
reuters.fileids('barley')
reuters.fileids(['barley', 'corn'])

reuters.words('training/9865')[:14]
reuters.words(['training/9865', 'training/9880'])
reuters.words(categories = 'barley')
reuters.words(categories = ['barley', 'corn'])

from nltk.corpus import inaugural
inaugural.fileids()
[fileid[:4] for fileid in inaugural.fileids()]

cfd = nltk.ConditionalFreqDist(
        (target, fileid[:4])
        for fileid in inaugural.fileids()
        for w in inaugural.words(fileid)
        for target in ['america', 'citizen']
        if w.lower().startswith(target))

cfd.plot()

nltk.corpus.cess_esp.words()
nltk.corpus.floresta.words() #Error
nltk.corpus.indian.words('hindi.pos')
nltk.corpus.udhr.fileids()
nltk.corpus.udhr.words('Javanese-Latin1')[11:]

from nltk.corpus import udhr
languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd = nltk.ConditionalFreqDist(
        (lang, len(word))
        for lang in languages
        for word in udhr.words(lang + '-Latin1'))
cfd.plot(cumulative = True)

raw = gutenberg.raw("burgess-busterbrown.txt")
raw[1:20]
words = gutenberg.words("burgess-busterbrown.txt")
words[1:20]
sents = gutenberg.sents("burgess-busterbrown.txt")
sents[1:20]

from nltk.corpus import PlaintextCorpusReader
corpus_root = '' #yourown file
wordlists = PlaintextCorpusReader(corpus_root, '.*')
wlrdlists.fileids()
wordlists.words('connectives')

from nltk.corpus import BracketParseCorpusReader
corpus_root = r""
file_pattern = r".*/wsj_.*\.mrg"
ptb = BracketParseCorpusReader(corpus_root, file_pattern)
ptb.fileids()
len(ptb.sents())
ptb.sents(fileids = '20/wsj_2013.mrg')[19]


#2.2====================

text = ['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]
pairs = [('news', 'The'), ('news', 'Fulton'), ('news', 'County'), ...]

import nltk
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
        (genre, word)
        for genre in brown.categories()
        for word in brown.words(categories = genre))

genre_word = [(genre, word)
                for genre in ['news', 'romance']
                for word in brown.words(categories = genre)]
                    
len(genre_word)

genre_word[:4]
genre_word[-4:]

cfd = nltk.ConditionalFreqDist(genre_word)
cfd

cfd.conditions()

cfd['news']
cfd['romance']
list(cfd['romance'])
cfd['romance']['could']

from nltk.corpus import inaugural
cfd = nltk.ConditionalFreqDist(
        (target, fileid[:4])
        for fileid in inaugural.fileids()
        for w in inaugural.words(fileid)
        for target in ['america', 'citizen']
        if w.lower().startswith(target))

from nltk.corpus import udhr
languages = ['Chickasaw', 'English', 'German_Deutsch',
             'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd = nltk.ConditionalFreqDist(
        (lang, len(word))
        for lang in languages
        for word in udhr.words(lang + '-Latin1'))
cfd

cfd.tabulate(conditions = ['English', 'German_Deutsch'], samples = range(10), cumulative = True)


#showyourwork / p.58
genre_word = [(genre, word)
                for genre in ['news', 'romance']
                for word in brown.words(categories = genre)]
cfd = nltk.ConditionalFreqDist(genre_word)
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
cfd.tabulate(samples = days)


sent = ['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven', 'and', 'the', 'earth', '.']
nltk.bigrams(sent) #doesn't work

def generate_model(cfdist, word, num = 15):
    for i in range(num):
        print (word),
        word = cfdist[word].max()
text = nltk.corpus.genesis.words('english-kjv.txt')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)

print (cfd['living'])
generate_model(cfd, 'living')
