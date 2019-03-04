import docIndex as d

import math


def norm(data):
    sum = 0
    for x in data:
        sum += x ** 2
    

    return math.sqrt(sum)
def dot_product(q, d):

    g = sum([x*y for x,y in zip(q,d)])
    return g


def main():
  
    doc = d.read_collection('ap89_collection')
    documents = doc[0]
    
    queries = d.read_query()
    data2 = d.query_execution(queries[0])
    data = d.query_execution2(documents)
    

    cs = list ()
    for j in range(len(data2)):
        temp = []
        for i in range(len((data[0]))):
            try:    
                query_norm = norm(data2[j])
                document_norm = norm(data[j][i])
                dp = dot_product(data2[j], data[j][i])
                p = query_norm * document_norm
                cosine_similarity = (dp)/p
                temp.append((cosine_similarity, i))
            except:
                pass
        
        cs.append(temp)
    
    cs[0].sort(reverse=True)
    
    #<query−number> Q0 <docno> <rank> <score> Exp
    q = d.read_query()
    query_num = q[1]
    
    doc_no = doc[1]
    
    for i in cs:
        i.sort(reverse=True)
        filename = 'results_file'+str(cs.index(i)+1)+'.txt'
        f = open(filename, "w")
        for j in range(len(cs)):
            no = i[j][1]
            
            score = (i[j][0])
            qn = query_num[cs.index(i)]
            

            f.write(str(qn) + ' ' + 'Q0' + ' ' + str(doc_no[no]) + ' ' + str(j) + ' ' + str(score) + ' ' + 'Exp' '\n')


      
if __name__ == "__main__":
    main()
