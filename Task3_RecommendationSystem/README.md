# CodSoft AI Internship - Task 3: Recommendation System

A simple content-based movie recommendation system built using genre similarity, as part of the CodSoft Artificial Intelligence Virtual Internship.

## About

This project recommends movies to a user based on a movie they already like. It uses **content-based filtering** — comparing the genre tags of movies rather than other users' ratings — to find and suggest the most similar titles.

## Features

- Dataset of 14 sample movies, each tagged with one or more genres
- Recommends the top 3 most similar movies to a chosen title
- Uses **Jaccard similarity** to measure genre overlap between movies
- Case-insensitive movie name matching
- Simple console-based interaction loop

## Tech Used

- Python 3
- No external libraries — pure Python logic (no pandas/sklearn required)

## How to Run

1. Clone this repository or copy `recommendation_system.py`
2. Run it with Python:
   ```
   python recommendation_system.py
   ```
3. Type the name of a movie from the printed list (e.g. `Inception`, `Titanic`)
4. View your top 3 recommended movies with similarity scores
5. Type `quit` to exit

## How It Works

Each movie is represented as a **set of genres**. To compare two movies, the program calculates:

```
similarity = (shared genres) / (total unique genres between both movies)
```

This is called **Jaccard similarity** — a score between 0 (no genres in common) and 1 (identical genres). The movies with the highest similarity score to the user's chosen movie are recommended.

## What I Learned

- The difference between content-based and collaborative filtering approaches
- How to represent and compare items using set operations
- Implementing a similarity metric (Jaccard similarity) from scratch
- Building an interactive recommendation loop in Python

## Internship

Built as Task 3 for the **Artificial Intelligence Virtual Internship** at [CodSoft](https://www.codsoft.in).
