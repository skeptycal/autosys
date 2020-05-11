# remove noise from text
# code by Pablo Salvador Lopez
# from https://towardsdatascience.com/distributed-text-preprocessing-with-python-and-dask-5312a4d26ae
from nltk.corpus import stopwords


def remove_noise(text):

    text = re.sub(r",", "", text)
    text = re.sub(r"\w+\d+", " numbers", text)
    text = re.sub(r'\d+', 'numbers', text)
    text = re.sub(r"\$", "dollar ", text)
    text = re.sub(r"\$+", "dollar ", text)
    text = re.sub(r"dollars", "dollar", text)
    text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)
    text = re.sub(r"!", " ", text)
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r":", "", text)
    text = re.sub(r" :", "", text)
    text = re.sub(r"\w+\-\w+", "", text)
    text = re.sub(r" -", "", text)
    text = re.sub(r" s ", "", text)
    text = re.sub(r" - ", "", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    #text = re.sub(r",", "", text)
    #text = re.sub(r"\.", " ", text)
    text = re.sub(r"!", " ! ", text)
    text = re.sub(r"\/", " ", text)
    text = re.sub(r"\^", " ^ ", text)
    text = re.sub(r"\+", " + ", text)
    text = re.sub(r"\-", " - ", text)
    text = re.sub(r"\=", " = ", text)
    text = re.sub(r"'", " ", text)
    text = re.sub(r"(\d+)(k)", r"\g<1>000", text)
    text = re.sub(r":", " : ", text)
    text = re.sub(r" e g ", " eg ", text)
    text = re.sub(r" b g ", " bg ", text)
    text = re.sub(r" u s ", " american ", text)
    text = re.sub(r"\0s", "0", text)
    text = re.sub(r" 9 11 ", "911", text)
    text = re.sub(r"e - mail", "email", text)
    text = re.sub(r"j k", "jk", text)
    text = re.sub(r"\s{2,}", " ", text)
    text = re.sub(r"", "", text)
    return text

    def remove_noise2(text):
    text = text.replace(".", "")
    return text

    def expand_contractions(text, contraction_mapping=CONTRACTION_MAP):

    contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())),
                                      flags=re.IGNORECASE | re.DOTALL)

    def expand_match(contraction):
        match = contraction.group(0)
        first_char = match[0]
        expanded_contraction = contraction_mapping.get(match)\
            if contraction_mapping.get(match)\
            else contraction_mapping.get(match.lower())
        expanded_contraction = first_char + expanded_contraction[1:]
        return expanded_contraction

    expanded_text = contractions_pattern.sub(expand_match, text)
    expanded_text = re.sub("'", "", expanded_text)
    return expanded_text


# remove stopwords
stop_words = stopwords.words("english")


def remove_stopwords3(text):
    tokens = tokenizer.tokenize(text)
    filtered_words = [w for w in tokens if len(w) > 2 if not w in stop_words]

    return " ".join(filtered_words)


def clean_text(df):

    df["review"] = df.review.map(lambda review: review.lower()).map(
        remove_noise).map(expand_contractions).map(remove_noise2).map(remove_stopwords3)

    return df
