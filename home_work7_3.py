import string
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                item = [str(i) for i in file]
                y = ','.join(item)
                y = y.translate(str.maketrans('', '', string.punctuation))
                y = y.split()
                all_words[item] = y
        return (all_words)

    def find(self, word):
        self.word = word.lower()
        file_dict = self.get_all_words()
        file_dict_lower = {key: [item.lower() for item in file_dict[key]] for key in file_dict}
        for key, value in file_dict_lower.items():
            if self.word in value:
                value_find = value.index(self.word) + 1
                return {key: value_find}
    def count(self, word):
        self.word = word.lower()
        file_dict = self.get_all_words()
        file_dict_lower = {key: [item.lower() for item in file_dict[key]] for key in file_dict}
        for key, value in file_dict_lower.items():
            if self.word in value:
                return {key: value.count(self.word)}



finder2 = WordsFinder('test_file.txt', 'Mother Goose - Monday’s Child.txt')
print(finder2.get_all_words())
print(finder2.find('TExt'))
print(finder2.count('CHild'))