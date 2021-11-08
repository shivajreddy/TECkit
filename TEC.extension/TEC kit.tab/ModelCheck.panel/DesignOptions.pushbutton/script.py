#Generate Design Options - V1 - </ShivaReddy>
import os
import clr
import collections

from Autodesk.Revit import DB
from Autodesk.Revit import UI
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI import Selection

from pyrevit import UI
from pyrevit import revit, DB
from pyrevit.revit.ui import *
from pyrevit.framework import List, wpf, Controls, Imaging

__title__ = "Design Options"
__author__ = "Shiva Reddy"

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
filePath = doc.PathName
fileTitle = doc.Title
head,split,tail = filePath.partition(fileTitle)
fileLocation = head
t = Transaction(doc)
# t.Start("Change GT Title")
# t.Commit()

###### LET THE HACKING BEGIN ######

designOptionsCollector = FilteredElementCollector(doc).OfClass(DesignOption)

designOptionSets = []
designOptions = []
primaryOptions = []

doDict = {e : (Element.Name.GetValue(doc.GetElement(e.get_Parameter(BuiltInParameter.OPTION_SET_ID).AsElementId()))) for e in designOptionsCollector}

newDict = sorted(doDict.items(), key=lambda kv: kv[1])

for i in newDict:
	list_i = list(i)
	list_i.append(i[0].Name)
	list_i.append(i[0].IsPrimary)
	designOptions.append(list_i)

for i in designOptionsCollector:
	e = doc.GetElement(i.get_Parameter(BuiltInParameter.OPTION_SET_ID).AsElementId())
	designSetName = Element.Name.GetValue(e)

	if(designSetName not in designOptionSets):
		designOptionSets.append(designSetName)

for i in designOptions:
	if i[3] == True:
		primaryOptions.append(i)

# print("this is the file location", fileLocation)

designOptionlocation = fileLocation + fileTitle +"DesignOptions.txt"
# print("this is the designoption file location", designOptionlocation)



file = open(designOptionlocation, 'w')
for i in primaryOptions:
	file.write(str(i) + "\n")
file.close()

myResult = "A total of {0} design options are found. \n Under {1} Design Sets. \n These are saved to {2}".format(len(designOptions), len(primaryOptions),designOptionlocation )
TaskDialog.Show("Generate Design Options", myResult)

# file = open(designOptionlocation, 'w')
# for i in primaryOptions:
# 	file.write("shiva")
# file.close()

