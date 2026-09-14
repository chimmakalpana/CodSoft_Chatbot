"""
CodSoft AI Internship - Task 3: Recommendation System
Author: Chimma Kalpana

A simple content-based movie recommendation system.
No external libraries needed (no pandas/sklearn) - runs anywhere, including Replit/Programiz.

How it works:
- Each movie has a set of genre tags.
- We recommend movies whose genres overlap most with a movie the user likes,
  using Jaccard similarity (intersection over union of genre sets).
"""

# ---------------------------------------------------------
# Sample movie dataset: name -> set of genres
# (In a real project this could come from a CSV/database instead)
# ---------------------------------------------------------
movies = {
    "The Dark Knight": {"Action", "Crime", "Drama"},
    "Inception": {"Action", "Sci-Fi", "Thriller"},
    "Interstellar": {"Sci-Fi", "Drama", "Adventure"},
    "The Notebook": {"Romance", "Drama"},
    "La La Land": {"Romance", "Musical", "Drama"},
    "John Wick": {"Action", "Thriller", "Crime"},
    "The Conjuring": {"Horror", "Thriller"},
    "Get Out": {"Horror", "Thriller", "Mystery"},
    "Toy Story": {"Animation", "Comedy", "Adventure"},
    "Finding Nemo": {"Animation", "Comedy", "Adventure"},
    "The Hangover": {"Comedy"},
    "Superbad": {"Comedy"},
    "Titanic": {"Romance", "Drama"},
    "Avengers: Endgame": {"Action", "Sci-Fi", "Adventure"},
}


def jaccard_similarity(set_a, set_b):
    """Similarity score between 0 and 1 based on shared genres."""
    intersection = len(set_a & set_b)
    union = len(set_a | set_b)
    return intersection / union if union else 0


def recommend(movie_name, top_n=3):
    """Return the top_n most similar movies to the given movie."""
    if movie_name not in movies:
        return None

    target_genres = movies[movie_name]
    scores = []

    for title, genres in movies.items():
        if title == movie_name:
            continue
        score = jaccard_similarity(target_genres, genres)
        if score > 0:
            scores.append((title, score))

    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:top_n]


def print_movie_list():
    print("\nAvailable movies:")
    for title in movies:
        print(f"  - {title}")


def main():
    print("=== Movie Recommendation System ===")
    print("(Content-based filtering using genre similarity)")
    print_movie_list()

    while True:
        choice = input("\nEnter a movie you like (or 'quit' to exit): ").strip()

        if choice.lower() == "quit":
            print("Goodbye!")
            break

        # Case-insensitive match against the dataset
        match = next((m for m in movies if m.lower() == choice.lower()), None)

        if not match:
            print("Movie not found. Please pick from the list above.")
            continue

        results = recommend(match)
        if not results:
            print(f"No similar movies found for '{match}'.")
            continue

        print(f"\nBecause you liked '{match}', you might also enjoy:")
        for title, score in results:
            print(f"  - {title}  (similarity: {score:.2f})")


if __name__ == "__main__":
    main()
