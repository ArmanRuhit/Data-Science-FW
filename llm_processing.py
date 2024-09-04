from transformers import pipeline
import pandas as pd
from sqlalchemy import create_engine

summarizer = pipeline("summarization", model="t5-small")

engine = create_engine('sqlite:///news.db')
df = pd.read_sql('news', engine)

df['Summary'] = df['Description'].apply(lambda x: summarizer(x, max_length=50, min_length=25, do_sample=False)[0]['summary_text'])

df.to_sql('summarized_news', engine, index=False, if_exists='replace')

print("LLM summarization task completed!")
