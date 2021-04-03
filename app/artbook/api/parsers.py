from flask_restx import reqparse

artist = reqparse.RequestParser()
artist.add_argument('name', type=str, required=True, help="Preferable name (or nickname) the artist is known by")
artist.add_argument('alternative_name', type=str, required=False, help="At least one alternative name must be supplied.")
