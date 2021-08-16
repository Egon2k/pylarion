from workitem import workitem
from module import module
from pathlib import Path
import xml.etree.ElementTree as ET


class parser():
    workitems = dict()
    modules = dict()

    def parseWoritems(self, path):
        results = list(Path(path).rglob("workitem.xml"))

        for result in results:
            id = str(result).split("\\")[-2]

            tree = ET.parse(result)
            root = tree.getroot()

            for field in root.iter("field"):
                if field.attrib["id"] == "author":
                    author = field.text
                if field.attrib["id"] == "created":
                    created = field.text
                if field.attrib["id"] == "description":
                    description = field.text
                if field.attrib["id"] == "type":
                    type = field.text
                    

            self.workitems[id] = workitem(id = id,
                                          author = author,
                                          created =  created,
                                          description =  description,
                                          linkedWorkitems = [],
                                          type = type)
    
    def parseModules(self, path):
        results = list(Path(path).rglob("module.xml"))

        for result in results:
            tree = ET.parse(result)
            root = tree.getroot()

            for field in root.iter("field"):
                if field.attrib["id"] == "title":
                    title = field.text
                if field.attrib["id"] == "author":
                    author = field.text
                if field.attrib["id"] == "created":
                    created = field.text
                if field.attrib["id"] == "homePageContent":
                    homePageContent = field.text
                if field.attrib["id"] == "status":
                    status = field.text
                if field.attrib["id"] == "type":
                    type = field.text
        
            self.modules[title] = module(title = title,
                                        author = author,
                                        created = created,
                                        homePageContent = homePageContent,
                                        status = status,
                                        type = type)
    
    def getWorkitemById(self, id):
        return self.workitems[id]

    def getModuleByTitle(self, title):
        return self.modules[title]

if __name__ == "__main__":
    parser = parser()

    parser.parseWoritems("./checkout")
    parser.parseModules("./checkout")
    
    workitem = parser.getWorkitemById("RTB-2929")
    print(workitem.id)
    print(workitem.created)
    print(workitem.type)

    module = parser.getModuleByTitle("APP Software Specification")
    print(module.getDescription())
