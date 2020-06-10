""" HashedIndex - InvertedIndex implementation using hash lists

    ```sh
    pip install hashedindex
    ```

    Fast and simple InvertedIndex implementation using hash lists (python dictionaries).

    Supports Python 3.5+

    Free software: BSD license

    Copyright (c) 2015, Michael Aquilina
    All rights reserved.

    Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

    * Neither the name of hashedindex nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    """

import math
import re
import unicodedata
from copy import copy
from string import ascii_letters, digits, punctuation

from hashed_index import *


# Stemmer interface which returns token unchanged
class NullStemmer:
    def stem(self, x):
        return x

    def __repr__(self):
        return "<NullStemmer>"


if True:
    _stopwords = frozenset()
    _accepted = frozenset(ascii_letters + digits + punctuation) - frozenset(
        "'"
    )

    _punctuation = copy(punctuation)
    _punctuation = _punctuation.replace("\\", "")
    _punctuation = _punctuation.replace("/", "")
    _punctuation = _punctuation.replace("-", "")

    _re_punctuation = re.compile("[%s]" % re.escape(_punctuation))
    _re_token = re.compile(r"[a-z0-9]+")

    _url_pattern = r"(https?:\/\/)?(([\da-z-]+)\.){1,2}.([a-z\.]{2,6})(/[\/\w \.-]*)*\/?(\?(\w+=\w+&?)+)?"
    _re_full_url = re.compile(r"^%s$" % _url_pattern)
    _re_url = re.compile(_url_pattern)


# Determining the best way to calculate tfidf is proving difficult,
# might need more advanced techniques
def tfidf(tf, df, corpus_size):
    """
    In information retrieval, tf–idf or TFIDF, short for term frequency–inverse document frequency, is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus.

    It is often used as a weighting factor in searches of information retrieval, text mining, and user modeling. The tf–idf value increases proportionally to the number of times a word appears in the document and is offset by the number of documents in the corpus that contain the word, which helps to adjust for the fact that some words appear more frequently in general.

    tf–idf is one of the most popular term-weighting schemes today. A survey conducted in 2015 showed that 83% of text-based recommender systems in digital libraries use tf–idf.
    """
    if df and tf:
        return (1 + math.log(tf)) * math.log(corpus_size / df)
    else:
        return 0.0


def normalize_unicode(text):
    """
    Normalize any unicode characters to ascii equivalent

    Return the normal form form for the Unicode string unistr. Valid values for form are ‘NFC’, ‘NFKC’, ‘NFD’, and ‘NFKD’.

    https://docs.python.org/3.8/library/unicodedata.html#unicodedata.normalize
    """
    if isinstance(text, str):
        return (
            unicodedata.normalize("NFKD", text)
            .encode("ascii", "ignore")
            .decode("utf8")
        )
    else:
        return text


def get_ngrams(token_list, n=2):
    for i in range(len(token_list) - n + 1):
        yield token_list[i : i + n]


def word_tokenize(
    text, stopwords=_stopwords, ngrams=None, min_length=0, ignore_numeric=True
):
    """
    Parses the given text and yields tokens which represent words within
    the given text. Tokens are assumed to be divided by any form of
    whitespace character.
    """
    if ngrams is None:
        ngrams = 1

    text = re.sub(re.compile("'s"), "", text)  # Simple heuristic
    text = re.sub(_re_punctuation, "", text)

    matched_tokens = re.findall(_re_token, text.lower())
    for tokens in get_ngrams(matched_tokens, ngrams):
        for i in range(len(tokens)):
            tokens[i] = tokens[i].strip(punctuation)

            if len(tokens[i]) < min_length or tokens[i] in stopwords:
                break
            if ignore_numeric and isnumeric(tokens[i]):
                break
        else:
            yield tuple(tokens)


def isnumeric(text):
    """
    Returns a True if the text is purely numeric and False otherwise.
    """
    try:
        float(text)
    except ValueError:
        return False
    else:
        return True


def is_url(text):
    """
    Returns a True if the text is a url and False otherwise.
    """
    return bool(_re_full_url.match(text))
