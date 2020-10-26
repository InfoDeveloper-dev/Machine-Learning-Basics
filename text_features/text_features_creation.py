"""
Program is to implement two feature extraction techniques of text

1.) Bags of Words
2.) TFIDF
"""

import pandas as pd
import re

dict_text_featutes = {
    'Models': ['BOW', 'TFIDF'],
    'Importance': ['Partially', 'Fully'],
    'Sequence': ['Yes', 'Yes'],
    'Semantic': ['No', 'No']
}

# Convert dictionary into dataframe
df_text_features = pd.DataFrame.from_dict(
                   dict_text_featutes
                   )

df_text_features.set_index(
                "Models",
                inplace=True
                )

"""
Let us understand BAG OF WORDS USING BELOW DOCUMENT
Suppose we have a document and we have been given below a para \
about india

India is a good country. India contains many cultures and religions

Now, we have to convert this to integer for machine to understand.
According to BOW, first we need to create vocuabulary from this and \
then count occurence of words of above given sentence using vocab

Vocab must be unique
"""


def creating_vocab(text_string):
    """
    Creating vocabulary which is unique
    Fetaures are created using this vocab
    """
    text_string_lower = text_string.lower()
    text_string_re = re.sub(r'\.', '', text_string_lower)
    data_in_list = text_string_re.split()
    data_in_set = set(data_in_list)
    return data_in_set


def feat_from_vocab(text_to_convert, vocabulary):
    """
    Text whose features are to be created are compared with vocab
    returns features in integer form for model to train
    """
    words_split = text_to_convert.split()
    dict_words_count = dict()
    for each_token in words_split:
        if each_token in vocabulary:
            # if value occures in dict count is incremented
            # else count is one
            if each_token in dict_words_count:
                dict_words_count[each_token] += 1
            else:
                dict_words_count[each_token] = 1
        else:
            dict_words_count[each_token] = 0

    text_to_features_list = list()
    for key, value in dict_words_count.items():
        text_to_features_list += [value]        
            
    return text_to_features_list        



corpus = """India is a good country. India contains many cultures 
and religions.
"""  

text_for_features = """ 
India contains cultures. India is also land of festivals"""

text_for_features_lo = text_for_features.lower()

text_for_features_lo_re = re.sub(
            r'\.', '', text_for_features_lo
            ) 

text_to_feat_vocab = creating_vocab(corpus)  

text_to_features = feat_from_vocab(
                   text_for_features_lo,
                   text_to_feat_vocab   
                   )
print(
     "Text to features for the sentence: {} is: {}".format(
      text_for_features, 
      text_to_features   
     )
)     
