"""
Programın çalışması için C dizini altında metin dosyaları ve input.txt dosyası bulunması gerekmektedir. 
"""
import os
import re

path = "C:\\"
temp_path = path
source = "input.txt"
receiver = "180401060_hw_1_output.txt"
data_text_list = os.listdir(path)
main_word_list = []
input_list = []
output_list = []
main_dict = dict()

for index in data_text_list:
    temp_path += index
    with open(temp_path, "r", encoding="utf-8") as r_file:
        word_list = [word for line in r_file for word in line.split()]
        i = 0
        for item in word_list:
            i += 1
            main_word_list.append(word_list[i-1])
    temp_path = path
main_text_length = len(main_word_list)

def add_word_dic(words_dict, word):
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

def find_dic_max(temp_dict):
    if not temp_dict:
        return " "
    return max(temp_dict, key=temp_dict.get)

def getNextText(text):
    words = text.split()
    word_len = len(words) 
    i = 0
    if word_len == 1:
        for iter in range(0, main_text_length-1):
            if main_word_list[iter] == words[i]:
                add_word_dic(main_dict, main_word_list[iter+1])
        output_list.append(find_dic_max(main_dict))
        main_dict.clear()
    elif word_len == 2:
        for iter in range(0, main_text_length-2):
            if main_word_list[iter] == words[i]:
                if main_word_list[iter+1] == words[i+1]:
                    add_word_dic(main_dict, main_word_list[iter+2])
        output_list.append(find_dic_max(main_dict))
        main_dict.clear()
    elif word_len == 3:
        for iter in range(0, main_text_length-3):
            if main_word_list[iter] == words[i]:
                if main_word_list[iter+1] == words[i+1]:
                    if main_word_list[iter+2] == words[i+2]:
                        add_word_dic(main_dict, main_word_list[iter+3])
        output_list.append(find_dic_max(main_dict))
        main_dict.clear()
    elif word_len == 4:
        for iter in range(0, main_text_length-4):
            if main_word_list[iter] == words[i]:
                if main_word_list[iter+1] == words[i+1]:
                    if main_word_list[iter+2] == words[i+2]:
                        if main_word_list[iter+3] == words[i+3]:
                            add_word_dic(main_dict, main_word_list[iter+4])
        output_list.append(find_dic_max(main_dict))
        main_dict.clear()
    elif word_len == 5:
        for iter in range(0, main_text_length-5):
            if main_word_list[iter] == words[i]:
                if main_word_list[iter+1] == words[i+1]:
                    if main_word_list[iter+2] == words[i+2]:
                        if main_word_list[iter+3] == words[i+3]:
                            if main_word_list[iter+4] == words[i+4]:
                                add_word_dic(main_dict, main_word_list[iter+5])
        output_list.append(find_dic_max(main_dict))
        main_dict.clear()
    else:
        output_list.append("Hatalı giriş: En fazla 5 kelime girmelisiniz..")

with open(source, "r", encoding="utf-8") as file:
    content = file.readlines()
    for item in content:
        input_list.append(item)
        getNextText(item)

for word in range(len(input_list)):
    input_list[word] = re.sub('\n', '', input_list[word])

with open(receiver, "w", encoding="utf-8") as file:
    for i in range(len(input_list)):
        file.write(input_list[i] + " - " + output_list[i] + "\n")
