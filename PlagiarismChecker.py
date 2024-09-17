import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the spaCy model for NLP processing
nlp = spacy.load('en_core_web_sm')

# Function to preprocess the text: tokenization, lemmatization, and stopword removal
def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(tokens)

# Function to calculate cosine similarity between two documents
def calculate_similarity(text1, text2):
    # Preprocess the texts
    text1_clean = preprocess_text(text1)
    text2_clean = preprocess_text(text2)
    
    # Vectorize the texts using TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1_clean, text2_clean])
    
    # Calculate the cosine similarity
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity[0][0]

# Main function for plagiarism detection
def check_plagiarism(text1, text2):
    similarity = calculate_similarity(text1, text2)
    print(f"Similarity score: {similarity * 100:.2f}%")
    
    if similarity > 0.8:
        print("Potential plagiarism detected!")
    else:
        print("The documents are likely different.")

# Example usage
if __name__ == "__main__":
    document1 = """This is a sample document. It contains some words that may overlap with other documents."""
    document2 = """This document is an example. Some of the words in this example may overlap with sample documents."""
    
    check_plagiarism(document1, document2)
