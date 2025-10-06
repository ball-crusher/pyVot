#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

##This file is part of PyVot
#############################################################################
#############################################################################
##                                                                         ##
##                                   Options                               ##
##                                                                         ##
#############################################################################
#############################################################################

## Copyright (C) 2006-2009 Cédrick FAURY

#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA


import ConfigParser
import Const
import os,os.path,sys
import wx
import wx.combo
import globdef
import ElementTable
import Elements
import wx.lib.customtreectrl as CT


##############################################################################
#      Options     #
##############################################################################
class Options:
    "Définit les options de PyVot"
    def __init__(self):
        #
        # Toutes les options ...
        # Avec leurs valeurs par défaut.
        #
        self.optElements = {"ProprietesDefaut"   : 0,
                            "FichierProprietes"  : ""}
        
        self.optAnalyse = {"AnimMontage" : True,
                           "AnimArrets"  : True,
                           "ChaineAction" : True}
        
        self.optGenerales = {"TypeAide" : 0,
                             "RepCourant" : globdef.SAMPLEPATH,
                             "OngletMontage" : False,
                             "Hachurer" : globdef.HACHURER_EN_EDITION}
        
        self.optImpression = {"DemanderImpr" : False,
                              "ImpMontage" : True,
                              "ImpCdCFCharge" : False,
                              "ImpCdCFEtanch" : False,
                              "ImpCdCFCout" : False,
                              "ImpAnImmob" : True,
                              "ImpAnResistAx" : True,
                              "ImpAnResistRl" : True,
                              "ImpAnMontabEns" : True,
                              "ImpAnMontabRlt" : True,
                              "ImpAnEtanch" : True,
                              "ImpAnStruc" : True,
                              "ImpAnCout" : True} #os.path.dirname(os.path.abspath(sys.argv[0]))+"\\ModeleRapport.txt"}
        
        self.typesOptions = {u"General" : self.optGenerales,
                             u"Elements" : self.optElements,
                             u"Report" : self.optImpression,
                             u"Analysis" : self.optAnalyse}
        
        # Le fichier où seront sauvées les options
        self.fichierOpt = "ConfigPyVot.cfg"

    def __repr__(self):
        t = "Options :\n"
        for o in self.optAnalyse.items() + self.optGenerales.items() + self.optImpression.items():
            if type(o[1]) == int:
                tt = str(o[1])
            elif type(o[1]) == bool:
                tt = str(o[1])
            else:
                tt = o[1]
            t += "\t" + o[0] + " = " + tt +"\n"
        return t
    
    ############################################################################
    def fichierExiste(self):
        """ Vérifie si le fichier "options" existe
        """
#        PATH=os.path.dirname(os.path.abspath(sys.argv[0]))
        os.chdir(globdef.PATH)
        if os.path.isfile(self.fichierOpt):
            return True
        return False

    ############################################################################
    def enregistrer(self):
        """" Enregistre les options dans un fichier
        """
        
#        print "Enregistrement",self
        
#        PATH=os.path.dirname(os.path.abspath(sys.argv[0]))
        os.chdir(globdef.PATH)
        config = ConfigParser.ConfigParser()

        for titre,dicopt in self.typesOptions.items():
            titre = titre.encode('utf-8')
#            print titre
            config.add_section(titre)
            for opt in dicopt.items():
                config.set(titre, opt[0],opt[1])
            
            
#        config.add_section('Options generales')
#       
#        config.add_section('Options analyse')
#        config.set('Options analyse', 'animMont', self.proposerAnimMont.get())
#        config.set('Options analyse', 'animArret', self.proposerAnimArret.get())
#        config.set('Options analyse', 'traceChaines', self.proposerChaines.get())
#
#        config.add_section('Options aide')
#        config.set('Options aide', 'type', self.typeAide.get())
#
#        config.add_section('Dossiers')
#        config.set('Dossiers', 'repcourant', self.repertoireCourant.get())
        
        config.write(open(self.fichierOpt,'w'))



    ############################################################################
    def ouvrir(self):
        "Ouvre un fichier d'options"
