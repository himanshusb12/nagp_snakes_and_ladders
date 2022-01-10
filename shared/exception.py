class BoardException(Exception):
    def __init__(self, message):
        """
        Custom exception related to Board.

        Parameters
        ----------
        message: str
            Message to be shown if exception is raised
        """
        self.message = message
