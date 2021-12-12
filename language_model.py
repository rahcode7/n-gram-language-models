from tokenizer import tokenize
from tokenizer import ngram_counter
from evaluation import perplexity
#from text_processing import random_samples

import sys
import pickle
#print (sys.argv)


if __name__ == '__main__':
    sent = input('input sentence: ')  
    
    print(sent)
    
    health_file = open('trained_models/health_lm.obj', 'rb')   
    health_lm = pickle.load(health_file) 
    px = perplexity(health_lm,[str(sent)])
    print("Perplexity {}".format(px[0]))

    #Fresh breath and shining
    
                