##        print "Ouvre Options"
#        PATH=os.path.dirname(os.path.abspath(sys.argv[0]))
        os.chdir(globdef.PATH)
        config = ConfigParser.ConfigParser()
        config.read(self.fichierOpt)
        
        for titre in self.typesOptions.keys():
            titreUtf = titre.encode('utf-8')
            for titreopt in self.typesOptions[titre].keys():
                opt = self.typesOptions[titre][titreopt] 
                if type(opt) == int:
                    opt = config.getint(titreUtf, titreopt)
                elif type(opt) == bool:
                    opt = config.getboolean(titreUtf, titreopt)
                elif type(opt) == str:
                    opt = config.get(titreUtf, titreopt)
                self.typesOptions[titre][titreopt] = opt
                
#        print "Ouverture",self


    ############################################################################
    def copie(self):
        """ Retourne une copie des options """
        options = Options()
        for titre,dicopt in self.typesOptions.items():
            titre.encode('utf-8')
            for opt in dicopt.items():
                options.typesOptions[titre][opt[0]] = opt[1]
        return options
                
#        self.proposerAnimMont.set(options.proposerAnimMont.get())
#        self.proposerAnimArret.set(options.proposerAnimArret.get())
#        self.proposerChaines.set(options.proposerChaines.get())
#        self.typeAide.set(options.typeAide.get())
#        self.repertoireCourant.set(options.repertoireCourant.get())

        
    ############################################################################
    def defaut(self):
        return
#        self.proposerAnimMont.set(1)
#        self.proposerAnimArret.set(1)
#        self.proposerChaines.set(1)
#        self.typeAide.set(0)
#        self.repertoireCourant.set("Exemples/")

    ###########################################################################
    def extraireRepertoire(self,chemin):
        for i in range(len(chemin)):
            if chemin[i] == "/":
                p = i
        self.repertoireCourant = chemin[:p+1]
        return chemin[:p+1]
        
##############################################################################
#     Fenêtre Options     #
##############################################################################
class FenOptions(wx.Dialog):
#   "Fenêtre des options"      
    def __init__(self, parent, options):
        wx.Dialog.__init__(self, parent, -1, u"PyVot options")#, style = wx.RESIZE_BORDER)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        nb = nbOptions(self, options)
        sizer.Add(nb, flag = wx.EXPAND)#|wx.ALL)
        
        btnsizer = wx.StdDialogButtonSizer()
        
        if wx.Platform != "__WXMSW__":
            btn = wx.ContextHelpButton(self)
            btnsizer.AddButton(btn)
        
        btn = wx.Button(self, wx.ID_OK)
        btn.SetHelpText(u"Save the changes")
        btn.SetDefault()
        btnsizer.AddButton(btn)

        btn = wx.Button(self, wx.ID_CANCEL)
        btn.SetHelpText(u"Cancel the changes")
        btnsizer.AddButton(btn)
        btnsizer.Realize()
        
        sizer.Add(btnsizer, flag = wx.EXPAND)#|wx.ALL)
        self.SetMinSize((350,-1))
#        print self.GetMinSize()
#        self.SetSize(self.GetMinSize())
        self.SetSizerAndFit(sizer)
        
