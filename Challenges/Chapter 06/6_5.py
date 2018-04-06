words = ["The","fox","jumped","over","the","fence","."]

sentence = " ".join(words[:len(words)-1]) + words[len(words)-1]

print(sentence)
