class ResponseFactory:
    """Generates boundary objects from domain objects"""

    def to_response(self, domain_object):
        """Converts a domain object to a boundary object"""
        raise NotImplementedError