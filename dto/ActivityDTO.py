class ActivityDTO:
    def __init__(self, activity, accessibility, type, participants, price, link, key):
        self.activity = activity
        self.accessibility = accessibility
        self.type = type
        self.participants = participants
        self.price = price
        self.link = link
        self.key = key

    @classmethod
    def from_json(cls, data):
        return cls(
            activity=data.get("activity"),
            accessibility=data.get("accessibility"),
            type=data.get("type"),
            participants=data.get("participants"),
            price=data.get("price"),
            link=data.get("link"),
            key=data.get("key"),
        )
