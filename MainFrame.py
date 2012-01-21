#!/usr/bin/env python3
#//==========================================================================//
#// Copyright (c) 2012 Wen-Han Gu. All rights reserved.
#//
#// Author: Nowar Gu (Wen-Han Gu)
#// E-mail: wenhan.gu <at> gmail.com
#//
#// Any advice is welcome. Thank you!
#//==========================================================================//

import tkinter

class MainFrame(tkinter.Frame):

  def __init__(self, pMaster=None, pGenerator=None):
    tkinter.Frame.__init__(self, pMaster)
    self.IDField = None
    self.IDText = tkinter.StringVar()
    self.GenBtn = None
    self.ExitBtn = None
    self.Generator = pGenerator
    self.pack()
    self.createAndInitWidgets()


  def createAndInitWidgets(self):
    self.IDField = tkinter.Entry(self)
    self.IDField["background"] = "white"
    self.IDField["textvariable"] = self.IDText
    self.IDField["width"] = 20
    self.IDField["justify"] = tkinter.CENTER
    self.IDField.pack(expand=False, padx="12", side="left")

    self.ExitBtn = tkinter.Button(self)
    self.ExitBtn["text"] = "Exit"
    self.ExitBtn["command"] = self.quit
    self.ExitBtn.pack(expand=False, side="right")

    self.GenBtn = tkinter.Button(self)
    self.GenBtn["text"] = "Generate"
    self.GenBtn["command"] = self.createNewID
    self.GenBtn.pack(expand=False, side="right")

    self.GenBtn.focus_set()


  def createNewID(self):
    self.IDText.set(self.Generator.gen())
