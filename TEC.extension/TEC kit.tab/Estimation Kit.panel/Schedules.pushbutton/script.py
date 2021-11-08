import os
import clr

from Autodesk.Revit import DB
from Autodesk.Revit import UI
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

clr.AddReference('System')

from pyrevit import UI
from pyrevit import script
from pyrevit import framework
from pyrevit.framework import wpf, Controls, Imaging

doc = __revit__.ActiveUIDocument.Document
t = Transaction(doc)
# t.Start("Change GT Title")
# t.Commit()

main_collector = FilteredElementCollector(doc)


schedules_collector = main_collector.OfCategory(BuiltInCategory.OST_Schedules)


myschedules = []

def get_schedule(schedule_name):
    for element in schedules_collector:
        # print(element.Name)
        if element.Name == schedule_name:
            myschedules.append(element)

get_schedule("8.EST_OSB_and_Sheathing")
get_schedule("5.EST_DryWall")
get_schedule("7.EST_Roofing")

osb_schedule = myschedules[0]
drywall_schedule = myschedules[1]
roofing_schedule = myschedules[2]

print("This is the name of the schedule", osb_schedule.Name)


items_of_schedule = FilteredElementCollector(doc, osb_schedule.Id)

print("here is the schedule itself", osb_schedule, "total items in this schedule's filter are ", items_of_schedule.GetElementCount())


item_list = []

# Filtering only Materials from the entire List
for item in items_of_schedule:
        # print(str(type(item)))
        # if str(type(item)) == "<type 'FamilyInstance'>":
        if str(type(item)) == "<type 'Material'>":
            item_list.append(item)


print("the total materials found in the schedule are", len(item_list))


count = 0
for i in item_list:
    name_of_i = i.Name
    if "Sheathing" in name_of_i:
        print(count, "Found")
        print(count, i)
    # else:
        # print(count, "Not Found")
    # print(count,"The item in the list" "the item is ", i, i.Name)
    count += 1



# print(osb_schedule.Outline)
# print(osb_schedule.ViewType)
# print(osb_schedule.GetMaterialIds())
# print(osb_schedule.ToElements())
# x = osb_schedule.ViewScheduleExportOptions
# x = osb_schedule.GetOrderedFilters()

# print("The number of columns are",  osb_schedule.Definition.GetFieldCount())
# print("The number of filters are", osb_schedule.Definition.GetFilterCount())

# osb_tabledata = osb_schedule.GetTableData()
# drywall_tabledata = drywall_schedule.GetTableData()
# roofing_tabledata = roofing_schedule.GetTableData()

# osb_table_body = osb_tabledata.GetSectionData(SectionType.Body)
# dry_table_body = drywall_tabledata.GetSectionData(SectionType.Body)
# roofing_table_body = roofing_tabledata.GetSectionData(SectionType.Body)


# print(osb_table_body.NumberOfRows, osb_table_body.NumberOfColumns)
# print(dry_table_body.NumberOfRows, dry_table_body.NumberOfColumns)
# print(roofing_table_body.NumberOfRows, roofing_table_body.NumberOfColumns)


# typecollector = FilteredElementCollector( osb_schedule.Document, osb_schedule.Id)
# number_of_types = typecollector.GetElementCount()
# print("total number of types are", number_of_types)

# inst_collector = FilteredElementCollector(osb_schedule.Document, osb_schedule.Id)
# inst_collector.WhereElementIsNotElementType()
# print("The numbker of instances that are not element type are", inst_collector.GetElementCount())





