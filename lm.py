from tokenizer import tokenize
from tokenizer import ngram_counter
from evaluation import perplexity
   
class lm:
    def __init__(self,ngram_type=4):
        self.fourgrams_counts= {}
        self.trigrams_counts= {}
        self.bigrams_counts= {}
        self.unigrams_counts= {}
        self.fourgrams = []
        self.trigrams = []
        self.bigrams = []
        self.unigrams = []
        self.ngram_type=ngram_type

        self.lamda_unigrams = {}
        self.lamda_bigrams = {}
        self.lamda_trigrams = {}

        self.prob_trigram_wb = 0
        self.prob_bigram_wb = 0
        self.prob_fourgram = 0

    def fit(self,corpus):
        # Tokenization of n-grams corpus
        self.fourgrams = tokenize(corpus,self.ngram_type)
        print("{} grams tokens".format(self.ngram_type))
        self.fourgrams_counts = ngram_counter(self.fourgrams)
        print(self.fourgrams_counts)


        # tokenization of n-3 grams corpus
        self.trigrams = tokenize(corpus,self.ngram_type-1)
        print("{} grams tokens".format(self.ngram_type-1))
        self.trigrams_counts = ngram_counter(self.trigrams)
        print(self.trigrams_counts)

		# tokenization of n-2 grams corpus
        self.bigrams = tokenize(corpus,self.ngram_type-2)
        print("{} grams tokens".format(self.ngram_type-2))
        self.bigrams_counts = ngram_counter(self.bigrams)
        print(self.bigrams_counts)


		 # tokenization of unigrams grams corpus
        self.unigrams = tokenize(corpus,self.ngram_type-3)
        print("{} grams tokens".format(self.ngram_type-3))
        self.unigrams_counts = ngram_counter(self.unigrams)
        print(self.unigrams_counts)


		# For all unique unigrams
        
        for uni in set(self.unigrams_counts):
            context_c = 0
            for bi in self.bigrams_counts:
                    if uni in bi[0]: 
                        context_c +=1  
            lamda_uni = 1 - context_c/(context_c+ self.unigrams_counts[uni])
            self.lamda_unigrams[uni] = lamda_uni
        #print("Lambda Values - Unigrams")
        #print(self.lamda_unigrams)


		# For all unique bigrams
        #lamda_bigrams = {}
        for bi in set(self.bigrams_counts):
            context_c = 0
            for tri in self.trigrams_counts:
                    #print(bi)
                    #print(tri)
                    if bi[0] == tri[0] and bi[1] == tri[1]: 
                        context_c +=1  
            lamda_bi = 1 - (context_c/(context_c + self.bigrams_counts[bi]))
            self.lamda_bigrams[bi] = lamda_bi
        #print("Lambda Values - Bigrams")
        #print(self.lamda_bigrams)

        # For all unique trigrams
        #lamda_trigrams = {}
        for tri in set(self.trigrams_counts):
            context_c = 0
            #print(tri)
            for four in self.fourgrams_counts:
                    if tri[0] == four[0] and tri[1] == four[1] and tri[2] == four[2]: 
                        context_c  +=1  
            #print("Context c {}".format(context_c))
            lamda_tri = 1 - (context_c/(context_c+self.trigrams_counts[tri]))
            self.lamda_trigrams[tri] = lamda_tri
        #print("Lambda Values - Trigrams")
        #print(self.lamda_trigrams)

    def predict(self,sentance): # sentance is a string of a sentance
        
        #Get all ngrams and n-1 grams i.e m grams for the sentence
        print("predicting sentance")
        #print(sentance)
        sent_fourgrams = tokenize([sentance],4)

        #print("Predictve sentence 4grams")
        #print(sent_trigrams)
        #print(sent_fourgrams)
        
        wb_prob = []
        # For all 4 grams, get probability and multiply
        for fourgrams in sent_fourgrams[0]:
            #print("single 4 gram")
            #print(fourgrams)
            # Witten Bell probability
             #P(wi∣wi−1)=λwi−1 PML(wi∣wi−1)+(1−λwi−1)P(wi)
            print(fourgrams[0])
            uni = fourgrams[0]
            if uni in self.unigrams_counts:
                count_a =  self.unigrams_counts[uni]
            else:
                count_a = 0

            bi = (fourgrams[0],fourgrams[1])
            if bi in self.bigrams_counts:
                count_ab =  self.bigrams_counts[bi]
            else:
                count_ab = 0

            tri = (fourgrams[0],fourgrams[1],fourgrams[2])
            if tri in self.trigrams_counts:
                count_abc =  self.trigrams_counts[tri]
            else:
                count_abc = 0

            if fourgrams in self.fourgrams_counts:
                count_abcd =  self.fourgrams_counts[fourgrams]
            else:
                count_abcd = 0

            if uni in self.lamda_unigrams:
                self.prob_bigram_wb = self.lamda_unigrams[uni] * count_ab/count_a   + (1-self.lamda_unigrams[uni])* (count_a/sum(self.unigrams_counts.values()))
            else:
                self.prob_bigram_wb = 1 * (count_a/sum(self.unigrams_counts.values()))
            #print("Bigram WB prob {}".format(self.prob_bigram_wb))

            if bi in self.lamda_bigrams:
                self.prob_trigram_wb =self.lamda_bigrams[bi] * count_abc/count_ab +((1-self.lamda_bigrams[bi])* self.prob_bigram_wb)
            else:
                self.prob_trigram_wb = self.prob_bigram_wb
            #print("Trigram WB prob {}".format(self.prob_trigram_wb))

            if tri in self.lamda_trigrams:
                # print("tri {}".format(tri))
                # print("3gram score {}".format(self.prob_trigram_wb))
                # print("3gram lamda score {}".format(self.lamda_trigrams[tri]))
                # print("4gram score {}".format((1-self.lamda_trigrams[tri])* self.prob_trigram_wb))
                self.prob_fourgram =  self.lamda_trigrams[tri] * count_abcd/count_abc +((1-self.lamda_trigrams[tri])* self.prob_trigram_wb)
            else:
                self.prob_fourgram =  self.prob_trigram_wb
            #print("4gram WB prob {}".format(self.prob_fourgram))

            wb_prob.append(self.prob_fourgram)


        print("WB prob list for all 4 grams")
        print(wb_prob)
        total_prob = 1
        for i in wb_prob:
            total_prob = total_prob*i

        print("Total probability {}".format(total_prob))
        return(total_prob)

