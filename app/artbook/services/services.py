from datetime import date, datetime
from neo4j.time import Date as neo4jDate

class Neo4JDate:
    @staticmethod
    def toDate(ndate: neo4jDate):
        """
        Converts an instance of neo4j.time.Date to a Python datetime.date
        """
        try:
            return date(ndate.year, ndate.month, ndate.day)
        except:
            return None