class pnlGenerales(wx.Panel):
    def __init__(self, parent, optGene):
        
        wx.Panel.__init__(self, parent, -1)
        
        self.opt = optGene
        
        ns = wx.BoxSizer(wx.VERTICAL)
        
        #
        # Choix du dossier de sauvegarde par défaut
        #
        sb1 = wx.StaticBox(self, -1, u"Default save folder", size = (200,-1))
        sbs1 = wx.StaticBoxSizer(sb1,wx.VERTICAL)
        fs = DirSelectorCombo(self, -1)
        fs.SetValueWithEvent(self.opt["RepCourant"])
        fs.SetToolTip(wx.ToolTip(u"Select the folder where *.pyv files are saved\nwhen PyVot starts. Later, the proposed folder\nwill be the last one used for a save."))
        sbs1.Add(fs, flag = wx.EXPAND|wx.ALL, border = 5)
        fs.Bind(wx.EVT_TEXT, self.EvtComboCtrl)
        ns.Add(sbs1, flag = wx.EXPAND|wx.ALL)
        
        #
        # Choix du type de fichier d'aide à afficher
        #
        rb1 = wx.RadioBox(self, -1, u"Help file type", wx.DefaultPosition, wx.DefaultSize,
                          ["CHM","HTML"], 1, wx.RA_SPECIFY_COLS)
        rb1.SetSelection(self.opt["TypeAide"])
        rb1.SetToolTip(wx.ToolTip(u"Depending on your system,\nthe help file may not display correctly.\nThis option can solve the problem."))
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, rb1)
        ns.Add(rb1, flag = wx.EXPAND|wx.ALL)
        
        #
        # Option "arbre de structure"
        #
        sb2 = wx.StaticBox(self, -1, u'"Project" tab', size = (200,-1))
        sbs2 = wx.StaticBoxSizer(sb2,wx.VERTICAL)
        cb1 = wx.CheckBox(self, -1, u'Show a "Project" tab')
        cb1.SetToolTip(wx.ToolTip(u'When enabled, a "Project" tab is displayed\non the left side of the assembly.'))
        cb1.SetValue(self.opt["OngletMontage"])
        sbs2.Add(cb1, flag = wx.EXPAND|wx.ALL, border = 5)
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBoxOnglet, cb1)
        ns.Add(sbs2, flag = wx.EXPAND|wx.ALL)
        
        #
        # Option "Affichage"
        #
        sb3 = wx.StaticBox(self, -1, u"Display", size = (200,-1))
        sbs3 = wx.StaticBoxSizer(sb3,wx.VERTICAL)
        cb2 = wx.CheckBox(self, -1, u"Hatch during placement")
        cb2.SetToolTip(wx.ToolTip(u"If unchecked, parts are hatched only after\nyou click to place them.\n\nThis can improve display performance."))
        cb2.SetValue(self.opt["Hachurer"])
        sbs3.Add(cb2, flag = wx.EXPAND|wx.ALL, border = 5)
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBoxHachurer, cb2)
        ns.Add(sbs3, flag = wx.EXPAND|wx.ALL)
        
        #
        self.SetSizerAndFit(ns)
        
        
    
    def EvtRadioBox(self, event):
        self.opt["TypeAide"] = event.GetInt()
        
    def EvtComboCtrl(self, event):
        self.opt["RepCourant"] = event.GetEventObject().GetValue()
        
    def EvtCheckBoxOnglet(self, event):
        dlg = wx.MessageDialog(self, u"This option will take effect after restarting the application",
                               u'"Project" tab option',
                               wx.OK | wx.ICON_INFORMATION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()
        self.opt["OngletMontage"] = event.GetEventObject().GetValue()
        
    def EvtCheckBoxHachurer(self, event):
        self.opt["Hachurer"] = event.GetEventObject().GetValue()


#######################################################################################################
class pnlElements(wx.Panel):
    def __init__(self, parent, optElem):
        
        wx.Panel.__init__(self, parent, -1)
        
        self.opt = optElem
        
        ns = wx.BoxSizer(wx.VERTICAL)
        
        #
        # Choix du fichier de propriété des éléments
        #
        self.sb2 = wx.StaticBox(self, -1, u"Custom properties")
        sbs2 = wx.StaticBoxSizer(self.sb2,wx.VERTICAL)
        
        fileList = ElementTable.listeFichiersElem()
        self.cb = wx.ComboBox(self, 500, self.opt["FichierProprietes"], (90, 50), 
                         (160, -1), fileList,
                         wx.CB_DROPDOWN
                         #| wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )
        
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.cb)
        self.cb.SetToolTip(wx.ToolTip(u"Select the element property file"))
        sbs2.Add(self.cb)
        
        bs1 = wx.BoxSizer(wx.HORIZONTAL)
        self.b1 = wx.Button(self, 10, u"New")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.b1)
        self.b2 = wx.Button(self, 11, u"Edit")
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.b2)
        bs1.Add(self.b1)
        bs1.Add(self.b2)
        sbs2.Add(bs1)
        sbs2.Layout()
        
        #
        # Choix de l'origine des propriétés
        #
        sb1 = wx.StaticBox(self, -1, u"Element properties", size = (200,-1))
        sbs1 = wx.StaticBoxSizer(sb1,wx.VERTICAL)
        
        self.group1_ctrls = []
        radio1 = wx.RadioButton( self, 0, u"Default", style = wx.RB_GROUP )
        radio2 = wx.RadioButton( self, 1, u"Custom")
        radio2.SetValue(self.opt["ProprietesDefaut"])

        self.group1_ctrls.append((radio1,None))
        self.group1_ctrls.append((radio2, self.sb2))
        
