

import pandas as pd

import csv

def get_data(filename):
    
    df = []
    with open(filename, "r", encoding='ISO-8859-1') as f:
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

def probability(counted):
    list_to_csv_1 =[]
    for key, value in counted.items():
        all_count = 0
        for counts in value:
            (word, count) = counts
            all_count += count
        for counts in value:
            (word, count) = counts
            list_to_csv = []
            list_to_csv.append(word)
            list_to_csv.append(count)
            list_to_csv.append(key)
            list_to_csv.append(all_count)
            list_to_csv_1.append(list_to_csv)

    df = pd.DataFrame.from_records(list_to_csv_1)
    pd.DataFrame.from_records(df).to_excel('word-count-key.xlsx',encoding='utf8',index=False)



def main():
    df = get_data('cleaned-v2.csv')
    df_2 = bag_of_words(df)
    df_3 = counting(df_2)
    probability(df_3)

if __name__ == '__main__':
    main()