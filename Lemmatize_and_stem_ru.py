import os
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer  # SnowballStemmer для русского языка
import spacy

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Initialize spaCy model for lemmatization
nlp = spacy.load('ru_core_news_sm')

# Get Russian stopwords and remove specific words if needed
stopwords_russian = stopwords.words('russian')
words_to_remove = ['не', 'нет']  # Removing common negations if desired
stopwords_russian = [word for word in stopwords_russian if word not in words_to_remove]

# Initialize stemmer (SnowballStemmer is for Russian language)
stemmer = SnowballStemmer('russian')

# Define punctuation characters to remove
punct = r'[!"#$%&()*+,\-./:;<=>?@\[\]^_`{|}~«»—*\'’‘“”]'

# Function to process text: clean, tokenize, remove stopwords, lemmatize, and stem
def process_text(text, stopwords):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    text = re.sub(punct, '', text)
    # Tokenize the text using spaCy for better handling of Russian text
    doc = nlp(text)
    words = [token.text for token in doc]
    # Remove stopwords
    words = [word for word in words if word not in stopwords]
    # Lemmatize the words using spaCy (spaCy handles lemmatization better for Russian)
    lemmatized_words = [token.lemma_ for token in doc if token.text in words]
    # Stem the lemmatized words
    stemmed_words = [stemmer.stem(word) for word in lemmatized_words]
    return ' '.join(stemmed_words)

# Define input and output folders
input_folder = '/Users/Desktop/TXT'
output_folder = '/Users/Desktop/15_output'

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process each text file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        input_path = os.path.join(input_folder, filename)

        # Read file content
        with open(input_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Process the text
        processed_text = process_text(text, stopwords_russian)

        # Prepare output filename and path
        output_filename = f"{os.path.splitext(filename)[0]}_processed.txt"
        output_path = os.path.join(output_folder, output_filename)

        # Save processed text to output folder
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(processed_text)

print("Text processing completed. Results saved in:", output_folder)
