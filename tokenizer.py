# Gets a sentence and returns tokens with n-grams
import time
#class Tokenizer():
def tokenize(corpus,num_tokens=1):
    
    #print("Tokenizing text for {} grams".format(num_tokens))
    ngrams_corpus = []

    # For each sentence in corpus
    #i=0
    for sent in corpus:
        #print(sent)
        #i=i+1
        #print(corpus.index(sent))
        token_list = ['<s>']
        for i in sent.split():
            token_list.append(i)
        token_list.append('</s>')
        ngrams = []
        #print(token_list)

        #ngrams.append('<s>')
        # Create n grams 
        if(num_tokens==1):
            ngrams = token_list
            #print(ngrams)

        elif(num_tokens==2):
            #print(token_list)
            for i,v in enumerate(token_list):
                #print(i)
                if(i<len(token_list)-1):
                    ngrams.append((token_list[i],token_list[i+1]))

        elif(num_tokens==3):
            #print(token_list)
            for i,v in enumerate(token_list):
                #print(i)
                if(i<len(token_list)-2):
                    ngrams.append((token_list[i],token_list[i+1],token_list[i+2]))

        elif(num_tokens==4):
            #print(token_list)
            for i,v in enumerate(token_list):
                #print(i)
                if(i<len(token_list)-3):
                    ngrams.append((token_list[i],token_list[i+1],token_list[i+2],token_list[i+3]))
        
        #ngrams.append('</s')
        ngrams_corpus.append(ngrams)

    #print("No. of ngrams found {}".format(len(ngrams_corpus)))
    return(ngrams_corpus)

def ngram_counter(ngrams):
    #print("Counting ngrams")

    # Unnest to a single list
    ngrams = sum(ngrams,[])
    print("No. of ngrams found {}".format(len(ngrams)))
    print(ngrams)

    # Count all ngrams
    print("Creating dictionary count")
    
    #%timeit
    ngrams_counts = dict((x,ngrams.count(x)) for x in set(ngrams))
    #ngrams_counts = {x,ngrams.count(x) for x in ngrams)}
    
    

    # Sort in descending order
    
    print("Sorting dictionary")
    sorted_list = sorted(ngrams_counts.items(), key=lambda item: item[1],reverse=True)    
    ngrams_counts=  {k: v for k, v in sorted_list}

   
    return(ngrams_counts)




################################################## Debugging
# ex = ["Hello how are Hello how are you","Hello I am doing good"]
# #ex = ["Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences, a paragraph is half a page long, etc. In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph. A paragraph is defined as “a group of sentences or a single sentence that forms a unit”. Length and appearance do not determine whether a section in a paper is a paragraph. For instance, in some styles of writing, particularly journalistic styles, a paragraph can be just one sentence long. Ultimately, a paragraph is a sentence or group of sentences that support one main idea. In this handout, we will refer to this as the “controlling idea,” because it controls what happens in the rest of the paragraph."]
   
# ngrams = tokenize(ex,2)
# print(ngrams)
# print(ngram_counter(ngrams))
#ngram_counts = ngram_counter(ngrams)
# ngrams = tokenize(ex,2)
# #print(ngrams)
# print(ngram_counter(ngrams))

# ngrams = tokenize(ex,1)
# #print(ngrams)
# print(ngram_counter(ngrams))

# bigram = "paragraph is"
# print("Bigrams found in")
# print(list(filter(lambda x:bigram.split()[0] in x and bigram.split()[1] in x and bigram.split()[0], ngram_counts)))

