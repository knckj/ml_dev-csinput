


from unicodedata import category
import pandas as pd

import csv

def get_data(filename):
    
    df = []
    with open(filename, "r", encoding='utf8') as f:
        f_reader = csv.reader(f, delimiter=';')
        
        for row in f_reader:
            df.append(row)
    return df

def bag_of_words(input_df):
    
    bag_word_cat = {}   

    for customer_input, category in input_df:
        bag_word = []
        splitted_cs = customer_input.split()
        bag_word.extend(splitted_cs)
        if category not in bag_word_cat.keys():
            bag_word_cat.update({category:bag_word})
        else:
            bag_word_cat[category].extend(bag_word)
    
    return bag_word_cat

def counting(input_dict):
    counted = {}
    input_dict.pop("category")
    for key, value in input_dict.items():
        no_duplicates_values = set((value))
        for word in no_duplicates_values:
            counts = value.count(word)
            word_counts = (word, counts)
            if key not in counted.keys():
                counted.update({key:[word_counts]})
            else:
                counted[key].append(word_counts)
    return counted


def main():
    df = get_data('cleaned-dalej.csv')
    df_2 = bag_of_words(df)
    counting(df_2)

if __name__ == '__main__':
    main()