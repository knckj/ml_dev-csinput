
import pickle 
import pandas as pd

model = pickle.load(open('customerInput_classifier-2.pkl', 'rb'))
tfidf_vectorizer = pickle.load(open('customerInput_vectorizer-2.pkl', 'rb'))
label_encoder = pickle.load(open('customerInput_label_encoder-2.pkl', 'rb'))

def process(inPath, outPath):
    input_df = pd.read_csv(inPath, encoding="ISO-8859-1", delimiter=';')

    features =  tfidf_vectorizer.transform(input_df['customerInput'])

    predictions = model.predict(features)

    input_df['category'] = label_encoder.inverse_transform(predictions)

    output_df = input_df

    output_df.to_csv(outPath, index=False, encoding='utf-8')

if __name__=="__main__":
    process('marzec2-wyczyszczony.csv','marzec-ml.csv')