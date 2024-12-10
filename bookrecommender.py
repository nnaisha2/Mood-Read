# bookrecommender.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load data
data = pd.read_csv('book_details.csv', encoding='ISO-8859-1')

# Fill or drop missing values
data['description'] = data['description'].fillna("")
data['title'] = data['title'].fillna("")
data['author'] = data['author'].fillna("")
data['combined_text'] = data['title'] + " " + data['author']

# Remove columns with excessive NaN values
data.dropna(thresh=len(data) * 0.5, axis=1, inplace=True)

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['description'])

# Compute similarity
similarity_matrix = cosine_similarity(tfidf_matrix)

# Function to map books to moods
def map_to_mood(row):
    text = (row['title'] + " " + row.get('description', "")).lower()
    
    mood_keywords = {
        "Admiration": ["hero", "achievement", "leader"],
        "Aesthetic": ["beauty", "art", "painting", "photography"],
        "Amusement": ["funny", "humor", "comic", "laugh"],
        "Anger": ["revenge", "injustice", "betrayal"],
        "Anxiety": ["worry", "tense", "stress", "fear"],
        "Awe": ["wonder", "amazing", "majestic", "universe"],
        "Awkwardness": ["embarrass", "cringe", "misunderstanding"],
        "Boredom": ["routine", "mundane", "boring"],
        "Calmness": ["peace", "serene", "quiet", "relax"],
        "Craving": ["desire", "hunger", "yearning"],
        "Disgust": ["gross", "revolting", "nausea"],
        "Empathetic": ["suffering", "loss", "grief"],
        "Entrancement": ["magic", "spellbound", "captivate"],
        "Excitement": ["adventure", "thrill", "exhilarate"],
        "Fear": ["terror", "scared", "danger"],
        "Horror": ["ghost", "horror", "blood", "haunted"],
        "Interest": ["fascinate", "curious", "learn", "mystery"],
        "Joy": ["happy", "cheerful", "bright", "positive"],
        "Nostalgia": ["memory", "past", "childhood"],
        "Romance": ["love", "romantic", "heart"],
        "Sadness": ["sad", "loss", "tears", "blue"],
        "Satisfaction": ["fulfill", "reward", "achieve"],
        "Sexual": ["passion", "lust", "sensual"],
        "Surprise": ["unexpected", "shock", "twist"]
    }
    
    for mood, keywords in mood_keywords.items():
        if any(keyword in text for keyword in keywords):
            return mood
    return "Neutral"

data['mood'] = data.apply(map_to_mood, axis=1)

def recommend_books(mood, similarity_matrix):
    mood_books = data[data['mood'] == mood]
    recommendations = mood_books.head(10)  # Top 10 recommendations
    return recommendations
#if __name__ == "__main__":
    #mood = input("Enter your mood (e.g., Happy, Sad, Adventure, etc.): ")
    
    ## Check for valid mood input
    #mood = mood.capitalize()  # Make sure the input is properly formatted
    #if mood not in data['mood'].unique():
        #print("Invalid mood. Please enter a valid mood from the list.")
    #else:
        #recommendations = recommend_books(mood, similarity_matrix)
        #print("\nTop book recommendations for your mood '{}':\n".format(mood))
        #print(recommendations[['title', 'author']])



from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    mood = (request.json)['mood']
    mood = mood.capitalize()

    if mood not in data['mood'].unique():
        response = {"message": "Invalid mood. Please enter a valid mood from the list."}
        return jsonify(response), 400
    else:
        recommendations = recommend_books(mood, similarity_matrix)
        response = recommendations[['title', 'author']].to_dict(orient='records')
        return jsonify(response), 200

if __name__ == "__main__":
    app.run(port=5000)



