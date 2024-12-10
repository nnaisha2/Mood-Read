# Mood-Read
## Book Recommender

This project is a mood-based book recommendation system, which suggests books to users based on their current mood.

### How it Works?

The program first read a CSV file 'book_details.csv'(a kaggle dataset from : https://www.kaggle.com/datasets/deepaktheanalyst/books-details-dataset) containing book details like title, author, description. It then maps books to different moods based on certain keywords present in their title and description. Then, based on user's mood input, it recommends a list of books that matches with the selected mood.

The project includes a Python file `bookrecommender.py` which includes the main codebase and a HTML file having a user interface setup which connects to a backend server setup in the Python file.

## How to Use

You can interact with this system via the HTML user interface.

### Prerequisites

- Python 3
- Pandas
- Sklearn

### Setup

1. Clone this repository.
2. Run the setup commands to install necessary Python libraries.
```shell
$ pip install pandas
$ pip install -U scikit-learn
```
3. Run `bookrecommender.py` 
```shell
$ python bookrecommender.py
```
4. Open `index.html` in your web browser.
5. Select your mood from the dropdown menu and click "Get Recommendations" to receive book recommendations.

## API

The script `bookrecommender.py` sets up a Flask API server at `localhost:5000`. It has a single endpoint `/recommendations`, which accepts POST requests with 'mood' in JSON format and returns a JSON response containing 10 recommended books.

## User Interface

The user interface is a simple single-page application which lets you choose your current mood from a dropdown. After selecting the mood, it sends a POST request to the server and displays the received book recommendations.

## Future Updates

As of now, the recommender provides book recommendations based on user's mood. In future, the recommendation system can be improved by considering user's past reading preferences, user’s feedback and by adding more books and moods.


## License

This project is licensed under the terms of the MIT License.
