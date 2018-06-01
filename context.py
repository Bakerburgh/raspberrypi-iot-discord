class Context:
    server = None
    channel = None

    def __init__(self, bot):
        self.bot = bot

    def valid(self):
        return self.bot and self.server
