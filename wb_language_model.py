from witten_bell import lm
from evaluation import perplexity
   
ex = ["Hello how are Hello","Hello I am doing good"]
test = ["Hello how are you "]
lm = lm(ngram_type=4)
lm.fit(corpus=ex)

perplexity(lm,test_corpus=ex)
#print("Perplexity is {}".format(perplexity(lm,test_corpus=test)))


