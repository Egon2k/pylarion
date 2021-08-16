from dataclasses import dataclass

@dataclass
class workitem():
    id: str
    title: str
    author: str
    created: str
    description: str
    linkedWorkitems: list()
    type: str


