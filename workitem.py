from dataclasses import dataclass

@dataclass
class workitem():
    id: int
    author: str
    created: str
    description: str
    linkedWorkitems: list()
    type: str


