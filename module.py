from dataclasses import dataclass
from bs4 import BeautifulSoup

@dataclass
class moduleElement():
    tag: str
    workitemId: str
    pass

@dataclass
class module():
    title: str
    author: str
    created: str
    homePageContent: str
    status: str
    type: str

    def getWorkitemList(self):
        moduleElements = list()

        soup = BeautifulSoup(self.homePageContent, 'html.parser')
        for element in soup.find_all(['div', 'h1', 'h2', 'h3']):
            tag = element.name
            id = element["id"]
            string = "params=id="
            start = id.find(string)

            if start != -1:
                workitemId = id[start + len(string):].split("|")[0]
                
                moduleElements.append(moduleElement(tag = tag, workitemId = workitemId))
        
        return moduleElements

