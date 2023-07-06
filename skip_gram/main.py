from coocurrence_matrix import compute_coocurrence_matrix, get_most_probable_next_word


ocurrence_matrix = compute_coocurrence_matrix()


first_word = "black"

next_words = [first_word]

counter = 0

while next_words[-1] != 0 and counter<10:
    next_words.append(get_most_probable_next_word(next_words[-1], ocurrence_matrix))
    counter += 1 

sentence = " ".join(next_words)

print(f" {sentence}  ")