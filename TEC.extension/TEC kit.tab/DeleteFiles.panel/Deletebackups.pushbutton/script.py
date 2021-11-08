#Delete Backup Revit Files - V1 -10/26/2021- </ShivaReddy>
import os
import clr

clr.AddReference('System')
clr.AddReference('System.Windows.Forms')
clr.AddReference('IronPython.Wpf')
clr.AddReference('PresentationCore')
clr.AddReference('PresentationFramework')


from Autodesk.Revit import DB
from Autodesk.Revit import UI 
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
from Autodesk.Revit.UI import Selection

from pyrevit import UI
from pyrevit import script
from pyrevit import revit, DB
from pyrevit.revit.ui import *
from pyrevit.framework import List, wpf, Controls, Imaging


import wpf
from System import Windows
from System.Windows import Media
import System.IO
import System.Windows
import Microsoft.Win32
import System.Windows.Controls as controls
import System.Windows.Media.Imaging

__title__ = "Delete Backups"
__author__ = "Shiva Reddy"
xaml_file_path = script.get_bundle_file('windowUI.xaml')
tec_logo_path = script.get_bundle_file('teclogo.png')



doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
t = Transaction(doc)
# t.Start("Change GT Title")
# t.Commit()

###### LET THE HACKING BEGIN ######

screenwidth = System.Windows.SystemParameters.PrimaryScreenWidth
screenheight = System.Windows.SystemParameters.PrimaryScreenHeight


allLFilePaths = []

def all_folders_rvt(path):
    listOfFilePaths = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if len(file) > 9:
                if (file.endswith(".rvt")):
                    if (file[-9] == "."):
                        listOfFilePaths.append(os.path.join(root, file))
    
    print(("Total BackUps found in \"{1}\" = {0}").format(len(listOfFilePaths), path))
    for path in listOfFilePaths:
        print(path)
        if path not in allLFilePaths:
            allLFilePaths.append(path)
    print("<--XXX-->")

def all_folders_rfa(path):

    listOfFilePaths = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if len(file) > 9:
                if (file.endswith(".rfa") and (file[-9] == ".")):
                    listOfFilePaths.append(os.path.join(root, file))
    
    print(("Total BackUps found in the parent folder = {0}").format(len(listOfFilePaths)))
    for path in listOfFilePaths:
        print(path)
        if path not in allLFilePaths:
            allLFilePaths.append(path)
    print("<--XXX-->")

                

class deletewindow(Windows.Window):

    pathString = ""


    def __init__(self):
        wpf.LoadComponent(self, xaml_file_path)
        self.Topmost = True
        self.Top = 0
        # self.WindowStartupLocation = Windows.WindowStartupLocation.CenterScreen
        self.Width = screenwidth * 0.6
        self.Height = screenheight * 0.4


    def dragmode(self, sender, e):
        self.DragMove()

    def browseButton(self, sender ,e):
        dialog = System.Windows.Forms.FolderBrowserDialog()
        result = dialog.ShowDialog()
        chosenPath = dialog.SelectedPath

        self.pathString = self.pathString[:0]
        self.filepath_1.Text = chosenPath
        self.pathString = self.pathString + chosenPath



    def findFilesButton(self, sender, e):

        if self.rb1.IsChecked == True:
            if len(self.pathString) > 0:
                all_folders_rvt(self.pathString)
            else:
                print("Make sure you select the PARENT FOLDER PATH")

        elif self.rb2.IsChecked == True:
            if len(self.pathString) > 0:
                all_folders_rfa(self.pathString)
            else:
                print("Make sure you select the PARENT FOLDER PATH")

        else:
            print("Make sure to Choose RVT or RFA files")


    def deleteFilesButton(self, sender, e):
        for file in allLFilePaths:
            print("the file is", file)
            # fileinfo = System.IO.FileInfo(file)
            # fileinfo.Delete()
            System.IO.File.Delete(file)
        print(("Operation Complete. Deleted a total of {0} backups").format(len(allLFilePaths)))


deletewindow().ShowDialog()