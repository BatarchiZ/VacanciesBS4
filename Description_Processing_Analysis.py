from bs4 import BeautifulSoup
import requests
import ProcessingFunctions as fnP
import AnalysisFunctions as fnA
import GetSimilarFunctions as fnGS

r = open("Results.txt", 'w+')

# Getting the vacancies.txt
f = open("Vacancies.txt", "w+")
texts = []
counter = 0
base_url = 'https://career.habr.com'
number = 0



for i in range(4):
    page = requests.get('https://career.habr.com/vacancies?page={}&type=all'.format(i))
    soup = BeautifulSoup(page.content, 'html.parser')
    for link in soup.find_all("a", {"class", "vacancy-card__icon-link"}):

            print(number, file=f)
            number +=1
            print(base_url + link["href"], file=f)
            career_link = requests.get(base_url+link["href"])
            borsch = BeautifulSoup(career_link.content, 'html.parser')

            print(borsch.find("div", "job_show_description__body").text ,file=f)
            texts.append(borsch.find('div','job_show_description__body').text)
            print("|"*50, file=f)
            print("|"*50, file=f)
            print("|"*50, file=f)
            print("|"*50, file=f)
            counter+=1
print(counter)
print(len(texts))


"""Natasha Processing and analysis"""
pre_texts = list(map(fnP.preprocessNatasha, texts))
DICT = {key: i for i, key in enumerate(set(sum(pre_texts, [])))}

matrix = []
for text in pre_texts:

    _x = [0] * len(DICT)
    for word in text:
        _x[DICT[word]] += 1
    matrix.append(_x)

# Natasha Analysis:


print('Document Start',file=r)
print("|"*100, file=r)
print('Natasha ANALYSIS( Page Index : Similarity Value)', file=r)
print('-'*35,file =r)
print('Euclidean Similarity:',file=r)
for i in range(1, len(matrix)):
    print(i,' : ', fnA.Euclidean_similarity(matrix[0], matrix[i]), file=r)
print('-'*35,file =r)
print('Hamming Similarity:',file=r)
for i in range(1, len(matrix)):
    print(i,' : ',  fnA.Hamming_similarity(matrix[0], matrix[i]), file=r)
print('-'*35,file =r)
print('Cosine Similarity:',file=r)
for i in range(1, len(matrix)):
    print(i,' : ',  fnA.Hamming_similarity(matrix[0], matrix[i]), file=r)
#Natasha Results:
print('-'*35,file =r)
print('Three similar Euclidean webpage indexes are:',fnGS.get3EuclideanSimilar(matrix),file=r)
print('Three similar Hamming webpage indexes are:', fnGS.get3Hammingsimilar(matrix),file=r)
print('Three similar Cosine webpage indexes are:', fnGS.get3CosineSimilar(matrix),file=r)



"""Re Processing and analysis:"""
re_lists = []
for i in texts:
    fnP.preprocessRe(i)
    re_lists.append(list(i.split()))

DICT = {key: i for i, key in enumerate(set(sum(re_lists, [])))}

matrix = []
for text in re_lists:

    _x = [0] * len(DICT)
    for word in text:
        _x[DICT[word]] += 1
    matrix.append(_x)

# Re Analysis
print("|"*100, file=r)
print("|"*100, file=r)
print('Re ANALYSIS( Page Index : Similarity Value)', file=r)
print('-'*35,file =r)
print('Euclidean Similarity:',file=r)
for i in range(1, len(matrix)):
    print(i,' : ', fnA.Euclidean_similarity(matrix[0], matrix[i]), file=r)
print('-'*35,file =r)
print('Hamming Similarity:',file=r)
for i in range(1, len(matrix)):
    print(i,' : ',  fnA.Hamming_similarity(matrix[0], matrix[i]), file=r)
print('-'*35,file =r)
print('Cosine Similarity:',file=r)
for i in range(1, len(matrix)):
    print(i,' : ',  fnA.Hamming_similarity(matrix[0], matrix[i]), file=r)
#Re Results:
print('-'*35,file =r)
print('Three similar Euclidean webpage indexes are:',fnGS.get3EuclideanSimilar(matrix),file=r)
print('Three similar Hamming webpage indexes are:', fnGS.get3Hammingsimilar(matrix),file=r)
print('Three similar Cosine webpage indexes are:', fnGS.get3CosineSimilar(matrix),file=r)

"""Python Processing and analysis:"""
Python_lists = []
for i in texts:
    fnP.preprocessPython(i)
    Python_lists.append(list(i.split()))
DICT = {key: i for i, key in enumerate(set(sum(Python_lists, [])))}

matrix = []
for text in Python_lists:

    _z = [0] * len(DICT)
    for word in text:
        _z[DICT[word]] += 1
    matrix.append(_z)

# Python Analysis
print("|"*100, file=r)
print("|"*100, file=r)
print('Python ANALYSIS( Page Index : Similarity Value)', file=r)
print('-'*35,file =r)
print('Euclidean Similarity:',file=r)
for i in range(1, len(matrix)):
    print(i,' : ', fnA.Euclidean_similarity(matrix[0], matrix[i]), file=r)
print('-'*35,file =r)
print('Hamming Similarity:',file=r)
for i in range(1, len(matrix)):
    print(i,' : ',  fnA.Hamming_similarity(matrix[0], matrix[i]), file=r)
print('-'*35,file =r)
print('Cosine Similarity:',file=r)
for i in range(1, len(matrix)):
    print(i,' : ',  fnA.Hamming_similarity(matrix[0], matrix[i]), file=r)
#Python results:
print('-'*35,file =r)
print('Three similar Euclidean webpage indexes are:',fnGS.get3EuclideanSimilar(matrix),file=r)
print('Three similar Hamming webpage indexes are:', fnGS.get3Hammingsimilar(matrix),file=r)
print('Three similar Cosine webpage indexes are:', fnGS.get3CosineSimilar(matrix),file=r)

