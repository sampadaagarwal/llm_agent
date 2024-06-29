from transformers import pipeline

# Load pre-trained model
summarizer = pipeline("summarization")

class BookAgent:
    def __init__(self, data):
        self.data = data

    def get_top_books(self, genre, top_n=100):
        return sorted(self.data.get(genre, []), key=lambda x: x['rating'], reverse=True)[:top_n]

    def get_top_10_books(self, genre):
        return self.get_top_books(genre, top_n=10)

    def get_book_for_user(self, genre):
        top_10 = self.get_top_10_books(genre)
        # Use the summarizer to help decide the best book for the user (for demo purposes, we just return the top book)
        summary = summarizer(" ".join([book['title'] for book in top_10]), max_length=50, min_length=25, do_sample=False)
        return top_10[0]

    def conclude_task(self):
        return "Thank you! Have a great day!"
