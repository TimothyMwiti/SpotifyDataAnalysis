import pytest
<<<<<<< HEAD
from main import get_list_of_featured_artists_from_track_name
=======
from utilities import Utilities
>>>>>>> feature/getNumberOfMinutesListenedToArtist

class TestGettingFeaturedArtistsFromTrackName:

    def test_track_contains_no_featured_artist(self):
<<<<<<< HEAD
        assert [] == get_list_of_featured_artists_from_track_name("Who Want The Smoke?")
        
    
    def test_track_contains_one_featured_artist_concated_using_feat(self):
        assert ["Drake"] == get_list_of_featured_artists_from_track_name("Going Bad (feat. Drake)")
    

    def test_track_contains_multiple_featured_artist_concated_using_feat(self):
        assert ["Offset", "Travis Scott"] == sorted(get_list_of_featured_artists_from_track_name("ZEZE (feat. Travis Scott & Offset)"))
        assert ["A$AP Rocky", "French Montana", "ScHoolboy Q", "Trinidad James"] == sorted(get_list_of_featured_artists_from_track_name(
            "Work REMIX (feat. A$AP Rocky, French Montana, Trinidad James & ScHoolboy Q)"
        ))
        

    def test_track_contains_multiple_featured_artist_concated_using_with(self):
        assert ["Keala Settle", "Kesha", "Missy Elliott"] == \
            sorted(get_list_of_featured_artists_from_track_name(
                "This Is Me (The Reimagined Remix) [with Keala Settle, Kesha & Missy Elliott]"))

    def test_track_contains_multipled_featured_artist_concated_with_parentheses(self):
        assert ["Gunna", "Lil Baby"] == sorted(get_list_of_featured_artists_from_track_name("Drip Too Hard (Lil Baby & Gunna)"))
=======
        assert [] == Utilities.get_list_of_featured_artists_from_track_name("Who Want The Smoke?")


    def test_track_contains_one_featured_artist_concated_using_feat(self):
        assert ["Drake"] == Utilities.get_list_of_featured_artists_from_track_name("Going Bad (feat. Drake)")


    def test_track_contains_multiple_featured_artist_concated_using_feat(self):
        assert ["Offset", "Travis Scott"] == sorted(Utilities.get_list_of_featured_artists_from_track_name("ZEZE (feat. Travis Scott & Offset)"))
        assert ["A$AP Rocky", "French Montana", "ScHoolboy Q", "Trinidad James"] == sorted(Utilities.get_list_of_featured_artists_from_track_name(
            "Work REMIX (feat. A$AP Rocky, French Montana, Trinidad James & ScHoolboy Q)"
        ))


    def test_track_contains_multiple_featured_artist_concated_using_with(self):
        assert ["Keala Settle", "Kesha", "Missy Elliott"] == \
            sorted(Utilities.get_list_of_featured_artists_from_track_name(
                "This Is Me (The Reimagined Remix) [with Keala Settle, Kesha & Missy Elliott]"))

    def test_track_contains_multipled_featured_artist_concated_with_parentheses(self):
        assert ["Gunna", "Lil Baby"] == sorted(Utilities.get_list_of_featured_artists_from_track_name("Drip Too Hard (Lil Baby & Gunna)"))
>>>>>>> feature/getNumberOfMinutesListenedToArtist
