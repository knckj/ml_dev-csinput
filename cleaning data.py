import csv
import pandas as pd
import re
def get_data(filename):
    # df = pd.read_csv(filename,delimiter=';')
    df = []
    with open(filename, "r", encoding='utf8') as f:
        f_reader = csv.reader(f, delimiter=';')
        
        for row in f_reader:
            df.append(row)
            

    return df
def clean_data(dataframe, stopwords_filename):
    stop_words = []
    customerInputs_cleaned = []

    with open(stopwords_filename, "r", encoding='utf8') as stop_words_file:
        for line in stop_words_file:
            line = line.strip()
            stop_words.append(line)
    i = 0
    for customerInput, category in dataframe:
        i += 1
        print(customerInput)
        customerInput_clean = [word for word in customerInput.split() if word.lower() not in stop_words]
        customerInput_clean_removed = " ".join(customerInput_clean)
        customerInputs_cleaned.append([customerInput_clean_removed, category])
    return customerInputs_cleaned

def main():
    input_df = get_data('customerInput-trainings-set.csv')
    clean_df = clean_data(input_df, 'allstopwords.txt')
    pd.DataFrame.from_records(clean_df).to_excel('cleaned.xlsx',encoding='utf8')


if __name__ == '__main__':
    main()