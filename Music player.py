import random   # Random function for display the average rating

# Rating class for audio
class Audio:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.rating = 0

    # Self rating function to rate the song for audio
    def set_rating(self, rating):
        self.rating = rating

# Function for Playlist to store the username, audio, genre and rating
class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.audios = []
        self.rating = 0

    def add_audio(self, audio): #Adding audio to the playlist
        self.audios.append(audio)  

    def set_rating(self, rating):  # Self rating function to rate the song for the playlist
        self.rating = rating

class MusicPlayer:  # Music Player Class initiated
    def __init__(self):  # Consrtuctor method
        self.users = []
        self.playlists = []

    def create_user(self, name):  #Created a user name
        user = {'name': name}
        self.users.append(user)

    def create_audio(self, name, url):  # Function for create audio  using URL
        return Audio(name, url)

    def create_playlist(self, name, genre):  # Function for Multiple playlist based on the genre
        return Playlist(name, genre)

    def add_audio_to_playlist(self, audio, playlist):   # Function for adding playlist to the 
        playlist.add_audio(audio)

    def search_audio_by_name(self, name):     # Function to search audio by name
        for playlist in self.playlists:             
            for audio in playlist.audios:
                if audio.name == name:
                    return audio
        return None

    def search_playlist_by_name(self, name):    # Search function for searching the playlist by name
        for playlist in self.playlists:
            if playlist.name == name:
                return playlist
        return None

    def generate_random_ratings(self):     # Function for generating random average rating range of 1-5
        return random.randint(1, 5)

    def display_average_rating(self):       # Function to display the average rating 
        total_ratings = 0
        total_count = 0
        for playlist in self.playlists:
            total_ratings += playlist.rating
            total_count += 1

            for audio in playlist.audios:
                total_ratings += audio.rating
                total_count += 1

        average_rating = total_ratings / total_count if total_count > 0 else 0
        return average_rating


player = MusicPlayer()

# Create users
player.create_user("User1")
player.create_user("User2")
player.create_user("User3")

# Create audio and playlist
audio1 = player.create_audio("Fearless Pt. ii", "https://wynk.in/music/song/fearless-pt-ii/ab_5055199521152_GB2LD1700381")
playlist1 = player.create_playlist("Playlist1", "Pop")

# Add audio to playlist
player.add_audio_to_playlist(audio1, playlist1)

# Give ratings
audio1.set_rating(4)  # User1's rating
playlist1.set_rating(5)  # User2's rating

# Display average rating
average_rating = player.display_average_rating()
print(f"Average Rating: {average_rating}")

