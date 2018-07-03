
# coding: utf-8

# In[9]:


import pandas as pd

class Preprocessor:
    
    def __init__(self):
        self.tokenlist = []
        
    def __str__(self):
        s = ('the length of the list is:' + str(len(self.tokenlist)))
        return s
    
    def tokenise(self, input_sequence):
        
        #creating the tokenised list
        for seq in input_sequence:
            a = seq.split(' ')
            for seq1 in a:
                self.tokenlist.append(seq1)            
        
        
    def get_tokenised_list(self):
        
        return self.tokenlist
    
# TASK 2 BEGINS

class CharacterAnalyser(Preprocessor):
    
    def __init__(self):
        Preprocessor.__init__(self)
        self.counts = pd.DataFrame()
        
    def analyse_characters(self, tokenised_list):
        
        #taking one word at a time
        b = []
        for seq in tokenised_list:
            b.append(list(seq))
        
        #Extracting all characters from a word 
        v = []
        for i1 in b:
            for i2 in i1:
                v.append(i2)

        import pandas as pd
        my_series = pd.Series(v)

        # Using Value counts to calculate the frequency
        count = my_series.value_counts()     
        self.counts = count.to_frame()
        
        return(self.counts)
    
    def get_punctuation_frequency(self):
            
        punc = []
        #if the chosen index is a punctuation, it is appended to the punc list
        for index1 in self.counts.index.tolist(): 
            if index1 not in list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'):
                punc.append(index1)
        #selecting all rows where the index belongs to punc list
        self.puncount = self.counts.loc[punc]
        return self.puncount

# TASK 3 BEGINS

class WordAnalyser(CharacterAnalyser):
    
    def __init__(self):
        CharacterAnalyser.__init__(self)
        self.wordcount = pd.DataFrame()
        
    def analyse_words(self, tokenised_list):
        
        my_series = pd.Series(tokenised_list)
        # Calculate the frequency off all the words
        self.wordcount1 = my_series.value_counts()
        self.wordcount = self.wordcount1.to_frame()
    
    def get_stopword_frequency(self):
        
        a = str('a about above across after again against all almost alone along already also although always among an and another any anybody anyone anything anywhere are area areas around as ask asked asking asks at away b back backed backing backs be became because become becomes been before began behind being beings best better between big both but by c came can cannot case cases certain certainly clear clearly come could d did differ different differently do does done down down downed downing downs during e each early either end ended ending ends enough even evenly ever every everybody everyone everything everywhere f face faces fact facts far felt few find finds first for four from full fully further furthered furthering furthers g gave general generally get gets give given gives go going good goods got great greater greatest group grouped grouping groups h had has have having he her here herself high high high higher highest him himself his how however i if important in interest interested interesting interests into is it its itself j just k keep keeps kind knew know known knows l large largely last later latest least less let lets like likely long longer longest m made make making man many may me member members men might more most mostly mr mrs much must my myself n necessary need needed needing needs never new new newer newest next no nobody non noone not nothing now nowhere number numbers o of off often old older oldest on once one only open opened opening opens or order ordered ordering orders other others our out over p part parted parting parts per perhaps place places point pointed pointing points possible present presented presenting presents problem problems put puts q quite r rather really right right room rooms s said same saw say says second seconds see seem seemed seeming seems sees several shall she should show showed showing shows side sides since small smaller smallest so some somebody someone something somewhere state states still still such sure t take taken than that the their them then there therefore these they thing things think thinks this those though thought thoughts three through thus to today together too took toward turn turned turning turns two u under until up upon us use used uses v very w want wanted wanting wants was way ways we well wells went were what when where whether which while who whole whose why will with within without work worked working works would x y year years yet you young younger youngest your yours z')
        b = a.split(' ')
        
        stopwordindf = []
        #selecting all the indexes which are stopwords from the self.wordcount dataframe
        for stopword in b:
            if stopword in self.wordcount.index.tolist():
                stopwordindf.append(stopword)
        
        #choosing the rows where a stopword is in index
        self.stopwordfreq = self.wordcount.loc[stopwordindf]
        return self.stopwordfreq
    
    def get_word_length_frequency(self):
        
        b = {}
        a = self.wordcount.index.tolist()
        # checking every element in index and using it's length 
        for i in a:
            if len(i) in b:
                b[len(i)] = b[len(i)]+1
            else:
                b[len(i)] = 1
                
        #Converting the dictionary into a dataframe        
        self.wordlengthfreq = pd.DataFrame.from_dict(b,orient = 'index')
        
        return self.wordlengthfreq

