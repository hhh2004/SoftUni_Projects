def movie_organizer(*args):
    movies = {}
    for movie, genre in args:
        if genre in movies.keys():
            movies[genre].append(movie)
        else:
            movies[genre] = [movie]

    for genre, genre_movies in movies.items():
        movies[genre] = sorted(genre_movies)
    movies = dict(sorted(movies.items()))
    movies = dict(sorted(movies.items(), key=lambda x: -len(x[1])))

    output = []
    for genre, genre_movies in movies.items():
        output.append(f"{genre} - {len(genre_movies)}")
        for movie in genre_movies:
            output.append(f"* {movie}")
    a = '10' + int('2')
    return '\n'.join(output)
