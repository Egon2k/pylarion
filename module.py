from dataclasses import dataclass

@dataclass
class module():
    title: str
    author: str
    created: str
    homePageContent: str
    status: str
    type: str
    

    def getDescription(self):
        print(self.homePageContent)

