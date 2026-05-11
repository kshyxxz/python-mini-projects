from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('blog_index.html', title="Wecome to My Website")

posts = [
		{"id": 1, "title": "First Post", "content": "This is the content of the first post."},
		{"id": 2, "title": "Second Post", "content": "This is the content of the second post."},
		{"id": 3, "title": "Third Post", "content": "This is the content of the third post."},
		{"id": 4, "title": "Fourth Post", "content": "This is the content of the fourth post."},
		{"id": 5, "title": "Fifth Post", "content": "This is the content of the fifth post."},
		{"id": 6, "title": "Sixth Post", "content": "This is the content of the sixth post."},
		{"id": 7, "title": "Seventh Post", "content": "This is the content of the seventh post."},
		{"id": 8, "title": "Eighth Post", "content": "This is the content of the eighth post."},
		{"id": 9, "title": "Ninth Post", "content": "This is the content of the ninth post."},
		{"id": 10, "title": "Tenth Post", "content": "This is the content of the tenth post."},
		{"id": 11, "title": "Eleventh Post", "content": "This is the content of the eleventh post."},
		{"id": 12, "title": "Twelfth Post", "content": "This is the content of the twelfth post."}
	]

pagination = [posts[i:i + 5] for i in range(0, len(posts), 5)]

@app.route('/posts/pages/<int:page>')
def show_posts(page):
	if 1 <= page <= len(pagination):
		return render_template('blog_posts.html', posts=posts, pagination=pagination, page=page, page_index=page - 1)
	else:
		return "Page not found", 404

@app.route('/posts/<int:id>')
def show_post(id):
	return render_template('blog_post.html', posts=posts, id=id)

if __name__ == "__main__":
	app.run(debug=True)  