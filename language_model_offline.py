from tokenizer import tokenize
from tokenizer import ngram_counter
from evaluation import perplexity
from text_processing import train_test_samples
from lm import lm
import pickle 

def save_pickle(obj, filename):
    with open(filename, 'wb') as f:  
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    health_corpus = []
    with open('dataset/Health_English.txt', 'r') as fp:
        while True:
            line = fp.readline() 
            #print(line)
            health_corpus.append(line.rstrip('.\n'))
            if not line: 
                break
    
    tech_corpus = []
    with open('dataset/technical_domain_corpus.txt', 'r') as fp:
        while True:
            line = fp.readline() 
            #print(line)
            tech_corpus.append(line.rstrip('.\n'))
            if not line: 
                break

    health_corpus = health_corpus[0:300]
    tech_corpus = tech_corpus[0:300]


    # Prepare train and test 
    health_corpus,health_test_corpus =  train_test_samples(health_corpus,n=100)
    tech_corpus,tech_test_corpus =  train_test_samples(tech_corpus,n=100)


    health_lm = lm(ngram_type=4)
    health_lm.fit(corpus=health_corpus)

    save_pickle(health_lm,'trained_models/health_lm.obj')

    # Tech corpus
    tech_lm = lm(ngram_type=4)
    tech_lm.fit(corpus=tech_corpus)

    save_pickle(tech_lm,'trained_models/tech_lm.obj')

   
    ######################################################################## Part 2 assignment 
    ### 2.a
    ### Perplexity on train corpus

    ## 
    ## Calculate 
    perplexity_train_health = perplexity(health_lm,test_corpus=health_corpus)
    print("Perplexity of health train corpus sent")
    print(perplexity_train_health)
    avg_px_train_health = sum(perplexity_train_health)/len(perplexity_train_health)
    print("avg_perplexity_train_health {}".format(avg_px_train_health))
    # Sentence TAB perplexity-score, at the end , average score
    
    f = open('report/2020900039-LM1-train-health-perplexity.txt','w')
    for i,val in enumerate(health_corpus):
        f.write(val+ "\t" + str(perplexity_train_health[i]) + '\n')
    f.write("Average perplexity" + '\t' + str(avg_px_train_health) + '\n')
    f.close()

    perplexity_train_tech = perplexity(tech_lm,test_corpus=tech_corpus)
    print("Perplexity of tehcnical train corpus sent")
    print(perplexity_train_tech)
    avg_px_train_tech = sum(perplexity_train_health)/len(perplexity_train_tech)

    f = open('report/2020900039-LM1-train-technical-perplexity.txt','w')
    for i,val in enumerate(tech_corpus):
        f.write(val+ "\t" + str(perplexity_train_tech[i]) + '\n')
    f.write("Average perplexity" + '\t' + str(avg_px_train_tech)+ '\n')
    f.close() 

    ### 2.2
    ### Perplexity on test corpus at sentance level
    # print(health_corpus[0:10])           
    #health_test_corpus = random_samples(health_corpus,n=len(tech_corpus))
    perplexity_test_health = perplexity(health_lm,test_corpus=health_test_corpus)
    print("Perplexity of health testcorpus sentances")
    print(perplexity_test_health)
    avg_px_test_health = sum(perplexity_test_health)/len(perplexity_test_health)


    f = open('report/2020900039-LM1-test-health-perplexity.txt','w')
    for i,val in enumerate(health_test_corpus):
        f.write(val+ "\t" + str(perplexity_test_health[i]) + '\n')
    f.write("Average perplexity" + '\t' + str(avg_px_test_health)+ '\n')
    
    f.close()


    #tech_test_corpus = random_samples(tech_corpus,n=len(tech_corpus))
    perplexity_test_tech = perplexity(tech_lm,test_corpus=tech_test_corpus)
    print("Perplexity of tech test corpus sentances")
    print(perplexity_test_tech)
    avg_px_test_tech = sum(perplexity_test_tech)/len(perplexity_test_tech)

   
    f = open('report/2020900039-LM1-test-technical-perplexity.txt','w')
    for i,val in enumerate(tech_test_corpus):
        f.write(val+ "\t" + str(perplexity_test_health[i]) + '\n')
    f.write("Average perplexity" + '\t' + str(avg_px_test_health)+ '\n')
    
    f.close()

  