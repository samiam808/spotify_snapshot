import pandas as pd
import re
from collections import Counter


def convert_google_link(link: str) -> str:
    """
    Converts a Google Sheet URL to a CSV export link.

    Args:
        link (str): The original Google Doc URL.

    Returns:
        str: The URL for exporting the sheet as a CSV file.
    """
    pattern = r'https://docs\.google\.com/spreadsheets/d/([a-zA-Z0-9-_]+)(/edit#gid=(\d+)|/edit.*)?'
    replacement = lambda match: (
        f'https://docs.google.com/spreadsheets/d/{match.group(1)}/export?' +
        (f'gid={match.group(3)}&' if match.group(3) else '') +
        'format=csv'
    )
    return re.sub(pattern, replacement, link)


def analyze_data(
    google_link: str,
    start_date: str,
    end_date: str,
    top_songs_limit: int,
    top_artists_limit: int,
    specific_song: str = None,
    specific_artist: str = None
) -> str:
    """
    Analyzes Spotify data from a Google Sheet URL and produces a summary.

    Args:
        google_link (str): URL of the Google Sheet containing the data.
        start_date (str): Start date for the analysis (format: 'yyyy-MM-dd').
        end_date (str): End date for the analysis (format: 'yyyy-MM-dd').
        top_songs_limit (int): Number of top songs to display.
        top_artists_limit (int): Number of top artists to display.
        specific_song (str): Specific song to count plays for.
        specific_artist (str): Specific artist to count plays for.

    Returns:
        str: A detailed analysis report.
    """
    try:
        # Convert Google Sheet URL and load data into a DataFrame
        csv_url = convert_google_link(google_link)
        spotify_data = pd.read_csv(csv_url)

        # Ensure 'date' column is properly formatted as datetime
        spotify_data['date'] = pd.to_datetime(spotify_data['date'], format='%B %d, %Y at %I:%M%p')

        # Filter data by the provided date range
        filtered_data = spotify_data[(spotify_data['date'] >= start_date) & (spotify_data['date'] <= end_date)]

        # Compute play counts for songs and artists
        filtered_song_counts = Counter(filtered_data['song'])
        filtered_artist_counts = Counter(filtered_data['artist'])
        all_song_counts = Counter(spotify_data['song'])
        all_artist_counts = Counter(spotify_data['artist'])

        # Construct the analysis result
        report = f"SELECTED TIMEFRAME: {start_date} TO {end_date}\n"
        report += f"TOTAL PLAYS IN SELECTED TIMEFRAME: {len(filtered_data)} SONGS\n\n"

        # Add top songs and artists in the selected timeframe
        report += f"TOP {top_songs_limit} SONGS IN SELECTED TIMEFRAME:\n"
        for idx, (song, count) in enumerate(filtered_song_counts.most_common(top_songs_limit), start=1):
            report += f"{idx}. {song}: {count} plays\n"

        report += f"TOP {top_artists_limit} ARTISTS IN SELECTED TIMEFRAME:\n"
        for idx, (artist, count) in enumerate(filtered_artist_counts.most_common(top_artists_limit), start=1):
            report += f"{idx}. {artist}: {count} plays\n"

        # Add all-time top songs and artists
        report += f"\n--- ALL-TIME TOP {top_songs_limit} SONGS ---\n"
        for idx, (song, count) in enumerate(all_song_counts.most_common(top_songs_limit), start=1):
            report += f"{idx}. {song}: {count} plays\n"

        report += f"\n--- ALL-TIME TOP {top_artists_limit} ARTISTS ---\n"
        for idx, (artist, count) in enumerate(all_artist_counts.most_common(top_artists_limit), start=1):
            report += f"{idx}. {artist}: {count} plays\n"

        # Include counts for specific song and artist, if provided
        if specific_song:
            report += f"\nSPECIFIC SONG: {specific_song}\n"
            report += f"Plays in Selected Timeframe: {filtered_song_counts.get(specific_song, 0)}\n"
            report += f"All-Time Plays: {all_song_counts.get(specific_song, 0)}\n"

        if specific_artist:
            report += f"\nSPECIFIC ARTIST: {specific_artist}\n"
            report += f"Plays in Selected Timeframe: {filtered_artist_counts.get(specific_artist, 0)}\n"
            report += f"All-Time Plays: {all_artist_counts.get(specific_artist, 0)}\n"

        return report

    except Exception as error:
        return f"Error: {str(error)}"