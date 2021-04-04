from flask_restx import reqparse, inputs

artist = reqparse.RequestParser()
artist.add_argument('name', type=str, required=True, trim=True, help="Preferable name (or nickname) the artist is known by.")
artist.add_argument('birth', type=inputs.date_from_iso8601, required=False, help='The date of birth of the artist.')
artist.add_argument('death', type=inputs.date_from_iso8601, required=False, help='The date of death of the artist.')
artist.add_argument('alternative_name', type=str, action='append', required=False, help="Another names the artist is known by.")


artwork = reqparse.RequestParser()
artwork.add_argument('title', type=str, required=True, trim=True, help="Title of the artwork.")
artwork.add_argument('creation', type=inputs.date_from_iso8601, required=False, help='The date of creation of the artwork.')
artwork.add_argument('techniques', type=str, action='append', required=False, help="Techniques used in the artwork.")


event = reqparse.RequestParser()
event.add_argument('title', type=str, required=True, trim=True, help="Name or title of the event.")
event.add_argument('start', type=inputs.date_from_iso8601, required=True, help='Start date of the event.')
event.add_argument('end', type=inputs.date_from_iso8601, required=True, help='End date of the event.')
