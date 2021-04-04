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