#        rb1.SetSelection(self.opt["ProprietesDefaut"])
        sb1.SetToolTip(wx.ToolTip(u"Default: PyVot uses built-in element properties.\nCustom: choose your own properties for the elements."))
        
        grid2 = wx.GridBagSizer()
        grid2.Add( radio1, (0,0), (1,1), wx.ALIGN_LEFT|wx.LEFT|wx.RIGHT|wx.TOP, 5 )
        grid2.Add( radio2, (1,0), (1,1), wx.ALIGN_LEFT|wx.LEFT|wx.RIGHT|wx.TOP, 5 )
        grid2.Add( sbs2, (1,1), (1,1), wx.ALIGN_CENTRE|wx.LEFT|wx.RIGHT|wx.TOP, 5 )
        
        for radio, text in self.group1_ctrls:
            self.Bind(wx.EVT_RADIOBUTTON, self.EvtRadioBox, radio )
        
        sbs1.Add(grid2)
        sbs1.Layout()
        ns.Add(sbs1, flag = wx.EXPAND|wx.ALL)
        
        self.EvtRadioBox()
        #
        self.SetSizerAndFit(ns)
        
    
    def OnClick(self, event):
        # Nouveau
        if event.GetId() == 10: 
            frame = ElementTable.ElementGridFrame(self, Elements.listeElements, Elements.listeFamilles,
                                                  fichier = wx.GetApp().auteur)
        
        # Editer
        elif event.GetId() == 11:
            frame = ElementTable.ElementGridFrame(self, fichier = self.cb.GetValue())
        frame.Show(True)
        
        
    def SetFichier(self, fichier):
        self.opt["FichierProprietes"] = fichier
        self.cb.SetValue(self.opt["FichierProprietes"])
    
    
    def EvtRadioBox(self, event = None):
        if event != None:
#            print "Radio",event.GetId()
            self.opt["ProprietesDefaut"] = event.GetId()
        
        if self.opt["ProprietesDefaut"] == 0:
            self.sb2.Enable(False)
            self.cb.Enable(False)
            self.b1.Enable(False)
            self.b2.Enable(False)
        else:
            self.sb2.Enable(True)
            self.cb.Enable(True)
            self.b1.Enable(True)
            self.b2.Enable(True)
        
    def EvtComboBox(self, event):
        self.opt["FichierProprietes"] = event.GetEventObject().GetValue()
        

     
class pnlImpression(wx.Panel):
    def __init__(self, parent, opt):
        wx.Panel.__init__(self, parent, -1)
        ns = wx.BoxSizer(wx.VERTICAL)
        self.opt = opt
        
        sb1 = wx.StaticBox(self, -1, u"Report content", size = (200,-1))
        sbs1 = wx.StaticBoxSizer(sb1,wx.VERTICAL)
        tree = ChoixRapportTreeCtrl(self, self.opt)
        sbs1.Add(tree, 1, flag = wx.EXPAND|wx.ALL, border = 5)
        
#        print tree.GetVirtualSize()[1], tree.GetBestSize()[1]
        
        cb2 = wx.CheckBox(self, -1, u"Ask what to include\nfor each new report")
        cb2.SetValue(self.opt["DemanderImpr"])
        
        sbs1.Add(cb2, flag = wx.EXPAND|wx.ALL, border = 5)
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, cb2)
        
        ns.Add(sbs1, flag = wx.EXPAND|wx.ALL)
        self.SetSizerAndFit(ns)
        sb1.SetMinSize((-1, 130))
        
