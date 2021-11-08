# Push Data to CoverPage V0.1 <Code by ShivaReddy>.
from Autodesk.Revit import DB
from Autodesk.Revit import UI
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

__title__ = " Link Sheet Params\nto Global Params"
__author__ = "ShivaReddy"
doc = __revit__.ActiveUIDocument.Document
t = Transaction(doc)
# t.Start("Change GT Title")
# t.Commit()


# Let the Hacking begin


# GlobalParametersManager.GetAllGlobalParameters(doc)
g_p = GlobalParametersManager.GetAllGlobalParameters(doc)

global_parameters = []

for g in g_p:
	e = doc.GetElement(g)
	global_parameters.append(e)

def get_global_param_id(param_name):
	for g in global_parameters:
		if g.Name == param_name:
			return g.Id
			# print(g, g.Name, g.Id)


# Get all global params from the Element Ids given by the 'GlobalParametrsManager' class
# for i in range(len(global_parameters)):
	# myelement = doc.GetElement(global_parameters[i])
	# global_params.append(myelement)

sheet_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets)



def get_sheet(sheet_name):
	for s in sheet_collector:
		if (sheet_name) == (str(s.Name)):
			return s


cover_page =  get_sheet("COVER PAGE")


def link_params(page):

	# t.Start("Assign Global Params")

	for c in page.Parameters:

		if c.Definition.Name == "SF - AS DESIGNED - BASEMENT":
			g_id = get_global_param_id("SF - AS DESIGNED - BASEMENT")
			c.AssociateWithGlobalParameter(g_id)
		
		if c.Definition.Name == "SF - AS DESIGNED - FIRST FLOOR":
			g_id = get_global_param_id("SF - AS DESIGNED - FIRST FLOOR")
			c.AssociateWithGlobalParameter(g_id)

		if c.Definition.Name == "SF - AS DESIGNED - GARAGE":
			g_id = get_global_param_id("SF - AS DESIGNED - GARAGE")
			c.AssociateWithGlobalParameter(g_id)

		if c.Definition.Name == "SF - AS DESIGNED - SECOND FLOOR":
			g_id = get_global_param_id("SF - AS DESIGNED - SECOND FLOOR")
			c.AssociateWithGlobalParameter(g_id)

		if c.Definition.Name == "SF - AS DESIGNED - THIRD FLOOR":
			g_id = get_global_param_id("SF - AS DESIGNED - THIRD FLOOR")
			c.AssociateWithGlobalParameter(g_id)

		if c.Definition.Name == "SF - AS DESIGNED - TOTAL FIN":
			g_id = get_global_param_id("SF - AS DESIGNED - TOTAL FINISHED")
			c.AssociateWithGlobalParameter(g_id)

		if c.Definition.Name == "SF - AS DESIGNED - UNFINISHED":
			g_id = get_global_param_id("SF - AS DESIGNED - UNFINISHED")
			c.AssociateWithGlobalParameter(g_id)

		if c.Definition.Name == "SF - STD - BASEMENT":
			g_id = get_global_param_id("SF - STD - BASEMENT")
			c.AssociateWithGlobalParameter(g_id)

		if c.Definition.Name == "SF - STD - FIRST FLOOR":
			g_id = get_global_param_id("SF - STD - FIRST FLOOR")
			c.AssociateWithGlobalParameter(g_id)

		if c.Definition.Name == "SF - STD - GARAGE":
			g_id = get_global_param_id("SF - STD - GARAGE")
			c.AssociateWithGlobalParameter(g_id)

		if c.Definition.Name == "SF - STD - SECOND FLOOR":
			g_id = get_global_param_id("SF - STD - SECOND FLOOR")
			c.AssociateWithGlobalParameter(g_id)

		if c.Definition.Name == "SF - STD - THIRD FLOOR":
			g_id = get_global_param_id("SF - STD - THIRD FLOOR")
			c.AssociateWithGlobalParameter(g_id)

		if c.Definition.Name == "SF - STD - TOTAL FIN":
			g_id = get_global_param_id("SF - STD - TOTAL FINISHED")
			c.AssociateWithGlobalParameter(g_id)

		if c.Definition.Name == "SF - STD - UNFINISHED":
			g_id = get_global_param_id("SF - STD - UNFINISHED")
			c.AssociateWithGlobalParameter(g_id)
# others
		if c.Definition.Name == "County":
			g_id = get_global_param_id("COUNTY")
			c.AssociateWithGlobalParameter(g_id)

		if c.Definition.Name == "Eagle Project Name":
			g_id = get_global_param_id("EAGLE PROJECT NAME")
			c.AssociateWithGlobalParameter(g_id)

		if c.Definition.Name == "Lot Code":
			g_id = get_global_param_id("LOT CODE")
			c.AssociateWithGlobalParameter(g_id)

		if c.Definition.Name == "Lot Number":
			g_id = get_global_param_id("LOT NUMBER")
			c.AssociateWithGlobalParameter(g_id)

		if c.Definition.Name == "Neighborhood":
			g_id = get_global_param_id("NEIGHBORHOOD")
			c.AssociateWithGlobalParameter(g_id)

		if c.Definition.Name == "State":
			g_id = get_global_param_id("STATE")
			c.AssociateWithGlobalParameter(g_id)

		if c.Definition.Name == "Building Code":
			g_id = get_global_param_id("BUILDING CODE")
			c.AssociateWithGlobalParameter(g_id)

		if c.Definition.Name == "Construction Type":
			g_id = get_global_param_id("CONSTRUCTION TYPE")
			c.AssociateWithGlobalParameter(g_id)

		if c.Definition.Name == "Drawn Date":
			g_id = get_global_param_id("DRAWN DATE")
			c.AssociateWithGlobalParameter(g_id)

		if c.Definition.Name == "Eagle Revision Date":
			g_id = get_global_param_id("REVISION DATE")
			c.AssociateWithGlobalParameter(g_id)

		if c.Definition.Name == "Eagle Project Issue Date":
			g_id = get_global_param_id("ISSUE DATE")
			c.AssociateWithGlobalParameter(g_id)

	# t.Commit()



# for sheet in sheet_collector:
	# link_params(sheet)

def link_all_sheets():
	t.Start("Assign Global Params")
	for sheet in sheet_collector:
		link_params(sheet)
	t.Commit()


