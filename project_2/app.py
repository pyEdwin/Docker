from flask import Flask, jsonify, request

app=Flask(__name__)

# Sample data
movies = [
    {"id":1 , "title":"Titanic" , "author":"Romeo"},
    {"id":2 , "title":"Rambo" , "author":"Jean"},
    {"id":3 , "title":"Boy II" , "author":"Pierre"},
    {"id":4 , "title":"House" , "author":"Patrick"},
    {"id":5 , "title":"Ocean" , "author":"Remis"}
]

# Get all the movies
@app.route('/movies' , methods=['GET'])
def get_movies():
    return movies

# Retrieve a movie
@app.route('/movies/<int:movie_id>' , methods=['GET'])
def movie_retrieved(movie_id):
    for movie in movies:
        if movie['id'] == movie_id:
            return movie
    return ("Error :  Book not found")


# Create a movie
@app.route('/movies', methods=['POST'])
def create_movie():
    new_movie = {"id":len(movies)+1 , "title":request.json["title"] , "author":request.json['author']}
    movies.append(new_movie)
    return new_movie


# Update a movie
@app.route('/movies/<int:movie_id>' , methods=['PUT'])
def update_movie(movie_id):
     for movie in movies:
        if movie['id'] == movie_id:
            movie['title'] = request.json['title']
            movie['author'] = request.json['author']
            return movie
        return ("Error :  Book not found") 

# Delete a movie
@app.route('/movies/<int:movie_id>' , methods=['DELETE'])
def delete_movie(movie_id):
     for movie in movies:
         if movie['id'] == movie_id:
            movies.remove(movie)
            return {"data":"Movie deleted successfully"}
     return ("Error :  Book not found")
 
# Run the flask app
if __name__ == '__main__':
    app.run(debug=True)