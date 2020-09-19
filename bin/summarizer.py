# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 13:13:32 2020

@author: sufiy
"""
import yaml

class SummarizeDoc:
    
    def __init__(self):
        with open('../config/config.yml','r') as fl:
            self.config = yaml.load(fl)
            
    
    def loadDocs(self,filePath):
#       with open('C:\Users\sufiy\Desktop\Data_Science\Deployment_GreyAtom\Session_2\gatut1909\data\train') #Never hard code like this
        with open(filePath,'r') as fl:
            text = fl.read()
        return text
        
    def splitSentences(self,text):
        """
        Split paragraph into an array of sentences
        
        Input:
            text: string
        Output:
            sentences: a list of string
        """
        sentences = text.split('.')
        return sentences
    
    def groupSentences(self,sentences):
        firstSent, restOfSent = sentences[0], sentences[1:]
        return firstSent, restOfSent
    
    def firstSentExtractor(self):
        pass
    
    def findNumWords(self):
        pass
    
    def findTop3Sent(self):
        pass
    
    def sentenceCombiner(self):
        pass
    
summarizeObj = SummarizeDoc()
summarizeObj.loadConfig()