class Sig:
    def __init__(self, item):
        self.item = item
        self.type = "sig"
        self.profile = ""
        self._profilename = ""
        self._profilestate = ""

    def __repr__(self):
        return "{0} {1} {2}".format(self.type, self.profile, self._profilename)
