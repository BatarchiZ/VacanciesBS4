def Euclidean_similarity(x:list,y:list)->float:
    _sum = 0
    for i in range(len(x)):
        _sum +=(x[i]-y[i])**2
        _sum **= 1/2
        try :
            ans = 1/_sum
        except ZeroDivisionError:
            ans = 0
    return ans

def Hamming_similarity(x:list, y:list)->int:
    _intersections = len(set(x)&set(y))
    return _intersections

def cos_similarity(x:list, y:list)->float:
    numerator = 0
    denominator = [0,0]
    for i in range(len(x)):
        numerator += x[i]*y[i]
        denominator[0]+=x[i]**2
        denominator[1]+=y[i]**2
    answer = numerator/((denominator[0]*denominator[1])**1/2)
    return answer
