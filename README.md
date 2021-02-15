# Search Engine  - Natural_Language_Processing

The implementation of the toy search engine is split into 2 parts. We use the cranfield dataset for the same.

## Dataset
The Cranfield dataset contains 1400 documents (cran_docs.json), 225 queries (cran_queries.json), and query-document relevance judgements (cran_qrels.json). 

The positions of the reference documents for each query (in cran_qrels.json) indicate the following judgements: 
1. References which are a complete answer to the question 
2. References of a high degree of relevance, the lack of which either would have made the research impracticable or would have resulted in a considerable amount of extra work 
3. References which were useful, either as general background to the work or as suggesting methods of tackling certain aspects of the work 
4. References of minimum interest, for example, those that have been included from an historical viewpoint 

Query-Reference pairs in which the reference is of no interest to the query are excluded from the relevance file. More on the Cranfield dataset: http://ir.dcs.gla.ac.uk/resources/test_collections/cran/

## PART- A1
Building the text processing module for the search engine that implements: 
- sentence segmentation 
- tokenization 
- stemming and lemmatization 
- stopword removal

## PART- A2
Implementing the Information Retrieval module using TF-IDF based Vector Space Model with the same dataset.

Implement the following evaluation metrics and analyse results: 
1. Precision @ k 
2. Recall @ k 
3. F-Score @ k 
4. Average Precision @ k 
5. nDCG @ k