# TASK 4 BEGINS

class AnalysisVisualiser:
    
    def __init__(self):
        
        self.chcount = pd.DataFrame
        
    def visualise_character_frequency(self,chdataframe):
        
        
        self.chcount = chdataframe
        #Assigning column names
        self.chcount.columns = ['EDW','HAM','HEN1','HEN2','RIC','JEW']
        
        import matplotlib.pyplot as plt
                
        self.chcount.fillna(0,inplace = True)  
        #fillna replaces all Nan's with 0
        
        self.chcount = self.chcount.div(self.chcount.sum(axis=0),axis = 1)
        
        self.chcount.plot()
        #plt.show(block=True)

    def visualise_punctuation_frequency(self,pudataframe):
        import matplotlib.pyplot as plt
        
        self.punccount = pudataframe
        self.punccount.columns = ['EDW','HAM','HEN1','HEN2','RIC','JEW']
        
        self.punccount.fillna(0,inplace = True)
        self.punccount = self.punccount.div(self.punccount.sum(axis=0),axis = 1)
        
        self.punccount.plot()
        #plt.show(block=True)
        
    def visualise_stopword_frequency(self,stdataframe):
        import matplotlib.pyplot as plt
        
        self.stopwordfreq = stdataframe
        self.stopwordfreq.columns = ['EDW','HAM','HEN1','HEN2','RIC','JEW']
        
        self.stopwordfreq.fillna(0,inplace = True)
        self.stopwordfreq = self.stopwordfreq.div(self.stopwordfreq.sum(axis=0),axis = 1)
        
        self.stopwordfreq.plot()
        #plt.show(block=True)
   
    def visualise_get_word_length_frequency(self,wordlndataframe):
        
        self.wordlengthfreq = wordlndataframe
        #self.wordlengthfreq.columns = ['EDW','HAM','HEN1','HEN2','RIC','JEW']
        
        self.stopwordfreq.fillna(0,inplace = True)
        self.wordlengthfreq = self.wordlengthfreq.div(self.wordlengthfreq.sum(axis=0),axis = 1)
        
        self.wordlengthfreq.plot()

# TASK 5 BEGINS        

# read_input function to read all the six input files        
def read_input():    
    return [[line.rstrip('\n') for line in open('Edward_II_Marlowe.tok','r')],
    [line.rstrip('\n') for line in open('Hamlet_Shakespeare.tok','r')],
    [line.rstrip('\n') for line in open('Henry_VI_Part2_Shakespeare.tok','r')],
    [line.rstrip('\n') for line in open('Henry_VI_Part1_Shakespeare.tok','r')],
    [line.rstrip('\n') for line in open('Richard_II_Shakespeare.tok','r')],
    [line.rstrip('\n') for line in open('Jew_of_Malta_Marlowe.tok','r')]]