#    def EvtComboCtrl(self, event):
#        self.opt["FichierMod"] = event.GetEventObject().GetValue()
    
    def EvtCheckBox(self, event):
        self.opt["DemanderImpr"] = event.IsChecked()
     
class pnlAnalyse(wx.Panel):
    def __init__(self, parent, options):
        wx.Panel.__init__(self, parent, -1)
        ns = wx.BoxSizer(wx.VERTICAL)
        self.options = options
        
        sb1 = wx.StaticBox(self, -1, u"Visual analysis tools")
        sbs1 = wx.StaticBoxSizer(sb1,wx.VERTICAL)
        
        label = {"AnimMontage"  : u"Suggest the disassembly/reassembly animation",
                 "AnimArrets"   : u"Suggest the animation for missing axial stops",
                 "ChaineAction" : u"Suggest plotting action chains"}

        self.cb = {}
        for titre, opt in options.items():
            c = wx.CheckBox(self, -1, label[titre])
            self.cb[c.GetId()] = titre
            c.SetValue(opt)
            self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, c)
            sbs1.Add(c, flag = wx.ALL, border = 5)
        
        ns.Add(sbs1, flag = wx.EXPAND)

        self.SetSizerAndFit(ns)

    def EvtCheckBox(self, event):
        self.options[self.cb[event.GetId()]] = event.IsChecked()
        

class nbOptions(wx.Notebook):
    def __init__(self, parent, options):
        wx.Notebook.__init__(self, parent, -1)
        
        self.AddPage(pnlGenerales(self, options.optGenerales), u"General")
        self.AddPage(pnlElements(self, options.optElements), u"Elements")
        self.AddPage(pnlImpression(self, options.optImpression), u"Report")
        self.AddPage(pnlAnalyse(self, options.optAnalyse), u"Analysis")
        self.SetMinSize((350,-1))
            
class DirSelectorCombo(wx.combo.ComboCtrl):
    def __init__(self, *args, **kw):
        wx.combo.ComboCtrl.__init__(self, *args, **kw)

        # make a custom bitmap showing "..."
        bw, bh = 14, 16
        bmp = wx.EmptyBitmap(bw,bh)
        dc = wx.MemoryDC(bmp)

        # clear to a specific background colour
        bgcolor = wx.Colour(255,254,255)
        dc.SetBackground(wx.Brush(bgcolor))
        dc.Clear()

        # draw the label onto the bitmap
        label = "..."
        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        dc.SetFont(font)
        tw,th = dc.GetTextExtent(label)
        dc.DrawText(label, (bw-tw)/2, (bw-tw)/2)
        del dc

        # now apply a mask using the bgcolor
        bmp.SetMaskColour(bgcolor)

        # and tell the ComboCtrl to use it
        self.SetButtonBitmaps(bmp, True)
        

    # Overridden from ComboCtrl, called when the combo button is clicked
    def OnButtonClick(self):
        # In this case we include a "New directory" button. 
#        dlg = wx.FileDialog(self, "Choisir un fichier modèle", path, name,
#                            "Rich Text Format (*.rtf)|*.rtf", wx.FD_OPEN)
        dlg = wx.DirDialog(self, "Choisir un dossier",
                           defaultPath = globdef.SAMPLEPATH,
                           style = wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )

        # If the user selects OK, then we process the dialog's data.
        # This is done by getting the path data from the dialog - BEFORE
        # we destroy it. 
        if dlg.ShowModal() == wx.ID_OK:
            self.SetValue(dlg.GetPath())

        # Only destroy a dialog after you're done with it.
        dlg.Destroy()
        
        self.SetFocus()

    # Overridden from ComboCtrl to avoid assert since there is no ComboPopup
    def DoSetPopupControl(self, popup):
        pass

