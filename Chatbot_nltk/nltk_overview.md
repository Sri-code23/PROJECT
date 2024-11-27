# Introduction to NLTK Library
# ======================================

The Natural Language Toolkit (NLTK) is a comprehensive library used for Natural Language Processing (NLP) tasks. It provides a wide range of tools and resources for text processing, tokenization, stemming, lemmatization, parsing, and semantic reasoning.

# Important and Basic NLTK Modules
# ======================================

### 1. Tokenization

Tokenization is the process of breaking down text into individual words or tokens.

```python
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

text = "This is an example sentence for NLTK library."
words = word_tokenize(text)
sentences = sent_tokenize(text)

print("Tokenized Words:", words)
print("Tokenized Sentences:", sentences)
```

Output:
```
Tokenized Words: ['This', 'is', 'an', 'example', 'sentence', 'for', 'NLTK', 'library', '.']
Tokenized Sentences: ['This is an example sentence for NLTK library.']
```

### 2. Stopwords Removal

Stopwords are common words like "is," "and," "the," etc. that do not add much value to the meaning of a sentence.

```python
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
words = word_tokenize(text)
filtered_words = [word for word in words if word.lower() not in stop_words]

print("Filtered Words:", filtered_words)
```

Output:
```
Filtered Words: ['This', 'example', 'sentence', 'NLTK', 'library', '.']
```

### 3. Stemming

Stemming is the process of reducing words to their base form.

```python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = word_tokenize(text)
stemmed_words = [stemmer.stem(word) for word in words]

print("Stemmed Words:", stemmed_words)
```

Output:
```
Stemmed Words: ['this', 'is', 'an', 'exampl', 'sentenc', 'for', 'nltk', 'librari', '.']
```

### 4. Lemmatization

Lemmatization is the process of reducing words to their base or root form.

```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
words = word_tokenize(text)
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

print("Lemmatized Words:", lemmatized_words)
```

Output:
```
Lemmatized Words: ['This', 'is', 'an', 'example', 'sentence', 'for', 'NLTK', 'library', '.']
```

### 5. Part-of-Speech (POS) Tagging

POS tagging is the process of identifying the part of speech (noun, verb, adjective, etc.) of each word in a sentence.

```python
from nltk import pos_tag

words = word_tokenize(text)
tagged_words = pos_tag(words)

print("POS Tagged Words:", tagged_words)
```

Output:
```python
POS Tagged Words: [('This', 'DT'), ('is', 'VBZ'), ('an', 'DT'), ('example', 'NN'), ('sentence', 'NN'), ('for', 'IN'), ('NLTK', 'NNP'), ('library', 'NN'), ('.', '.')]
```

### 6. Named Entity Recognition (NER)

NER is the process of identifying named entities (people, places, organizations, etc.) in a sentence.

```python
from nltk import ne_chunk, pos_tag

words = word_tokenize(text)
tagged_words = pos_tag(words)
ner_tags = ne_chunk(tagged_words)

print("NER Tagged Words:", ner_tags)
```

Output:
```python
NER Tagged Words: (S 
  This/DT 
  is/VBZ 
  an/DT 
  example/NN 
  sentence/NN 
  for/IN 
  NLTK/NNP 
  library/NN 
  ./.
)
```

### 7. Frequency Distribution

Frequency distribution is the process of calculating the frequency of each word in a sentence.

```python
from nltk.probability import FreqDist

words = word_tokenize(text)
freq_dist = FreqDist(words)

print("Frequency Distribution:", freq_dist)
```

Output:
```python
Frequency Distribution: FreqDist({'This': 1, 'is': 1, 'an': 1, 'example': 1, 'sentence': 1, 'for': 1, 'NLTK': 1, 'library': 1, '.': 1})
```

### 8. Corpora

NLTK provides a wide range of corpora (collections of text) for various NLP tasks.

```python
from nltk.corpus import gutenberg

text = gutenberg.raw('austen-persuasion.txt')
print(text)
```

Output:
```
The text of the book "Persuasion" by Jane Austen.
```

### 9. Text Processing

NLTK provides various tools for text processing, including tokenization, stemming, lemmatization, and parsing.

```python
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

text = "This is an example sentence for NLTK library."
words = word_tokenize(text)
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]

print("Stemmed Words:", stemmed_words)
```

Output:
```
Stemmed Words: ['this', 'is', 'an', 'exampl', 'sentenc', 'for', 'nltk', 'librari', '.']
```

### 10. Semantic Reasoning

NLTK provides tools for semantic reasoning, including WordNet and FrameNet.

```python
from nltk.corpus import wordnet

synsets = wordnet.synsets('dog')
print(synsets)
```

Output:
```python
[Synset('dog.n.01'), Synset('dog.n.02'), Synset('dog.n.03'), Synset('dog.n.04'), Synset('frump.n.01')]
```