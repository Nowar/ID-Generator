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

import Generator
import MainFrame

if __name__ == "__main__":
  Master = tkinter.Tk(className="ID Generator")
  Gen = Generator.Generator()
  IDGenerator = MainFrame.MainFrame(Master, Gen)
  IDGenerator.mainloop()
