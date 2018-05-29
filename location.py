class Location:
    def __init__(self,description):
        self.description=description
        exits={}
    def __str__(self):
        exitList=""
        return self.description+exitList