class FileSelectorCombo(wx.combo.ComboCtrl):
    def __init__(self, *args, **kw):
        wx.combo.ComboCtrl.__init__(self, *args, **kw)

        # make a custom bitmap showing "..."
        bw, bh = 14, 16
        bmp = wx.EmptyBitmap(bw,bh)
        dc = wx.MemoryDC(bmp)

        # clear to a specific background colour
        bgcolor = wx.Colour(255,254,255)
        dc.SetBackground(wx.Brush(bgcolor))
        dc.Clear()

        # draw the label onto the bitmap
        label = "..."
        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        dc.SetFont(font)
        tw,th = dc.GetTextExtent(label)
        dc.DrawText(label, (bw-tw)/2, (bw-tw)/2)
        del dc

        # now apply a mask using the bgcolor
        bmp.SetMaskColour(bgcolor)

        # and tell the ComboCtrl to use it
        self.SetButtonBitmaps(bmp, True)
        

    # Overridden from ComboCtrl, called when the combo button is clicked
    def OnButtonClick(self):
        # In this case we include a "New directory" button.
        path = os.path.dirname(os.path.abspath(sys.argv[0]))
        os.chdir(path)
        name = ""
        mesFormats = "Texte brut (*.txt)|*.txt|" \
                     "Rich Text Format (*.rtf)|*.rtf" 
                     
        dlg = wx.FileDialog(self, u"Choose a template file", path, name,
                            mesFormats, wx.FD_OPEN)

        # If the user selects OK, then we process the dialog's data.
        # This is done by getting the path data from the dialog - BEFORE
        # we destroy it. 
        if dlg.ShowModal() == wx.ID_OK:
            self.SetValue(dlg.GetPath())

        # Only destroy a dialog after you're done with it.
        dlg.Destroy()
        
        self.SetFocus()


    # Overridden from ComboCtrl to avoid assert since there is no ComboPopup
    def DoSetPopupControl(self, popup):
        pass

##############################################################################
#     Choix des trucs à mettre dans le rapport     #
##############################################################################
class ChoixRapportTreeCtrl(CT.CustomTreeCtrl):

    def __init__(self, parent, optImpr):

        CT.CustomTreeCtrl.__init__(self, parent, -1, 
                                   style = wx.WANTS_CHARS| wx.SUNKEN_BORDER ,
                                   agwStyle = CT.TR_HIDE_ROOT | 
                                   CT.TR_HAS_BUTTONS | CT.TR_HAS_VARIABLE_ROW_HEIGHT | 
                                   CT.TR_AUTO_CHECK_CHILD | CT.TR_AUTO_CHECK_PARENT)

        self.optImpr = optImpr
        
        self.structure = [[u"Assembly", "ImpMontage"],
                          [u"Functional spec",    [[u"Loads on the shaft",         "ImpCdCFCharge"],
                                        [u"Lubrication & sealing",  "ImpCdCFEtanch"],
                                        [u"Allowed cost",             "ImpCdCFCout"]]],
                          [u"Analysis", [[u"Structure", [[u"Axial positioning", "ImpAnImmob"],
                                                        [u"Diagram","ImpAnStruc"]]],
                                        [u"Strength",[[u"Axial", "ImpAnResistAx"],
                                                        [u"Bearings","ImpAnResistRl"]]],
                                        [u"Assemblability",[[u"Assembly", "ImpAnMontabEns"],
                                                         [u"Bearings","ImpAnMontabRlt"]]],
                                        [u"Sealing", "ImpAnEtanch"],
                                        [u"Cost", "ImpAnCout"]]]
                          ]

        self.root = self.AddRoot("")
        self.par ={}

        self.ConstructionFinie = False

        def AppendBranch(parent, lst):
#            branch = []
            for b in lst:
                
                if type(b[1]) == list:
                    self.par[b[0]] = self.AppendItem(parent, b[0], ct_type = 1, data = None)
                    AppendBranch(self.par[b[0]], b[1])
#                    branch.append([item, br])
#                    self.SetItemPyData(item, None)
                else:
                    item = self.AppendItem(parent, b[0], ct_type = 1, data = b[1])
#                    branch.append([item, b[1]])
#                    self.SetItemPyData(item, b[1])
                    if optImpr[b[1]]:
                        self.CheckItem(item, True)
            return True
        
        self.ConstructionFinie = AppendBranch(self.root, self.structure)
        self.EtatCdCF = self.IsItemChecked(self.par[u"CdCF"])
        self.GererEtats()
        
        self.Bind(CT.EVT_TREE_ITEM_CHECKED, self.OnItemCheck)
        
        self.ExpandAll()
        self.Fit()
        self.Refresh()
        
