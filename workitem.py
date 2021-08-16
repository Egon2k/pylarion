from dataclasses import dataclass

@dataclass
class workitem():
    id: str
    author: str
    created: str
    description: str
    linkedWorkitems: list()
    type: str


