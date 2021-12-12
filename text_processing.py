import random


def train_test_samples(file,n):

    test_file = []
    index_remove = []
    train_file = []
    print("File random {}".format(len(file)))
    for i in range(n):
        index = random.randint(0,len(file)-1)
        
        test_file.append(file[index])
        index_remove.append(index)

    # for i in index_remove:s
    #     del file[i]
    print(len(index_remove))
    train_file = [val for i, val in enumerate(file) if i not in index_remove]
    
    return(train_file,test_file)


# if __name__ == '__main__':

#     health_corpus = []
#     with open('Health_English.txt', 'r') as fp:
#         while True:
#             line = fp.readline() 
#             #print(line)
#             health_corpus.append(line.rstrip('.\n'))
#             if not line: 
#                 break
    
#     #health_corpus[0:10] = health_corpus[0:10] 
#     print(len(health_corpus))          
#     train_file,test_file = train_test_samples(health_corpus,1000)
#     print(len(train_file))
#     print(len(test_file))


    
