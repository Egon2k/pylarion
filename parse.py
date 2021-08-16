from workitem import workitem
from module import module, moduleElement
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

            values = self.__getValuesFromWorkitem(root, ['title', 
                                                         'author', 
                                                         'created', 
                                                         'description',
                                                         'type'])

            self.workitems[id] = workitem(id = id,
                                          title = values['title'],
                                          author = values['author'],
                                          created =  values['created'],
                                          description =  values['description'],
                                          linkedWorkitems = [],
                                          type = values['type'])
    
    def parseModules(self, path):
        results = list(Path(path).rglob("module.xml"))

        for result in results:
            tree = ET.parse(result)
            root = tree.getroot()

            values = self.__getValuesFromWorkitem(root, ['title', 
                                                         'author', 
                                                         'created', 
                                                         'homePageContent',
                                                         'status',
                                                         'type'])
            
            self.modules[values['title']] = module(title = values['title'],
                                                   author = values['author'],
                                                   created = values['created'],
                                                   homePageContent = values['homePageContent'],
                                                   status = values['status'],
                                                   type = values['type'])

    def __getValuesFromWorkitem(self, root, attributes):
        values = dict()
        
        for field in root.iter("field"):
            if field.attrib["id"] in attributes:
                values[field.attrib["id"]] = field.text

        # fill all other entries in the dict with empty string
        for attribute in attributes:
            if attribute not in values:
                values[attribute] = ""
        return values

    def getWorkitemsDict(self):
        return self.workitems
    
    def getWorkitemById(self, id):
        return self.workitems[id]

    def getModuleByTitle(self, title):
        return self.modules[title]

if __name__ == "__main__":
    parser = parser()

    parser.parseWoritems("./checkout")
    parser.parseModules("./checkout")

    workitems = parser.getWorkitemsDict()
    
    workitem = parser.getWorkitemById("RTB-2929")
    print(workitem.id)
    print(workitem.created)
    print(workitem.type)

    module = parser.getModuleByTitle("APP Software Specification")
    moduleElements = module.getWorkitemList()

    
    content = ''

    content += '<html><body>\n'
    for moduleElement in moduleElements:
        content += f'<{moduleElement.tag}>'
        content += workitems[moduleElement.workitemId].id + " - " + workitems[moduleElement.workitemId].title
        
        if workitems[moduleElement.workitemId].description != "":
            content += '<p>'
            content += workitems[moduleElement.workitemId].description
            content += '</p>'
        content += f'</{moduleElement.tag}>\n'
    content += '</body></html>\n'
    
    f = open("index.html", "w")
    f.write(content)
    f.close()
    