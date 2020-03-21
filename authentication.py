import tweepy
from credentials import API_CREDENTIALS


def authenticate(credential):
    auth = tweepy.OAuthHandler(
        credential["api_key"],
        credential["api_secret"]
    )
    auth.set_access_token(
        credential["access_token_key"],
        credential["access_token_secret"]
    )
    return auth


def validate_credential(credential: dict):
    auth = authenticate(credential)
    api = tweepy.API(auth)
    # If the authentication was successful, you should
    # see the name of the account print out
    return api.me().name == "Shuyuan Deng"


if __name__ == "__main__":
    print("Validating Twitter API credentials...")
    for cred_id, credential in API_CREDENTIALS.items():
        print(
            cred_id,
            credential["usage"],
            validate_credential(credential)
        )
