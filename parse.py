from workitem import workitem
from page import page
from pathlib import Path
import xml.etree.ElementTree as ET


class parser():
    workitems = dict()


    def parseWoritems(self, path):
        results = list(Path(path).rglob("workitem.xml"))

        for result in results:
            id = str(result).split('\\')[-2]

            tree = ET.parse(result)
            root = tree.getroot()

            for child in root.find('field'):
                print(child.__class__)

            self.workitems[id] = workitem(id = id,
                                          author = "user",
                                          created =  "01.01.1970",
                                          description =  "empty",
                                          linkedWorkitems = [],
                                          type = "workitem")

        #print(self.workitems)



if __name__ == "__main__":
    parser = parser()

    parser.parseWoritems('./checkout')
