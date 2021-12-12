def perplexity(lm,test_corpus):
    print(test_corpus)
    # For all words or ngrams in test set
    pinv_testset = []
    vocab_testset = []
    vocab_testset_size = len(set(vocab_testset))
    perplexity_test_sent = []
    
    for sent in test_corpus:
        pinv_sent = []
        #for word in sent.split():
        print(sent)
       # pinv_sent = [1/x for x in lm(sent)]

        if lm.predict(sent) == 0:
            pinv_sent = 0
        else:
            pinv_sent = 1/float(lm.predict(sent))

        pinv_testset.append(pinv_sent)

        print("Inverse prob {}".format(pinv_sent))

        vocab_size = len(set(sent.split()))
        #print(set(sent.split()))
        for word in sent:
            vocab_testset.append(word)
        print("Vocab size {}".format(vocab_size))

        if(pinv_sent == 0):
            perplexity_sent = float('inf') 
        else:
            perplexity_sent = vocab_size ** (1/pinv_sent)

        perplexity_test_sent.append(perplexity_sent)
        #print(perplexity_sent)


    #perplexity_testset = vocab_testset_size ** pinv_testset
    return(perplexity_test_sent)


def perplexity_corpus(lm,test_corpus):

    # For all words or ngrams in test set
    pinv_testset = []
    vocab_testset = []
    vocab_testset_size = len(set(vocab_testset))
    perplexity_test_sent = []

    for sent in test_corpus:
        pinv_sent = []
        #for word in sent.split():
        print(sent)
       # pinv_sent = [1/x for x in lm(sent)]
        pinv_sent = 1/float(lm.predict(sent))

        pinv_testset.append(pinv_sent)

        print("Inverse prob {}".format(pinv_sent))

        vocab_size = len(set(sent))
        for word in sent:
            vocab_testset.append(word)
        print("Vocab size {}".format(vocab_size))
        perplexity_sent = vocab_size ** (1/pinv_sent)
        perplexity_test_sent.append(perplexity_sent)
        #print(perplexity_sent)


    #perplexity_testset = vocab_testset_size ** pinv_testset
    return(perplexity_test_sent)


