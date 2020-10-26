"""
Program is to implement two feature extraction techniques of text

1.) Bags of Words
2.) TFIDF
"""

import pandas as pd
import re
import math 

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
print("Result using BAG OF WORDS APPROACH")
print("-"*50)
print(
     "Text is: {}\nand features are:\n {}".format(
      text_for_features, 
      text_to_features   
     )
)     
print("-"*50)
"""
Implementing TFIDF 

TF: Term Frequency i.e num of times a word appers in document/
                       total number of words in the document

IDF: Inverse Document Frequency i.e 
                    log(number of document/documents where words 
                    appears)

"""
doc1 = "My name is developer"
doc2 = "I love python"
doc3 = "python is my passion"


def all_cases_to_lower(string):

    string = string.lower()
    return string


def term_frequency(document, word):
    
    document = all_cases_to_lower(document)
    word = all_cases_to_lower(word)

    doc_list = document.split()
    len_of_doc = len(doc_list)
    
    if word in doc_list:
        document_count = doc_list.count(word)
    else:
        print("select word from the document only")
    term_freq = (document_count/len_of_doc)

    return term_freq


def inverse_frequency_document(total_document, word):

    len_documents = len(total_document)
    count = 0
    word = all_cases_to_lower(word)
    for i in range(len_documents):
        if word in total_document[i]:
            count += 1
    
    idf_result = math.log(len_documents/count) 

    return idf_result

# calculating the term frequency of each word in document 1
doc1_in_list = doc1.split()
print()
print("TF Calculation for Document 1")
print("Word".ljust(20), "Term Frequency")
print()
for each_word in doc1_in_list:
    term_fre = term_frequency(doc1, each_word)
    print(each_word.ljust(20), term_fre)

documents_list = [doc1, doc2, doc3]
document_list_lo = [i.lower() for i in documents_list]
print()
print("IDF Calculation for word python")
print("Word".ljust(20), "Inverse Document Frequency")
python_idf = inverse_frequency_document(
             document_list_lo,
             "Python"
    ) 
print("Python".ljust(20), python_idf)



