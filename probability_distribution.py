from math import factorial, exp, sqrt, pi

grades = [65, 61, 81, 88, 69, 89, 55, 84, 86, 84, 71, 81, 84, 81, 78, 67, 96, 66, 73, 75, 59, 71, 69, 63, 79, 76, 63,
          85, 87, 88, 80, 71, 65, 84, 71, 75, 81, 79, 64, 65, 84, 77, 70, 75, 84, 75, 73, 92, 90, 79, 80, 71, 73, 71,
          58, 79, 73, 64, 77, 82, 81, 59, 54, 82, 57, 79, 79, 73, 74, 82, 63, 64, 73, 69, 87, 68, 81, 73, 83, 73, 80,
          73, 73, 71, 66, 78, 64, 74, 68, 67, 75, 75, 80, 85, 74, 76, 80, 77, 93, 70, 86, 80, 81, 83, 68, 60, 85, 64,
          74, 82, 81, 77, 66, 85, 75, 81, 69, 60, 83, 72]


def make_dictionary():
    dictionary = {}
    for i in grades:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary

def number_of_members(dict):
    n = 0
    for i in dict:
        n += dict[i]
    return n

def probability(x):
    n = number_of_members(dictionary)
    m = 0
    if x in dictionary:
        m = dictionary[x]
    q = m/n
    return q

def Multinomial_distribution(dict):
    md = 1
    n = number_of_members(dict)
    for j in dict:
        p = probability(j)
        md *= (p**dict[j])/factorial(dict[j])
    md *= factorial(n)
    return md

def mean(dict):
    m = 0
    n = number_of_members(dict)
    for j in dict:
        m += (j*dict[j])
    M = m/n
    return M

def variance(dict):
    m = 0
    n = number_of_members(dict)
    for j in dict:
        m += dict[j]*((j-mean(dict))**2)
    V = m/(n-1)
    return V

def normal_distribution(x, mean, variance):
    exponent = exp(-((x-mean)**2)/(2*variance))
    N = (1/sqrt(2*pi*variance))*exponent
    return N


if __name__ == '__main__':
    dictionary = make_dictionary()
    dictionary1 = {71: 2, 65: 1, 83: 1, 90: 1}
    print("dictionary:", dictionary)
    print("Multinomial distribution for grades=[71,71,65,83,90] is:", Multinomial_distribution(dictionary1))
    print("normal distribution for 75 is:", normal_distribution(75, mean(dictionary), variance(dictionary)))