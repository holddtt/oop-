# Classes for authentication through social networks
class FacebookAuth:
    def authenticate(self, token):
        # Facebook authentication logic
        print("Authentication through Facebook")

class GoogleAuth:
    def authenticate(self, token):
        # Google authentication logic
        print("Authentication through Google")

class TwitterAuth:
    def authenticate(self, token):
        # Twitter authentication logic
        print("Authentication through Twitter")

# Facade class for social network authentication
class SocialAuthFacade:
    def __init__(self):
        self.facebook_auth = FacebookAuth()
        self.google_auth = GoogleAuth()
        self.twitter_auth = TwitterAuth()

    def authenticate_with_facebook(self, token):
        self.facebook_auth.authenticate(token)

    def authenticate_with_google(self, token):
        self.google_auth.authenticate(token)

    def authenticate_with_twitter(self, token):
        self.twitter_auth.authenticate(token)

# Using the facade class
social_auth = SocialAuthFacade()

# Authentication through Facebook
facebook_token = "facebook_access_token"
social_auth.authenticate_with_facebook(facebook_token)

# Authentication through Google
google_token = "google_access_token"
social_auth.authenticate_with_google(google_token)

# Authentication through Twitter
twitter_token = "twitter_access_token"
social_auth.authenticate_with_twitter(twitter_token)
