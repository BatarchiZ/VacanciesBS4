import AnalysisFunctions as fnA
#Matrix is the
def get3EuclideanSimilar(matrix:list)->list:
    list_of_Euclideans = []
    for i in range(1, len(matrix)):
        list_of_Euclideans.append(fnA.Euclidean_similarity(matrix[0], matrix[i]))

    keys = list(range(1, len(matrix)))
    dictionary = dict(zip(keys, list_of_Euclideans))
    maximum_similarity = []
    for i in range(3):
        max_value_number = max(dictionary, key=dictionary.get)
        maximum_similarity.append(max_value_number)
        del dictionary[max_value_number]

    return(maximum_similarity)

def get3CosineSimilar(matrix:list)->list:
    list_of_Cosine = []
    for i in range(1, len(matrix)):
        list_of_Cosine.append(fnA.Euclidean_similarity(matrix[0], matrix[i]))

    keys = list(range(1, len(matrix)))
    dictionary = dict(zip(keys, list_of_Cosine))
    maximum_similarity = []
    for i in range(3):
        max_value_number = max(dictionary, key=dictionary.get)
        maximum_similarity.append(max_value_number)
        del dictionary[max_value_number]
    return (maximum_similarity)
def get3Hammingsimilar(matrix:list)->list:

    list_of_Cosine = []
    for i in range(1, len(matrix)):
        list_of_Cosine.append(fnA.Euclidean_similarity(matrix[0], matrix[i]))

    keys = list(range(1, len(matrix) + 1))
    dictionary = dict(zip(keys, list_of_Cosine))
    maximum_similarity = []
    for i in range(3):
        max_value_number = max(dictionary, key=dictionary.get)
        maximum_similarity.append(max_value_number)
        del dictionary[max_value_number]
    return (maximum_similarity)