import requests

def search_songs_by_artist_genre(artist, genre):
    url = "https://shazam-api6.p.rapidapi.com/songs/list-artist-top-tracks"

    querystring = {"id":"40008598","locale":"en-US"}

    headers = {
        "X-RapidAPI-Key": "102ce5e804msh0bcc957ccbd7b35p105d4ejsn021be17875a4",
        "X-RapidAPI-Host": "shazam-api6.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    
    if response.status_code == 200:
        data = response.json()
        songs = data['tracks']['hits']

        songs_list = []

        for song in songs:
            song_title = song['track']['title']
            song_length = song['track']['duration']

            songs_list.append({
                'title': song_title,
                'length': song_length
            })

        return songs_list
    else:
        print('Failed to fetch songs. Status code:', response.status_code)
        return None

# Example usage
artist_name = input("Enter the artist's name: ")
genre = input("Enter the genre: ")

songs = search_songs_by_artist_genre(artist_name, genre)

if songs:
    print(f"Songs by {artist_name} in the {genre} genre:")
    for song in songs:
        print(f"Title: {song['title']}, Length: {song['length']} seconds")
else:
    print("No songs found.")