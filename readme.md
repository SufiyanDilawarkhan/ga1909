Python Editiors for Pushing Code to Production

spyder
pycharm
Vscode
Atom
Not jupyter

We should use function
-- makes code Reusable

Never use keywords as function name, variable name
dont use single letter variable name (example, a, b, x, y, etc.)
Variable names and function names which convey the meaning of it

This makes our code more Readable

technical debt

Code should always contain documentation

Docstring to each function, class, modules
Avoid inline comments as much as possible

Maintainable

Explainability
 -- how easy it is to understand the code in terms of logic
 -- how easy it is to understand the code in terms of machine learning
 
Scalability
-- vertical scalability -- add more ram and harddisk to the same laptop or add GPU
-- horizontal scalability -- add a new laptop

Assume 4GB RAM, 1TB HD, 4 Core CPU laptop
ML model with 10000 datapoints
ML model with 1Million datapoints
We need to scale our infrastructure

Modular Structure
Use of modules(multiple code files), classes and functions

path, config should be written in a seperate config file

Assignment - Take any past project check it for pep8 compliance check for issues and remove all those issues

Empirical logic to find summary 
Split the sentence and use first sentence and find the top 5 sentences with maximum number of words among the rest
Document summarization
ga1909
	/bin
    - preprocessor.py
	    Class ProcessDoc
			functions
			- special char removal
			- tokenization
			- stopword removal
	- summarizer.py
        Class SummarizeDoc
			functions
			- readDocs
			- loadConfig
			- splitter
			- groupSentence
			- findNumWords
			- findTop3Sent
			- sentenceCombiner
		
relative paths		
		
		