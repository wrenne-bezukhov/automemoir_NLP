import pandas as pd
from langdetect import detect

def is_english(text):
    try:
        return detect(text) == 'en'
    except:
        return False

def filter_english_reviews(csv_file):
    df = pd.read_csv(csv_file)
    # Assuming the reviews are in a column named 'review'
    english_reviews = df[df['reviews_review'].apply(is_english)]
    english_reviews.to_csv('les_annees_run_results_eng.csv', index=False)

filter_english_reviews('les_annees_run_results.csv')
