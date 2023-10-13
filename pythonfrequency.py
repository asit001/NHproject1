def word_frequency(file_path):
    with open(file_path, 'r') as file:
        content = file.read().lower()
        words = content.split()

    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

file_path = 'your_file_path.txt'
word_freq = word_frequency(file_path)

for word, freq in word_freq.items():
    print(f'{word}: {freq}')
