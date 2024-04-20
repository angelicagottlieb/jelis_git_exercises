# file: app.py

from lib.album_repository import *
from lib.album import *
from lib.database_connection import DatabaseConnection
from lib.artist_repository import *
from lib.artist import *

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")
        
    def run(self):
        album_repository = AlbumRepository(self._connection)
        artist_repository = ArtistRepository(self._connection)

        print("Welcome to the music library manager!")

        print("What would you like to do?")
        print("1 - List all albums")
        print("2 - List all artists")

        choice = input("Enter your choice: ")

        if choice == '1':
                self.list_all_albums(album_repository)
        elif choice == '2':
                self.list_all_artists(artist_repository)

        

    def list_all_albums(self, album_repository):
        album_repository = AlbumRepository(self._connection)
        albums = album_repository.all()
        print("Here is the list of albums:")
        for album in albums:
            print(f"* {album.id}: {album.title}")

    def list_all_artists(self, artist_repository):
        artist_repository = ArtistRepository(self._connection)
        artists = artist_repository.all()
        print("Here is the list of artists:")
        for artist in artists:
            print(f"* {artist.name}")

if __name__ == '__main__':
    app = Application()
    app.run()