def main():

    # initializing objects
    lines,lines1,lines2,lines3,lines4,lines5 = read_input()
    
    # calling class wordanalyser six times for each file
    q1 = WordAnalyser()
    q21 = q1.tokenise(lines)
    q31 = q1.get_tokenised_list()
    q41 = q1.analyse_characters(q31)
    q51 = q1.get_punctuation_frequency()
    q61 = q1.analyse_words(q31)
    q71 = q1.get_stopword_frequency()
    q81 = q1.get_word_length_frequency()

    q2 = WordAnalyser()
    q22 = q2.tokenise(lines1)
    q32 = q2.get_tokenised_list()
    q42 = q2.analyse_characters(q32)
    q52 = q2.get_punctuation_frequency()
    q62 = q2.analyse_words(q32)
    q72 = q2.get_stopword_frequency()
    q82 = q2.get_word_length_frequency()


    q3 = WordAnalyser()
    q23 = q3.tokenise(lines2)
    q33 = q3.get_tokenised_list()
    q43 = q3.analyse_characters(q33)
    q53 = q3.get_punctuation_frequency()
    q63 = q3.analyse_words(q33)
    q73 = q3.get_stopword_frequency()
    q83 = q3.get_word_length_frequency()

    q4 = WordAnalyser()
    q24 = q4.tokenise(lines3)
    q34 = q4.get_tokenised_list()
    q44 = q4.analyse_characters(q34)
    q54 = q4.get_punctuation_frequency()
    q64 = q4.analyse_words(q34)
    q74 = q4.get_stopword_frequency()
    q84 = q4.get_word_length_frequency()

    q5 = WordAnalyser()
    q25 = q5.tokenise(lines4)
    q35 = q5.get_tokenised_list()
    q45 = q5.analyse_characters(q35)
    q55 = q5.get_punctuation_frequency()
    q65 = q5.analyse_words(q35)
    q75 = q5.get_stopword_frequency()
    q85 = q5.get_word_length_frequency()

    q6 = WordAnalyser()
    q26 = q6.tokenise(lines5)
    q36 = q6.get_tokenised_list()
    q46 = q6.analyse_characters(q36)
    q56 = q6.get_punctuation_frequency()
    q66 = q6.analyse_words(q36)
    q76 = q6.get_stopword_frequency()
    q86 = q6.get_word_length_frequency()
    
    #Meging all the 6 character analysis dataframe
    q = pd.merge(q41,q42,how = 'outer',left_index=True, right_index=True)
    q = pd.merge(q,q43,how = 'outer',left_index=True, right_index=True)
    q = pd.merge(q,q44,how = 'outer',left_index=True, right_index=True)
    q = pd.merge(q,q45,how = 'outer',left_index=True, right_index=True)
    q = pd.merge(q,q46,how = 'outer',left_index=True, right_index=True)
    q.columns = ['EDW','HAM','HEN1','HEN2','RIC','JEW']
    q.sort_index(inplace=True)
    #print('the character counts of all the six files is')

    #Meging all the 6 punctuation analysis dataframe
    #print('the punctuation count of all six files is')
    p = pd.merge(q51,q52,how = 'outer',left_index=True, right_index=True)
    p = pd.merge(p,q53,how = 'outer',left_index=True, right_index=True)
    p = pd.merge(p,q54,how = 'outer',left_index=True, right_index=True)
    p = pd.merge(p,q55,how = 'outer',left_index=True, right_index=True)
    p = pd.merge(p,q56,how = 'outer',left_index=True, right_index=True)
    p.columns = ['EDW','HAM','HEN1','HEN2','RIC','JEW']
    p.sort_index(inplace=True)
    #print(p)

    #Merging all the 6 stopword analysis DataFrame
    #print('the stopword frequency count of six files is ')
    w = pd.merge(q71,q72,how = 'outer',left_index=True, right_index=True)
    w = pd.merge(w,q73,how = 'outer',left_index=True, right_index=True)
    w = pd.merge(w,q74,how = 'outer',left_index=True, right_index=True)
    w = pd.merge(w,q75,how = 'outer',left_index=True, right_index=True)
    w = pd.merge(w,q76,how = 'outer',left_index=True, right_index=True)
    w.columns = ['EDW','HAM','HEN1','HEN2','RIC','JEW']
    w.sort_index(inplace=True)
    #print(w)

    #the length frequency count of six files is 
    l = pd.merge(q81,q82,how = 'outer',left_index=True, right_index=True)
    l = pd.merge(l,q83,how = 'outer',left_index=True, right_index=True)
    l = pd.merge(l,q84,how = 'outer',left_index=True, right_index=True)
    l = pd.merge(l,q85,how = 'outer',left_index=True, right_index=True)
    l = pd.merge(l,q86,how = 'outer',left_index=True, right_index=True)
    l.columns = ['EDW','HAM','HEN1','HEN2','RIC','JEW']
    l.sort_index(inplace=True)
    
    c = AnalysisVisualiser()
    
    flag1 = 'Y'             # CREATING AN INITIAL FLAG(LOOP CONTINUES UNTIL FLAG VALUE IS CHANGED)
    while(flag1 == 'Y'):
        
        choice = int(input('Enter 1 for Character analysis, 2 for puctuation frequency analysis, 3 for stopword frequency analysis, 4 for word length analysis'))
        if choice == 1:
            print('the character frequency plot is')
            c.visualise_character_frequency(q)
        elif choice ==2:
            print('the punctuation word frequency plot is')
            c.visualise_punctuation_frequency(p)
        elif choice ==3:
            print('the stopword frequency plot is')
            c.visualise_stopword_frequency(w)
        elif choice ==4:    
            print('the word length frequency plot is')
            c.visualise_get_word_length_frequency(l)
        else:
            print('incorrect choice entered')
            
        flag2 = input("PRESS 'Y' or 'y' and enter key if there's plot visualization,Press anything else and enter key if no other code:")
        flag1 = flag2.upper()
        
if  __name__ == '__main__':
    main()

    


# In[ ]:




