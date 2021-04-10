from flask_restx import reqparse, inputs

artist = reqparse.RequestParser()
artist.add_argument('name', type=str, required=True, trim=True, help="Preferable name (or nickname) the artist is known by.")
artist.add_argument('birth', type=inputs.date_from_iso8601, required=False, default=None, help='The date of birth of the artist.')
artist.add_argument('death', type=inputs.date_from_iso8601, required=False, default=None, help='The date of death of the artist.')
artist.add_argument('alternative_name', type=str, action='append', required=False, default=None, help="Another names the artist is known by.")

partialArtist = reqparse.RequestParser()
partialArtist.add_argument('name', type=str, required=False, trim=True, help="Preferable name (or nickname) the artist is known by.")
partialArtist.add_argument('birth', type=inputs.date_from_iso8601, required=False, help='The date of birth of the artist.')
partialArtist.add_argument('death', type=inputs.date_from_iso8601, required=False, help='The date of death of the artist.')
partialArtist.add_argument('alternative_name', type=str, action='append', required=False, help="Another names the artist is known by.")


artwork = reqparse.RequestParser()
artwork.add_argument('uuid', type=str, required=False, trim=True, help="The unique identifier of the artwork.")
artwork.add_argument('title', type=str, required=True, trim=True, help="Title of the artwork.")
artwork.add_argument('creation', type=inputs.date_from_iso8601, required=False, default=None, help='The date of creation of the artwork.')
# artwork.add_argument('techniques', type=str, action='append', required=False, default=None, help="Techniques used in the artwork.")


partialArtwork = reqparse.RequestParser()
partialArtwork.add_argument('title', type=str, required=False, trim=True, help="Title of the artwork.")
partialArtwork.add_argument('creation', type=inputs.date_from_iso8601, required=False, default=None, help='The date of creation of the artwork.')
# partialArtwork.add_argument('techniques', type=str, action='append', required=False, default=None, help="Techniques used in the artwork.")


event = reqparse.RequestParser()
event.add_argument('uuid', type=str, required=False, trim=True, help="The unique identifier of the artist.")
event.add_argument('title', type=str, required=True, trim=True, help="Name or title of the event.")
event.add_argument('start', type=inputs.date_from_iso8601, required=True, help='Start date of the event.')
event.add_argument('end', type=inputs.date_from_iso8601, required=True, help='End date of the event.')


partialEvent = reqparse.RequestParser()
partialEvent.add_argument('title', type=str, required=False, trim=True, help="Name or title of the event.")
partialEvent.add_argument('start', type=inputs.date_from_iso8601, required=False, help='Start date of the event.')
partialEvent.add_argument('end', type=inputs.date_from_iso8601, required=False, help='End date of the event.')
