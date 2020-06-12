# CS6370-Natural_Language_Processing
NLP Coursework @ IIT Madras 

Both the assignments involve implemeting a basic search engine application. We use the cranfield dataset for the same.

## Dataset
The Cranfield dataset contains 1400 documents (cran_docs.json), 225 queries (cran_queries.json), and query-document relevance judgements (cran_qrels.json). 

The positions of the reference documents for each query (in cran_qrels.json) indicate the following judgements: <\br>
1 - References which are a complete answer to the question <\br>
2 - References of a high degree of relevance, the lack of which either would have made the research impracticable or would have resulted in a considerable amount of extra work  <\br>
3 - References which were useful, either as general background to the work or as suggesting methods of tackling certain aspects of the work <\br>
4 - References of minimum interest, for example, those that have been included from an historical viewpoint <\br>
Query-Reference pairs in which the reference is of no interest to the query are excluded from the relevance file 

More on the Cranfield dataset: http://ir.dcs.gla.ac.uk/resources/test_collections/cran/

## Assgn-1
Build a basic text processing module that implements:  <\br>
1- sentence segmentation <\br>
2- tokenization <\br>
3- stemming and lemmatization <\br>
4- stopword removal<\br>

## Assgn-2
- Implementing an Information Retrieval system using the Vector Space Model with the same dataset.
- Implement the following evaluation metrics and analyse results: <\br>
(a) Precision @ k <\br>
(b) Recall @ k <\br>
(c) F-Score @ k <\br>
(d) Average Precision @ k <\br>
(e) nDCG @ k






