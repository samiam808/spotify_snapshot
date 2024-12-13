#https://github.com/liz-stippell/spotify_data.git
import sys
from PyQt6 import QtWidgets
from gui import Ui_spotify_snapshot_window  # GUI class
from logic import analyze_data

class SpotifySnapshotApplication(QtWidgets.QMainWindow):
    """
    Main application class for managing the Spotify Snapshot GUI and interactions.
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_spotify_snapshot_window()
        self.ui.setupUi(self)

        # Set default values for input fields
        self.ui.songs_to_load.setValue(10)  # Default to top 10 songs
        self.ui.artists_to_load.setValue(10)  # Default to top 10 artists

        # Connect the submit button to the analysis function
        self.ui.submit_button.clicked.connect(self.run_analysis)

    def run_analysis(self):
        """
        Collects input from the GUI, performs data analysis, and displays the result.
        """
        # Retrieve user inputs from the GUI
        google_sheet_url = self.ui.doc_link.text()
        start_date = self.ui.start_date.date().toString('yyyy-MM-dd')
        end_date = self.ui.end_date.date().toString('yyyy-MM-dd')
        top_songs_limit = self.ui.songs_to_load.value()
        top_artists_limit = self.ui.artists_to_load.value()
        specific_song = self.ui.specific_song.text()
        specific_artist = self.ui.specific_artist.text()

        # Perform analysis and display the results in the text browser
        analysis_result = analyze_data(
            google_sheet_url, start_date, end_date,
            top_songs_limit, top_artists_limit, specific_song, specific_artist
        )
        self.ui.textBrowser.setPlainText(analysis_result)


if __name__ == '__main__':
    # Initialize and run the application
    app = QtWidgets.QApplication(sys.argv)
    main_window = SpotifySnapshotApplication()
    main_window.show()
    sys.exit(app.exec())