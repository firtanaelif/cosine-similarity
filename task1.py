import re
import math
from collections import Counter


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    word = re.compile(r'\w+')
    words = word.findall(text)
    return Counter(words)


def get_result(content_a, content_b):
    text1 = content_a
    text2 = content_b

    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)

    cosine_result = get_cosine(vector1, vector2)
    return cosine_result
print("Python cosine similarity algorithm between two text file")
print("********************************************************")
f = open("text1.txt")
f2 = open("text2.txt")
print("Cosine similarity is calculating...")
print("********************************************************")
print("Cosine similarity result is: ")
print get_result(f.readline(), f2.readline())
print("********************************************************")
if get_result(f.readline(), f2.readline()) <= 0.5:
    print("Cosine similarity between two text file, very low.")
elif get_result(f.readline(), f2.readline()) >= 0.5:
    print("Cosine similarity between two text file, very high.")
