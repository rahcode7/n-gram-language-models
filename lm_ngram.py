from tokenizer import tokenize
from tokenizer import ngram_counter
from evaluation import perplexity
   
class lm:
    def __init__(self,ngram_type=4):
        #self.corpus = corpus
        #self.ngram_type = ngram_type
        self.ngram_counts = {}
        self.mgrams_counts = {}
        self.ngrams = []
        self.mgrams = []
        self.ngram_type =ngram_type
        l = []

    def fit(self,corpus):
        # Tokenization of n-grams corpus
        self.ngrams = tokenize(corpus,self.ngram_type)
        print("{} grams tokens".format(self.ngram_type))
        self.ngrams_counts = ngram_counter(self.ngrams)
        print(self.ngrams_counts)

        # Context counts
        

        # tokenization of n-1 grams corpus
        self.mgrams = tokenize(corpus,self.ngram_type-1)
        print("{} grams tokens".format(self.ngram_type-1))
        self.mgrams_counts = ngram_counter(self.mgrams)
        print(self.mgrams_counts)


    def predict(self,sentance):
         #Get all ngrams and n-1 grams i.e m grams for the sentence
        print("predicting sentance {}".format(sentance))
        sent_ngrams = tokenize([sentance],self.ngram_type)
        sent_mgrams = tokenize([sentance],self.ngram_type-1)
        #print(sent_ngrams)
        #print(sent_mgrams)
        
        
        # Generate MLE/probability for the sentence
        #p('fresh breath ') = p('breath | fresh') = c('fresh' and 'breath' together)/ c('fresh')  
        #p('a b c ') = p(b | a)  *  p(c|b) = c(ab)/c(a) * c(bc)/c(b) 

        ngram_prob = []
        # For each ngram tuples, compute probability and multiple all probabilities to get prob of sentence
        for i in range(0,len(sent_ngrams[0])):
            #print("Ngrams {} and n-1 grams {}".format(sent_ngrams[0][i],sent_mgrams[0][i]))
            #print(i)
            #print(sent_ngrams[0][i])
            count_ab = 0
            count_a = 0

            if sent_ngrams[0][i] in self.ngrams_counts:
                count_ab = self.ngrams_counts[sent_ngrams[0][i]]
                
            if sent_mgrams[0][i] in self.mgrams_counts:
                count_a =  self.mgrams_counts[sent_mgrams[0][i]]
            
            if count_a ==0 or count_ab == 0:
                 prob_i = 0
            else:
                 prob_i = count_ab/count_a
            #print("Ngram count {} , n-1 gram count {} ,probability {}".format(count_a,count_ab,prob_i))
            ngram_prob.append(prob_i)

        total_prob = 1
        for i in ngram_prob:
            total_prob = total_prob*i

        print("Total probability {}".format(total_prob))
        return(total_prob)


#     # tokenization of n-2 grams corpus
#     lgrams = tokenize(corpus,ngram_type-2)
#     print("{} grams tokens",ngram_type-2)
#     lgrams_counts = ngram_counter(lgrams)
#     print(lgrams_counts)

#     grams = [lgrams,mgrams,ngrams]
#     gram_counts = [lgrams_counts,mgrams_counts,ngrams_counts]



#     # # Smoothing 
    # # p("a paragraph not") = p("not" | "a paragraph")  = max(ckn("a paragraph not")-d,0)/ckn("a paragraph") 
    # #
    # # 
    # # 
    # # 
    # #for i in range(0,len(sent_ngrams[0])):    
    # # If LM is trigram, 
    # def ckn_term(ngram_word,ngram_type)
    #     ckn = 0 
    #     d = 0.75


    #     cont_cnt = ngram_word.split()[:-1] # Take 



    #     if ngram_type=3:
    #         # for highest order
    #         count_ab = ngrams_counts[sent_ngrams[0][0]] 
           
    #         # if no match found for highest order, go to lower order to find
    #         #if count_ab == 0:
    #         #    ckn_term(ngram_word)

    #         ckn = count_ab
    #         d = 0 
    #     if ngram_type=2:
    #         count_a =  mgrams_counts[sent_mgrams[0][0]
    #         ckn = ckn_term(ngram_word) # Various word types before string   
    #            # All trigrams where "a paragraph" is the last word   / # All trigrams where "a" is the last word
            
    #     if ngram_type=1:
    #         count_a =  lgrams_counts[sent_lgrams[0][0]]
    #         ckn = continuation_count(ngram_word) 

    # return(ckn,d)

    # succeeding_count =    sent_mgrams[0][0]            # all trigrams that contains the bigram as first 2 words
    # lambda_wi= (d / count_a) * succeeding_count  # 0/(1+4)*  2 = 0

    # # P continuation probability    
    # p_cont = calculate_later / len(ngrams_count)  #no of different strings before final word among ngram type/length of ngram freq table or total ngram types


    # pkn = max(ckn(wi) - d,0)/ckn(wi_minus1) + lambda_wi * p_cont
    # return(pkn)

    
    # def kneser_key(vocab,counter):
    #     # Base case n=1 
    #     1.0 / len(vocab)


# corpus = ['The boy bought a chocolate','The girl got a chocholate','The girl ate a chocolate','the boy ate a ice cream']
# #lm("the boy ate a chocholate ")
# def kneser_smooth(corpus):
#     d = 0
#     count_ab = ngrams_counts[sent_ngrams[0][i]]
#     pkn = max(count_ab - d,0)
#     count_a =  mgrams_counts[sent_mgrams[0][i]]
 

    

