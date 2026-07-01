# collaborative filtering
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def load_dataset(file_path):
	return pd.read_csv(file_path)

def calculate_similarity(matrix):
	similarity = cosine_similarity(matrix)
	return pd.DataFrame(similarity, index=matrix.index, columns=matrix.index)

def recommend_movies(user_id, ratings_matrix, user_similarity):
    similar_users = user_similarity[user_id].sort_values(ascending=False)
    recommendations = {}
    for similar_user, similarity_score in similar_users.items():
        if similar_user == user_id:
            continue
        watched_movies = ratings_matrix.loc[similar_user]
        for movie, rating in watched_movies.items():
            if rating > 0 and ratings_matrix.loc[user_id][movie] == 0:
                if movie not in recommendations:
                    recommendations[movie] = rating * similarity_score
                else:
                    recommendations[movie] += rating * similarity_score
    return recommendations

def main():
	ratings_file = './ratings.csv'  
	ratings_data = load_dataset(ratings_file)

	ratings_matrix = ratings_data.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)
	user_similarity = calculate_similarity(ratings_matrix)
	user_id = 1 
	recommendations = recommend_movies(user_id, ratings_matrix, user_similarity)

	print(f"Recommended movies for user {user_id}:")
	for movie, score in sorted(recommendations.items(), key=lambda x: x[1], reverse=True):
		print(f"Movie ID: {movie}, Score: {score}")

if __name__ == "__main__":
	main()