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


# Run the flask app
if __name__ == '__main__':
    app.run(debug=True)