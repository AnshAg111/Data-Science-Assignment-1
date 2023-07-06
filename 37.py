# Write a Python program to reverse the order of words in a sentence while preserving the word order.

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

sentence = input("Write any sentence: ")
print("Reversed sentence:", reverse_sentence(sentence))