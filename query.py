# -- a. Top 5 movies Titles:
# --Duration
query1 = """
SELECT title
FROM movies
ORDER BY minutes DESC
LIMIT 5;"""

# --Year of Release
query2 = """
SELECT title
FROM  movies
ORDER BY year DESC
LIMIT 5;
"""

# --Average rating (consider movies with minimum 5 ratings)
query3 = """
SELECT m.title
FROM movies m
LEFT JOIN 
(
    SELECT movie_id, AVG(rating) as avg_rating, COUNT(*) as rating_count
    FROM ratings
    GROUP BY movie_id
    HAVING COUNT(*) >= 5
) AS r ON m.id = r.movie_id
ORDER BY avg_rating DESC
LIMIT 5;
"""

# -- Number of ratings given
query4 = """
SELECT m.title
FROM movies m
JOIN 
(
    SELECT movie_id, COUNT(*) as rating_count
    FROM ratings
    GROUP BY movie_id
) AS r ON m.id = r.movie_id
ORDER BY rating_count DESC
LIMIT 5;
"""

# -- b. Number of Unique Raters:
query5 = """
SELECT COUNT(DISTINCT rater_id) unique_rater_cnt FROM ratings;
"""

# -- c. Top 5 Rater IDs
# -- Most movies rated
query6 = """
SELECT rater_id, COUNT(DISTINCT movie_id) as movies_rated
FROM ratings
GROUP BY rater_id
ORDER BY movies_rated DESC
LIMIT 5;
"""

# -- Highest Average rating given 
query7 = """
SELECT rater_id, AVG(rating) as avg_rating, COUNT(*) as rating_count
FROM ratings
GROUP BY rater_id
HAVING COUNT(*) >= 5
ORDER BY avg_rating DESC
LIMIT 5;
"""

# -- d. Top Rated movies:
query8 = """
SELECT m.title, AVG(r.rating) as avg_rating, COUNT(r.rating) as rating_count
FROM movies m
JOIN ratings r ON m.id = r.movie_id
WHERE m.director = 'Michael Bay' 
AND m.genre = 'Comedy' 
AND m.year = 2013 
AND m.country = 'India'
GROUP BY m.title
HAVING COUNT(r.rating) >= 5
ORDER BY avg_rating DESC
LIMIT 1;
"""

# -- e. Favorite movies Genre of Rater ID 1040:
query9 = """
SELECT genre
FROM 
(
    SELECT m.genre, COUNT(*) as genre_count
    FROM movies m
    JOIN ratings r ON m.id = r.movie_id
    WHERE r.rater_id = 1040
    GROUP BY m.genre
    ORDER BY genre_count DESC
    LIMIT 1
) AS favorite_genre;
"""

# -- f. Highest Average Rating for a movies Genre by Rater ID 1040
query10 = """
SELECT genre, MAX(avg_rating) as highest_avg_rating
FROM
(
    SELECT m.genre, ROUND(AVG(r.rating),2) as avg_rating, COUNT(r.rating) as rating_count
    FROM  movies m
    JOIN ratings r ON m.id = r.movie_id
    WHERE r.rater_id = 1040
    GROUP BY 1
    HAVING COUNT(rating) >= 5
) AS subquery
GROUP BY 1;
"""

# -- g. Year with Second-Highest Number of Action Movies:
query11 = """
SELECT * FROM
(
    SELECT year,cnt, ROW_NUMBER() OVER(ORDER BY cnt DESC ) rn
    FROM (
        SELECT
            year,COUNT(DISTINCT id) cnt  
        FROM 
            (
                SELECT year, id 
                FROM movies 
                WHERE  genre ~ 'Action' AND country ='USA'
            ) m       
        LEFT JOIN 
            (
                SELECT movie_id 
                FROM ratings 
                GROUP BY movie_id
                HAVING AVG(rating) >= 6.5
            ) r 
            ON m.id = r.movie_id
        GROUP BY 1
    ) AS subquery
) as subquery2
WHERE rn=2;
"""

# -- h. Count of Movies with High Ratings:
query12 = """
SELECT title
FROM movies   m
LEFT JOIN 
(
    SELECT movie_id , rating
    FROM ratings 
    GROUP BY movie_id,rating
    HAVING COUNT(rater_id) >= 5 and rating >= 7
) AS r
ON r.movie_id=m.id;
"""

queries = [query1, query2, query3, query4, query5, query6, query7, query8, query9, query10, query11,query12]
