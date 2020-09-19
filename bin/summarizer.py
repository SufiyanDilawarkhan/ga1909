# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 13:13:32 2020

@author: sufiy
"""
import yaml
import numpy as np

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
        
    def findSentLength(self,text):
        return text.split()
    
    def findSentLengthArray(self,sentences):
        return [self.findSentLength(sent) for sent in sentences]
    
    def findTopSentences(self,sentLengths,sentences,n):
        sortedIdx = np.argsort(sentLengths)
        topnIdx = sortedIdx[-n:]
        topnSentences = [sentences[i] for i in top3Idx]
        return topnSentences
    
    def findSummary(self):
        filePath = self.config['data_path']['train_data']
        text = self.loadDocs(filePath)
        sentences = self.splitSentences(text)
        firstSent,restOfSent = self.groupSentences(sentences)
        sentLengths = self.findSentLengthArray(restOfSent)
        topnSentences = self.findTopSentences(sentLengths,restOfSent,self.config['sent_num'])
        allSentences = [firstSent] + topnSentences
        summary = ' '.join(allSentences)
        return summary
        
summarizeObj = SummarizeDoc()
summarizeObj.loadConfig()