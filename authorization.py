import tekore as tk

def authorize():
    CLIENT_ID = "ba0dc2e882664d6790fd17ed6a8f6d66"
    CLIENT_SECRET = "6f92962ba29e4a3fb7fd8b1525200444"
    app_token = tk.request_client_token(CLIENT_ID, CLIENT_SECRET)
    return tk.Spotify(app_token)