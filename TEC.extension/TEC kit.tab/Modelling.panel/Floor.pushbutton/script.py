#Automate FLoor Boundaries - V2.2 - </ShivaReddy>
import os
import clr

from Autodesk.Revit import DB
from Autodesk.Revit import UI
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI import Selection

from pyrevit import UI
from pyrevit import revit, DB
from pyrevit import forms
# from pyrevit.form import WPFWindow
from pyrevit.revit.ui import *
from pyrevit.framework import List, wpf, Controls, Imaging

__title__ = "Smart Floors"
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

def createFloor(thisRoom, floorType, currentLevel,):

	spatialElementBoundaryOptions = SpatialElementBoundaryOptions()

	myBoundaries = []
	myCurves = []
	myCurveArray = CurveArray()
	myCurveLoop = CurveLoop()
	myCurveLoopList = []

	myBoundaryList = thisRoom.GetBoundarySegments(spatialElementBoundaryOptions)
	for boundary in myBoundaryList[0]:
		myBoundaries.append(boundary)
		myCurve = boundary.GetCurve()
		myCurves.append(myCurve)
		myCurveArray.Append(myCurve)
		myCurveLoop.Append(myCurve)
	
	myCurveLoopList.append(myCurveLoop)

	floor = Floor.Create(doc, myCurveLoopList, floorType.Id, currentLevel.Id)
	# floor = doc.Create.NewFloor(myCurveArray, floorTypeId,currentLevelId,isStructural)
	return floor


def getRoomsCreateFloors():

	active = doc.ActiveView
	level = active.LookupParameter("Associated Level")

	if level == None:
		TaskDialog.Show("That is why you fail", "Only Jedi's can draw Floor's in any View")

	else:
	#Get Which Floor should be used to for creating Floors from Rooms
		floorTypes = FilteredElementCollector(doc).OfClass(FloorType).ToElements()
		
		chosenFloorTypeName = forms.CommandSwitchWindow.show([Element.Name.__get__(i) for i in floorTypes], message = "Pick Type of Floor to model")
		for i in floorTypes:
			if (Element.Name.__get__(i) == chosenFloorTypeName):
				chosenFloorType = i
		
		# print("chosen floor ->{}, {}".format(Element.Name.__get__(chosenFloorType), chosenFloorType))

		chosenFloorTypeThickness = chosenFloorType.LookupParameter("Default Thickness").AsDouble()

	# Get the current Level
		lvlCollector = FilteredElementCollector(doc).OfClass(Level).ToElements()
		
		for lvl in lvlCollector:
			if lvl.Name == level.AsString():
				presentLevel = lvl
				# presentId = lvl.Id

	# Get the Rooms at the current Floor
		roomCollector = FilteredElementCollector(doc).WhereElementIsNotElementType().OfClass(SpatialElement)
		currentViewRooms = []

		for room in roomCollector:
		#Checks |>| Location (checking if it is present in the active Design Option) |>| Type is a Room |>| Room's LevelId is the Current Level's Id
			if (room.Location != None) and (str(room.GetType()) == "Autodesk.Revit.DB.Architecture.Room") and (room.LevelId == presentLevel.Id):
				currentViewRooms.append(room)
			
		
		finalCurrentViewRoomNames = forms.SelectFromList.show([Element.Name.__get__(i) for i in currentViewRooms], title ="Select the Rooms to create Floors for", button_name = "OK", multiselect = True)
		
		finalCurrentViewRooms = []
		for name in finalCurrentViewRoomNames:
			for room in currentViewRooms:
				if Element.Name.__get__(room) == name:
					finalCurrentViewRooms.append(room)

		if chosenFloorType != None:
			# This is the start of creatign Floor's
			t.Start("Create Floors Using Rooms")
			for room in finalCurrentViewRooms:
				thisFloor = createFloor(room, floorType=chosenFloorType, currentLevel=presentLevel)
				# Increase the Floor offset height from the current level with the value of floor thickness
				((thisFloor.GetParameters("Height Offset From Level"))[0]).Set(chosenFloorTypeThickness)
				# set the Location Room parameter of these floors into the selected room
				try:
					(thisFloor.GetParameters("Location - Room"))[0].Set(Element.Name.__get__(room))
				except:
					print("No Parametere named \"Location - Room\"")

			t.Commit()

		print("Using [{}] as Floor Type, Created new Floors at Rooms: ".format(Element.Name.__get__(chosenFloorType)))

		print("{}".format(finalCurrentViewRoomNames))

getRoomsCreateFloors()
