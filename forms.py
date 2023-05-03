from wtforms import SelectField, StringField, TextAreaField
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField('Playlist Name')
    description = TextAreaField('Description')

class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField('Song Name')
    artist = StringField('Artist Name')

class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
