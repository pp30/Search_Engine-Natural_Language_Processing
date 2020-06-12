from util import *
import numpy as np
from numpy import dot
from numpy.linalg import norm
# Add your import statements here
import operator
import datetime as dt
import warnings
warnings.filterwarnings("ignore")

class InformationRetrieval():

    def __init__(self):
        self.index = None

    def buildIndex(self, docs, docIDs):
        """
        Builds the document index in terms of the document
        IDs and stores it in the 'index' class variable

        Parameters
        ----------
        arg1 : list
            A list of lists of lists where each sub-list is
            a document and each sub-sub-list is a sentence of the document
        arg2 : list
            A list of integers denoting IDs of the documents
        Returns
        -------
        None
        """
        # print('-'*30,'\n', docIDs,'\n', '-'*30)
        start = dt.datetime.now()
        index = None
        D = len(docs)
        # print("len(docs)",len(docs))
        
        list_of_words = []
        
        for document in docs:
           for sentence in document:
               for word in sentence:
                       list_of_words.append(word)   #this can have repetition of words 

        self.list_unique = list(set(list_of_words))

        # print('unique_list operation took:', dt.datetime.now()-start)

        start = dt.datetime.now()
        df = np.zeros(len(self.list_unique)) # df(i) is number of docs containing term i, used for calculating IDF 
        
        TD_matrix = np.zeros([len(self.list_unique),len(docs)]) #term-document matrix
        
        
        for j, doc in enumerate(docs):       # iterate over documents
            for k, sentence in enumerate(doc):  # iterate over sentences for a document
                for word in sentence:
                    # for i, unique_word in enumerate(self.list_unique):    # iterate over terms
                    #     if unique_word == word:
                    #         TD_matrix[i,j] += 1    # update term frequency
                    #         break
                    try:
                        TD_matrix[self.list_unique.index(word),j] += 1
                    except:
                        temp_skip = 0
        
        df = np.sum(TD_matrix > 0, axis=1)

        self.IDF = np.log(D/df)            
        # print('IDF operation took:', dt.datetime.now()-start)

        start = dt.datetime.now()

        self.doc_weights = np.zeros([len(self.list_unique),len(docs)])
        # print("check if 8835: ", len(self.doc_weights[:,0]))
        
        for i in range(len(self.list_unique)):
            self.doc_weights[i,:] = self.IDF[i]*TD_matrix[i,:]   # vector weights for each document 
                      

        index = {key: None for key in docIDs}  # initialize dictionary with keys as doc_IDs
       
        for j in range(len(docs)): 
           index[docIDs[j]] = self.doc_weights[:,j]   # update dict-values with weight vector for corresponding docIDs                
        
        # print("len(self.doc_weights[:][0]", len(self.doc_weights[:,0]))        
        # print('doc_weights operation took:', dt.datetime.now()-start)
        self.index = index
        

    def rank(self, queries):
        """
        Rank the documents according to relevance for each query

        Parameters
        ----------
        arg1 : list
            A list of lists of lists where each sub-list is a query and
            each sub-sub-list is a sentence of the query
        

        Returns
        -------
        list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        """

        # we have already calculated the document vectors in previous function
        start = dt.datetime.now()
        TQ_matrix = np.zeros([len(self.list_unique),len(queries)]) # term frequency matrix (for each query in list queries)
        
        for i, unique_word in enumerate(self.list_unique):
            for j, query in enumerate(queries):       # iterate over all queries
                for k, sentence in enumerate(query):  # iterate over sentences for a query
                    for word in sentence:
                        if unique_word == word:
                            TQ_matrix[i,j] += 1 

        # print('TQ operation took:', dt.datetime.now()-start)
        start = dt.datetime.now()
        self.query_weights = np.zeros([len(self.list_unique),len(queries)])
        
        for i, unique_word in enumerate(self.list_unique):
            self.query_weights[i,:] = self.IDF[i]*TQ_matrix[i,:]  # vector weights for each query  
        
        id_docs = list(self.index.keys())
        
        
        doc_IDs_ordered  = list(range(len(queries)))
        # print('Pre-Ranking operation took:', dt.datetime.now()-start)
        start = dt.datetime.now()
        # print('length of queries:', len(queries))
        for j in range(len(queries)):
            dict_cosine = {key: None for key in id_docs} # given ONE query, stores cosine measures for between query and all docs
            # for i in range(len(self.index)):
            #     a = self.index[id_docs[i]]
            #     b = self.query_weights[:,j]
            #     dict_cosine[id_docs[i]] = dot(a,b)/(norm(a)*norm(b))
            for doc_id, doc_vector in self.index.items():
                a = doc_vector
                b = self.query_weights[:,j]
                dict_cosine[doc_id] = dot(a,b)/(norm(a)*norm(b))
                 
            dc_sort = sorted(dict_cosine.items(),key = operator.itemgetter(1),reverse = True)
            # temp = [x for x, _ in dc_sort]
            # for k in range(len(dc_sort)):
            #     temp.append(dc_sort[k][0])  # take only the keys (doc IDs) and store in temp
                
                 
            doc_IDs_ordered[j] = [x for x, _ in dc_sort]  #sorted docIDs stored corresponding to that query 
        # print('Ranking operation took:', dt.datetime.now()-start)

        # doc_IDs_ordered = []

        #Fill in code here

        return doc_IDs_ordered