#        self.AdjustSize()

    def AdjustSize(self):
#        print self.GetBestSize(), self.GetVirtualSize()
#        self.InvalidateBestSize()
#        self.SetVirtualSize(self.GetBestSize())
        self.SetBestSize((self.GetBestSize()[0]+4, 134))
        self.SendSizeEvent()
#        print self.GetBestSize(), self.GetVirtualSize()

    def OnItemCheck(self, event):
        if self.ConstructionFinie:
            item = event.GetItem()
            self.Maj(item)
            if item != self.par[u"CdCF"]:
                self.GererEtats()
            event.Skip()

    def Maj(self, item):
        nc = self.GetChildrenCount(item, False)
        
        child, cookie = self.GetFirstChild(item)
        cookie  =1
        for c in range(nc):
            self.Maj(child)
            child, cookie = self.GetNextChild(item, cookie)
#            yield child

#        print self.GetItemPyData(item)
        if self.GetItemPyData(item) != None:
            self.optImpr[self.GetItemPyData(item)] = self.IsItemChecked(item)
        
    def GererEtats(self):
        if self.IsItemChecked(self.par[u"Analyse"]):
            self.EtatCdCF = self.IsItemChecked(self.par[u"CdCF"])
            self.CheckItem2(self.par[u"CdCF"], False)
            self.par[u"CdCF"].Enable(False)
        else:
            self.par[u"CdCF"].Enable(True)
            self.CheckItem2(self.par[u"CdCF"], self.EtatCdCF)
        
        self.Refresh()
        
        
class FenOptionsImpression(wx.Dialog):
#   "Fenêtre des options"      
    def __init__(self, parent, optionsImpr):
        wx.Dialog.__init__(self, parent, -1, u"Create analysis report")#, style = wx.RESIZE_BORDER)
        self.SetMinSize((400,300))
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        txt = wx.StaticText(self, -1, u"Select the report content:")
        sizer.Add(txt, flag = wx.EXPAND|wx.ALL, border = 5)
        
        tree = ChoixRapportTreeCtrl(self, optionsImpr)
        sizer.Add(tree, 1, flag = wx.EXPAND|wx.ALL, border = 5)
        
        btnsizer = wx.StdDialogButtonSizer()
        
#        if wx.Platform != "__WXMSW__":
#            btn = wx.ContextHelpButton(self)
#            btnsizer.AddButton(btn)
        
        btn = wx.Button(self, wx.ID_OK, "Continue")
        btn.SetHelpText(u"Continue creating the report")
        btn.SetDefault()
        btnsizer.AddButton(btn)

        btn = wx.Button(self, wx.ID_CANCEL, "Cancel")
        btn.SetHelpText(u"Cancel report creation")
        btnsizer.AddButton(btn)
        btnsizer.Realize()
        
        sizer.Add(btnsizer, flag = wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL)#|wx.ALL)
#        self.SetMinSize((350,-1))
#        print self.GetMinSize()
#        self.SetSize(self.GetMinSize())
        self.SetSizer(sizer)

