from ..reddit import RedditClient

RECIPE_SUBREDDITS = ["recipes", "easyrecipes", "TopSecretRecipes"]

# 1. Constructor Injection
class Ideas:
    def __init__(self, reddit_client: RedditClient):
        self.reddit_client = reddit_client

    def fetch_ideas(self) -> dict:
        return {
            key: self.reddit_client.get_reddit_top(subreddit=key)
            for key in RECIPE_SUBREDDITS
        }


# 2. Setter Injection
class Ideas:
    _client = None

    def fetch_ideas(self) -> dict:
        return {
            key: self.client.get_reddit_top(subreddit=key) for key in RECIPE_SUBREDDITS
        }

    @property # The @property decorator is used to define a method that acts as a getter for an attribute
    def client(self):
        return self._client

    @client.setter # The @client.setter decorator is used to define a method that acts as a setter for an attribute.
    def client(self, value: RedditClient):
        self._client = value


# Interface Injection
