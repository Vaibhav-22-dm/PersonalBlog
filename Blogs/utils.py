import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Function to get article recommendations based on user query
def get_article_recommendations(user_query, blogs, num_recommendations=5):
    # Create a DataFrame from the dataset
    clean = re.compile('<.*?>')
    articles = [
        {
            'id': item.id,
            'content':re.sub(clean, '',item.content)
        } for item in list(blogs)]
    
    articles_df = pd.DataFrame(articles)

    # Preprocess the text data (optional: convert to lowercase and remove special characters)
    articles_df['content'] = articles_df['content'].str.lower()
    articles_df['content'] = articles_df['content'].replace(r'[^a-zA-Z0-9\s]', '', regex=True) 
    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(articles_df['content'])
    
    # Convert user query to TF-IDF vector
    user_query_vector = vectorizer.transform([user_query.lower()])
    
    # Compute cosine similarity between user query and articles
    cosine_similarities = cosine_similarity(user_query_vector, tfidf_matrix)
    
    # Get the indices of articles with highest cosine similarity to the user query
    similar_article_indices = cosine_similarities.argsort()[0][-num_recommendations:][::-1]
    
    # Get the recommended articles
    recommended_articles = list(articles_df.loc[similar_article_indices,'id'])
    
    return [blogs.filter(id=id).first() for id in recommended_articles]

# Example usage
# user_question = "Tell me about topic X"
# recommended_articles = get_article_recommendations(user_question, df)
# print(recommended_articles[['title', 'content']])