##############################################################################
#     Fenêtre Options     #
##############################################################################
#class FenOptions(Toplevel):
#    "Fenêtre des options"
#    def __init__(self, master, options):
#        Toplevel.__init__(self,master)
#        self.withdraw()
#        self.transient(master)
#        self.focus_set()
#        self.grab_set()
#        self.title(u"Options")
###        self.iconbitmap(Images.Icone_Fenetre)
#        self.geometry("+500+250")
#        self.master = master
#        # Options
#        self.options = options
#
#        # Options provisoires
#        self.optionsProv = Options()
#        self.optionsProv.copie(self.options)
#       
#        ################################################################################
#        zoneOptionsGenerales = gui.ZoneAffichage(self, titre = u"Options Générales", bg = "SystemButtonFace")
#        zoneOptionsGenerales.grid(row = 0, column = 0, padx = 5, pady = 5, columnspan = 2)
#        
###        Label(zoneOptionsGenerales, text = u"Options Générales",
###                    font = Const.Font_Titre[0],
###                    fg = Const.Font_Titre[1]) \
###            .grid(column = 1, row = 0, padx = 2, pady = 2,  columnspan = 2, \
###                  sticky = W)
#
###        Checkbutton(zoneOptionsGenerales, \
###                    text = u"Autoriser les montages à un seul roulement", \
###                    variable = self.optionsProv.roulementUnique) \
###                    .grid(column = 1, row = 1, columnspan = 2, \
###                                  padx = 4, pady = 2, sticky = W)
#
#
#        ################################################################################
#        zoneOptionsAnalyse = gui.ZoneAffichage(self, titre = u"Options d'Analyse", bg = "SystemButtonFace")
#        zoneOptionsAnalyse.grid(row = 1, column = 0, padx = 5, pady = 5, columnspan = 2)
#        
###        Label(zoneOptionsAnalyse, text = u"Options d'Analyse",
###                    font = Const.Font_Titre[0],
###                    fg = Const.Font_Titre[1]) \
###            .grid(column = 1, row = 0, padx = 2, pady = 2,  columnspan = 2, \
###                  sticky = W)
#
#        Checkbutton(zoneOptionsAnalyse, \
#                    text = u"Proposer l'animation des éléments non arrêtés", \
#                    variable = self.optionsProv.proposerAnimArret) \
#                    .grid(column = 1, row = 1, columnspan = 2, \
#                                  padx = 4, pady = 2, sticky = W)
#        
#        Checkbutton(zoneOptionsAnalyse, \
#                    text = u"Proposer le tracé des chaînes d'action", \
#                    variable = self.optionsProv.proposerChaines) \
#                    .grid(column = 1, row = 2, columnspan = 2, \
#                                  padx = 4, pady = 2, sticky = W)
#        
#        Checkbutton(zoneOptionsAnalyse, \
#                    text = u"Proposer l'animation du Montage/Démontage", \
#                    variable = self.optionsProv.proposerAnimMont) \
#                    .grid(column = 1, row = 3, columnspan = 2, \
#                                  padx = 4, pady = 2, sticky = W)
#        
#
#        ################################################################################
#        zoneOptionsAide = gui.ZoneAffichage(self, titre = u"Options d'Aide", bg = "SystemButtonFace")
#        zoneOptionsAide.grid(row = 2, column = 0, padx = 5, pady = 5, columnspan = 2)
#        
###        Label(zoneOptionsAide, text = u"Options d'Aide",
###                    font = Const.Font_Titre[0],
###                    fg = Const.Font_Titre[1]) \
###            .grid(column = 1, row = 0, padx = 2, pady = 2,  columnspan = 2, \
###                  sticky = W)
#
#        Radiobutton(zoneOptionsAide, \
#                    text = u"Aide au format .CHM",
#                    value = 0,
#                    variable = self.optionsProv.typeAide) \
#                    .grid(column = 1, row = 1, columnspan = 2, \
#                                  padx = 4, pady = 2, sticky = W)
#
#        Radiobutton(zoneOptionsAide, \
#                    text = u"Aide au format .HTML",
#                    value = 1,
#                    variable = self.optionsProv.typeAide) \
#                    .grid(column = 1, row = 2, columnspan = 2, \
#                                  padx = 4, pady = 2, sticky = W)
#
#        
#        
#        ################################################################################
#        boutonOk = Button(self, width = 10,  relief = RAISED,
#                          height = 1,
#                          text = "Ok", command = self.valider)
#        boutonOk.grid(row = 3, column = 0, padx = 5, pady = 5)
#
#
#        Button(self, width = 10,  relief = RAISED, \
#               height = 1, \
#               text = "Annuler", command = self.destroy) \
#               .grid(row = 3, column = 1, padx = 5, pady = 5)
#
#        gui.alignerZones(zoneOptionsAide,zoneOptionsAnalyse,zoneOptionsGenerales)
#            
#        self.deiconify()
#
#
#    ####################################################################################
#    def valider(self):
#        self.options.copie(self.optionsProv)
#        self.master.gestionActivationBoutons()
#        self.destroy()
#
#        
