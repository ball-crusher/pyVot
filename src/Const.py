#!/usr/bin/env python
# -*- coding: utf-8 -*-

##This file is part of PyVot
#############################################################################
#############################################################################
##                                                                         ##
##                                   Const                                 ##
##                                                                         ##
#############################################################################
#############################################################################

## Copyright (C) 2006 CÃ©drick FAURY

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

import wx
import os

##import gui
#from Tkinter import *
import sys
#from Elements import listeElements, coefTaille
#from Widget import InfoBulle


##############################################################################
#     Polices     #
##############################################################################

Font_Titre       = [("Helvetica, ", "13", "bold",   "italic")             ,"blue"]
Font_Logo        = [("Helvetica, ", "30", "bold",   "italic")             ,"red"]

Font_AnalTitre   = [("Helvetica, ", "11", "bold",   "italic")             ,"dark red"]

Font_CdCFTitre   = [("Helvetica, ", "9",  "bold",   "roman")              ,"dark blue"]
Font_CdCFTitreS  = [("Helvetica, ", "10",  "bold",   "roman", "underline")   ,"dark blue"]
Font_CdCFValeur  = [("Helvetica, ", "10", "normal", "roman")              ,"dark red"]
Font_CdCFPetit   = [("Helvetica, ", "8",  "normal", "roman")              ,"dark grey"]
Font_CdCFMoy     = [("Helvetica, ", "9",  "normal", "italic")             ,"black"]

Font_Message     = [("Helvetica, ", "20", "bold",   "roman")              ,"black"]
Font_LienWeb     = [("Helvetica, ", "9",  "normal", "roman", "underline") ,"blue"]
Font_test        = [("Helvetica, ", "8",  "normal", "roman")              ,"black"]

Font_TitreBulle  = [("Helvetica, ", "9",  "bold", "roman", "underline") , "dark blue"]
Font_MessBulle   = [("Helvetica, ", "8",  "normal", "roman")              ,"black"]
Font_MessBulleI  = [("Helvetica, ", "8",  "normal", "italic")              ,"black"]
Font_MessBulleG  = [("Helvetica, ", "8",  "bold", "roman")              ,"black"]
Font_MessBulleS  = [("Helvetica, ", "8",  "normal", "roman", "underline")   ,"black"]

Font_Info        = [("Helvetica, ", "10",  "normal", "roman")              ,"dark red"]
Font_InfoNoir    = [("Helvetica, ", "9",  "normal", "roman")             ,"black"]
Font_Message     = [("Helvetica, ", "11",  "normal", "italic")             ,"dark blue"]
Font_PetitGrand  = [("Helvetica, ", "12",  "normal", "roman")              ,"dark red"]

Font_AnalDetail  = [("Helvetica, ", "9", "normal", "roman")              ,"dark red"]

Font_GrosBouton  = [("Helvetica, ", "11",  "normal", "roman")             ,"black"]

Font_Onglet = [("Helvetica, ", "8",  "normal", "roman")              ,"black"]
Font_OngletActif = [("Helvetica, ", "8",  "bold", "roman")              ,"black"]


##############################################################################
#     Message d'erreur d'analyse     #
##############################################################################
arg2str = {0    : ("sens",u"right"),
           1    : ("sens",u"left"),
           "D"  : ("cote",u"right"),
           "G"  : ("cote",u"left"),
           "GD" : ("cote",u""),
           "DG" : ("cote",u""),
           "Al" : ("radi",u"bore"),
           "Ar" : ("radi",u"shaft"),
           "EAl" : ("etanch",u"static"),
           "EAr" : ("etanch",u"dynamic")
           }


messagesAnalyse = { ''               : ('','black'),
                    'MontOk'         : (u"Assembly is correct","green"),

                    # Remarques gÃ©nÃ©rales
                    'ManqueRlt'      : (u"A bearing is missing to form a pivot joint!", "red"),
                    'RltPasMaintenu' : (u"One of the %(cote)s bearing rings is not retained.", "red"),
                    'RltPasMaintenus': (u"One of the bearing rings is not retained.", "red"),
                    'RltsImcomp'     : (u"Incompatible bearings.", "red"),
                    'OrientIncorr'   : (u"The orientation of the angular contact bearings is incorrect.", "red"),
                    'RltPasArrete'   : (u"The %(cote)s bearing should be retained on both sides on the %(radi)s.", "blue"),
                    'RltPasArretes'  : (u"Both bearings should be retained on both sides on the %(radi)s.", "blue"),

                    # Immobilisation axiale du montage
                    'ArretArbreSens' : (u"The shaft is not axially retained toward the %(sens)s" , "red"),
                    'Hyperstatique'  : (u"hyperstatic." , "blue"),
                    'ImmobCorrect'   : (u"The shaft is axially retained." , "green"),
                    'ArbreArrete'    : (u"The shaft is correctly axially retained." , "green"),
                    'ArbrePasArrete' : (u"The shaft is not correctly axially retained." , "red"),

                    # RÃ©sistance aux charges
                        # axial
                    'ChargeAxOk'     : (u"The assembly withstands the axial load." , "green"),
                    'ChargeAxNo'     : (u"The assembly does not withstand the axial load." , "red"),
                    'ElemResistPas'  : (u"The following elements do not withstand the load:", "red"),
                        # roult
                    'RltSupportePas' : (u"does not withstand" , "red"),
                    'RltSupporte'    : (u"withstands" , "green"),
                    'TRltSupportePas' : (u"No bearing withstands the load." , "red"),
                    '1RltSupportePas' : (u"The %(cote)s bearing does not withstand the load." , "red"),
                    'TRltSupporte'    : (u"All bearings withstand the load." , "green"),

                        # 
                    'ChargeRadOk'    : (u"Withstands the radial load.", "green"),
                    'EffortRadial'   : (u"Does not withstand the radial load.", "red"),

                    # MontabilitÃ©
                    'MontImposs'     : (u"Some components cannot be assembled or disassembled!" , "red"),
                    'Possible'       : (u"possible" , "green"),
                    'Impossible'     : (u"impossible" , "red"),
                    'Collision'      : (u"Collision between the following elements:", "red"),
                    'ElemNonDem'     : (u"Element %s cannot be assembled/disassembled.", "red"),
                    'RltGonfl'       : (u"The %(cote)s bearing cannot be mounted on the %(radi)s!", "red"),
                    'MontPoss'       : (u"The components can be assembled/disassembled." , "green"),
                    'MontImpossRlt'  : (u"The %(cote)s bearing cannot be mounted on the %(radi)s!", "red"),
                    'CollisionRlt'   : (u"Collision with the following elements:" , "red"),
                    'BagueIsolee'    : (u"The following bearing cannot be assembled on its tight housing.", "red"),
                    'BagueIsolees'   : (u"The following bearings cannot be assembled on their tight housing.", "red"),

                    # Sealing
                    'EtanchStat'      : (u"Static sealing is ensured." , "green"),
                    'PasEtanchStat'   : (u"Static sealing is not ensured!" , "red"),
                    'EtanchDyn'       : (u"Dynamic sealing is ensured." , "green"),
                    'PasEtanchDyn'    : (u"Dynamic sealing is not ensured!" , "red"),
                    'IncompLubHuil'   : (u"Oil lubrication is impossible with the labyrinth seals!" , "red"),
                    'IncompLubChic'   : (u"The labyrinth seals are incompatible with the desired pressure!" , "red"),
                    'ManqueJoint'     : (u"A sealing device is missing on the %(cote)s side.", "red"),
                    'VitesseTrop'     : (u"The speed is too high for the %(cote)s seal.", "red"),
                    'FactPVTrop'      : (u"The PV factor is too high for the %(cote)s seal.", "red"),
                    'VittPVTrop'      : (u"The speed and PV factor are too high for some seals.", "red"),
                    'PressTrop'       : (u"The pressure is too high for the %(cote)s seal.", "red"),

                    'LubrifComp'      : (u"The seals are compatible with the selected lubrication.", "green"),
                    'LubrifPasComp'   : (u"The labyrinth seals are not compatible with oil lubrication.", "red")
                    }

#########################################################################################
class StyleDeTexte:
    def __init__(self, font, color):
        self.font = font
        self.color = color
        
    def applique(self, win, color = None):
        if color != None:
            self.color = color
        win.SetFont(self.font)
        win.SetForegroundColour(self.color)
        
############################################################################################
class MessageAnalyse:
    def __init__(self, clef = '', lstArg = [], mess = None, coul = None):

##        print
##        print "Initialisation messsage : clef =",clef," ; args =",args

        strArg = {}
        for comp in lstArg:
            strArg[arg2str[comp][0]] = arg2str[comp][1]
    
        self.clef = clef

        if "GD" in lstArg or "DG" in lstArg:
            clef += "s"
            
        if clef <> '':
            self.mess = messagesAnalyse[clef][0] %strArg
            self.coul = messagesAnalyse[clef][1]
        else:
            self.mess = mess
            self.coul = coul

    

################################################################################
#      Liens vers l'aide       #
################################################################################
dossierTravail = os.getcwd()
dossierAide = "/Aide/"
lienAide = {"index"   : "index.html",
            "cdcf"    : "cdcf.html",
            "analyse" : "analyse.html"}

def afficherAide(options, clef):
##    webbrowser.open(lienAide[clef])
##    print "Affichage de l'aide :",lienAide[clef]
    if options.typeAide.get() == 0 and sys.platform == 'win32':
        os.startfile(dossierAide+'pyvotaide.chm')
    else:
        os.chdir(dossierTravail+dossierAide+"html/")
        webbrowser.open('index.html')
        os.chdir(dossierTravail)



##############################################################################
#     Zone de message     #
##############################################################################

#messages = {'SelectElem' : u"Selectionner un Ã©lÃ©ment Ã  placer sur le montage",
#            'FaireGliss' : u"Faire glisser l'Ã©lÃ©ment sur le montage",
#            'MenuContex' : u"Bouton droit de la souris pour modifier l'Ã©lÃ©ment",
#            'PlacerElem' : u"Cliquer pour placer l'Ã©lÃ©ment sur le montage",
#            'ModifCdCF'  : u"Modification du CdCF"}
#
#class ZoneMessage(Frame):
#    "classe dÃ©finissant la zone de message"
#    def __init__(self, master):
#        Frame.__init__(self, bd = 2, relief = FLAT,
#                       width = 400, height = 30, padx = 3, pady = 3)
#        self.grid_propagate(0)
#        self.master = master
#        self.message = StringVar()
#        self.messageSauv = messages['SelectElem']
#        Label(self, textvariable = self.message, \
#              font = Font_Message[0], \
#              fg = Font_Message[1], \
#              anchor = E, justify = LEFT,
#              ) \
#              .grid(column = 0, row = 0, sticky = W)
#
#    def afficher(self, clef, sauv = False):
#        if sauv:
#            self.messageSauv = self.message.get()
#        self.message.set(messages[clef])
#        
#    def restaurer(self):
#        self.message.set(self.messageSauv)
        


##############################################################################
#     Info bulle     #
##############################################################################
bulles = {'vide'    : u"",
          'Ouvrir'  : u"Open an assembly from a file",
          'Enregi'  : u"Save the assembly to a file",
          'ModCdcf' : u"Edit the functional specification",
          'Analyse' : u"Analyze the assembly",
          'Reinit'  : u"Reset the assembly\nAll elements will be removed!",
          'CdCFCurs'    : u"Drag the slider\nto change the index value",
          'CdCFAide'    : u"Show the CdCF help",
          'CdCFCharg'   : u"Distribution and indices of the loads\napplied to the shaft",
          'CdCFBague'   : u"Specifies which ring rotates\nrelative to the radial load\napplied to the shaft",
          'CdCF'        : u"Functional specification",
          'CdCFCout'    : u"Maximum cost index of the assembly",
          'CdCFPress'   : u"Relative pressure index in the joint",
          'CdCFVitt'    : u"Angular speed index of the joint",
          'AnalyAnim'   : u"Play an animation illustrating missing stops",
          'AnalyChai'   : u"Draw the action chain of the axial load",
          'SelectRoul'  : u"Highlight elements that do not resist the axial load",
          'AnalyHypr'   : u"The action chain is doubled...",
          'EnsPasDemont': u"Disassemble the assembly to be able to\n",
          'Dem'         : u"Disassemble",
          'Rem'         : u"Reassemble",
          'Ens'         : u"the assembly",
          'Rlt'         : u"the bearing",
          'G'           : u"left",
          'D'           : u"right",
          'Al'          : u"shaft",
          'Ar'          : u"bore",
          'vers'        : u"toward the",
          'depuis'      : u"from the",
          'sens0'       : u"right.",
          'sens1'       : u"left.",
          'AnalyMtgEns': u"Play an animation of the disassembly/assembly\nof the assembly toward/from the right",
          'AnalyMtgEns1': u"Play an animation of the disassembly/assembly\nof the assembly toward/from the left",
          'AnalyMtgRlt' : u"Play an animation of the disassembly/assembly\nof bearing %s toward/from the %s",
          'AnalyMtgObs' : u"Highlight the different obstacles to disassembly"
          }


#################################################################################
class InfoBulleSimple:
    def __init__(self, zone, clefBulle):
        bulle = InfoBulle(zone)  
        Label(bulle, text = bulles[clefBulle], bg = bulle['bg']).grid()



#################################################################################
class InfoBulleMulti:
    def __init__(self, zone, lstClefBulle):
        bulle = InfoBulle(zone)
        self.label = Label(bulle, text = '', bg = bulle['bg'])
        self.label.grid()
        self.changer(lstClefBulle)

    def changer(self,lstClefBulle):
        txt = ''
        for c in lstClefBulle:
            txt += bulles[c]+" "
        self.label['text'] = txt
        
        

#################################################################################
class InfoBulleDetails:
    def __init__(self, zone, lstNoms,
                 commandEntrer, commandQuitter):
        self.bulle = InfoBulle(zone)
        self.commandEntrer = commandEntrer
        self.commandQuitter = commandQuitter
        
        Label(self.bulle, text = lstNoms['mess'],
              bg = self.bulle['bg'],
              justify = LEFT) \
            .pack(anchor = W)

        self.l = []
        for n in lstNoms['lst']:
            self.l.append(Label(self.bulle, text = n,
                              bg = self.bulle['bg'],
                              justify = LEFT))
        
        for n in range(len(self.l)):
            self.l[n].pack(anchor = W)
            self.l[n].bind("<Enter>",lambda evt = None, arg = n : self.entrer(evt,arg))
            self.l[n].bind("<Leave>",lambda evt = None, arg = n : self.quitter(evt,arg))

        self.bulle.zone.bind("<Leave>",self.quitterZone)
        self.bulle.bind("<Leave>",self.quitterBulle)
        self.bulle.bind("<Enter>",self.entrerBulle)

    def quitterBulle(self, event):
        if event.widget == self.bulle:
            self.bulle.efface()

    def quitterZone(self, event):
        self.action = self.bulle.after(100,self.bulle.efface)
        self.bulle.zone.quitter()

    def entrerBulle(self,event):
        self.bulle.after_cancel(self.action)
        
    def entrer(self, event = None, num = None):
        self.l[num]['bg'] = "dark blue"
        self.l[num]['fg'] = "white"
        self.commandEntrer(num)

    def quitter(self, event = None, num = None):
        self.l[num]['bg'] = self.bulle['bg']
        self.l[num]['fg'] = "black"
        self.commandQuitter(num,False)



#################################################################################        
class InfoBulleElem:
    """Tooltip helper describing an element in the catalogue."""
    
    def __init__(self, zone, numElem, taille = ["P","G"]):
        bulle = InfoBulle(zone)
        
        if type(taille) <> list: taille = [taille]
            
        Label(bulle, text = listeElements[numElem]['nom'],
              bg = bulle['bg'],
              font = Font_TitreBulle[0],
              fg = Font_TitreBulle[1],
              justify = RIGHT) \
            .grid(row = 0, column = 0,
                  columnspan = 4, sticky = W)

        c = 1
        for t in taille:
            if t == "P":
                tx = u"small"
            else:
                tx = u"large"
            Label(bulle, text = tx,
                  bg = bulle['bg'],
                  justify = RIGHT, anchor = E) \
                .grid(row = 1, column = c, sticky = E)
            c += 1
            
        if listeElements[numElem]['type'] == "R":
            Label(bulle, text = u"Allowable load indices:",
                  bg = bulle['bg'],
                  justify = RIGHT, anchor = E,
                  font = Font_MessBulleG[0]) \
                .grid(row = 1, column = 0, sticky = E)
            Label(bulle, text = u"axial:",
                  bg = bulle['bg'],
                  justify = RIGHT, anchor = E) \
                .grid(row = 2, column = 0, sticky = E)
            Label(bulle, text = u"radial:",
                  bg = bulle['bg'],
                  justify = RIGHT, anchor = E) \
                .grid(row = 3, column = 0, sticky = E)
            Label(bulle, text = u"combined:",
                  bg = bulle['bg'],
                  justify = RIGHT, anchor = E) \
                .grid(row = 4, column = 0, sticky = E)

            r = 2
            c = 1
            for i in ["axial","radial","combi"]:
                for t in taille:
                    Label(bulle, text = str(coefTaille(listeElements[numElem]['chargeAdm'][i],
                                                      numElem,t)),
                          justify = RIGHT, bg = bulle['bg']) \
                        .grid(row = r, column = c)
                    c += 1
                Label(bulle, text = adaptation[listeElements[numElem]['chargeAdm'][i]],
                      justify = RIGHT, bg = bulle['bg'],
                      font = Font_MessBulleI[0]) \
                    .grid(row = r, column = c)
                c = 1
                r += 1

            Label(bulle, text = u"Cost index:",
                  bg = bulle['bg'],
                  justify = RIGHT, anchor = E,
                  font = Font_MessBulleG[0]) \
                .grid(row = r, column = 0, sticky = E)
            c = 1
            for t in taille:
                Label(bulle, text = str(coefTaille(listeElements[numElem]['cout'],
                                                      numElem,t)),
                          justify = RIGHT, bg = bulle['bg']) \
                        .grid(row = r, column = c)
                c += 1
         
        elif listeElements[numElem]['type'] == "A":
            Label(bulle, text = u"Allowable load index:",
                  bg = bulle['bg'],
                  justify = RIGHT, anchor = E,
                  font = Font_MessBulleG[0]) \
                .grid(row = 2, column = 0, sticky = E)
            c = 1
            for t in taille:
                Label(bulle, text = str(coefTaille(listeElements[numElem]['chargeAdm']["axial"],
                                                  numElem,t)),
                          justify = RIGHT, bg = bulle['bg']) \
                        .grid(row = 2, column = c)
                c += 1
            
            Label(bulle, text = u"Cost index:",
                  bg = bulle['bg'],
                  justify = RIGHT, anchor = E,
                  font = Font_MessBulleG[0]) \
                .grid(row = 3, column = 0, sticky = E)
            c = 1
            for t in taille:
                Label(bulle, text = str(coefTaille(listeElements[numElem]['cout'],
                                                       numElem,t)),
                          justify = RIGHT, bg = bulle['bg']) \
                        .grid(row = 3, column = c)
                c += 1

        elif listeElements[numElem]['type'] == "J":
            Label(bulle, text = u"Allowable pressure:",
                  bg = bulle['bg'],
                  justify = RIGHT, anchor = E,
                  font = Font_MessBulleG[0]) \
                .grid(row = 2, column = 0, sticky = E)

            c = 0
            for e in listeElements[numElem]['pos']:
                Label(bulle, text = str(coefTaille(listeElements[numElem]['pressAdm'][e],
                                                   numElem,t)),
                      justify = RIGHT, bg = bulle['bg']) \
                      .grid(row = 2, column = c)
                c += 1
                
            
            Label(bulle, text = u"Allowable speed:",
                  bg = bulle['bg'],
                  justify = RIGHT, anchor = E,
                  font = Font_MessBulleG[0]) \
                .grid(row = 3, column = 0, sticky = E)

            Label(bulle, text = str(coefTaille(listeElements[numElem]['vittAdm'],
                                               numElem,t)),
                  justify = RIGHT, bg = bulle['bg']) \
                  .grid(row = 3, column = c)
                

        
##class infoBulle(Toplevel):
##    def __init__(self, parent, lstMess = [], lstClef = [], numElem = None,
##                 frameSpec = None, temps = 400, side = LEFT, position = "bord"):
##
####        if lstMess <> []:
####            t = "lstMess ="
####            a = lstMess
####        elif lstClef <> []:
####            t = "lstClef ="
####            a = lstClef
####        elif elemMess <> None:
####            t = "elemMess ="
####            a = elemMess
####        elif frameSpec <> None:
####            t = "frameSpec ="
####            a = frameSpec
####        
####        print
####        print "Initialisation Bulle :"
####        print t,a
##        
##        Toplevel.__init__(self,parent,bd=2,bg='lightyellow',relief = RIDGE)
##        self.tps = temps
##        self.parent=parent
##        self.withdraw()
##        self.overrideredirect(1)
##        self.transient()
##        self.position = position
##        self.side = side
##        self.lstLabel = []
##
##        self.lstMess = lstMess
##        self.lstClef = lstClef
##
##        self.tipwidth = 0
##        self.tipheight = 0
##            
##        if numElem <> None:
##            self.ajouterFrame(numElem)
##        elif frameSpec <> None:
##            self.ajouterFrameSpec(frameSpec)  
##        else:
##            self.ajouterLabel()
##
##        self.parent.bind('<Enter>',self.delai)
##        self.parent.bind('<Button-1>',self.efface)
##        self.parent.bind('<Leave>',self.efface)
##
##    ############################################################################
##    def listeMessages(self):
##        lstMess = []
##        for c in self.lstClef:
##            lstMess.append({'str' : bulles[c],
##                            'fon' : Font_MessBulle})
##        for c in self.lstMess:
##            lstMess.append(c)
##            
##        return lstMess
##
##    ####################################################################################################
##    def majLabel(self,lstClef = None):
##        
##        if lstClef is not None:
##            self.lstClef = lstClef
##            
##        lstMess = self.listeMessages()
##        
####        print "  majLabel",self.lstClef,lstMess
####        print " tailles : labels =",len(self.lstLabel)
####        print "           mess =",len(lstMess)
##
##        for i in range(len(self.lstLabel)):
##            txt = lstMess[i]['str']
##            if txt[-1:] == "\n":
##                txt = txt[:-1]
##                packside = TOP
##            else:
##                packside = self.side
##            
##            self.lstLabel[i]['text'] = txt
##            self.lstLabel[i]['font'] = lstMess[i]['fon'][0]
##            self.lstLabel[i]['fg'] = lstMess[i]['fon'][1]
##            
##            self.lstLabel[i].pack(side = packside)
####            print i
##
##        self.attribuerDimensions()
##        
####        print "dimensions =",self.tipwidth,self.tipheight
##
##
##    ####################################################################################################
##    def ajouterLabel(self):
####        print "  ajouter label"
##        self.lstLabel = []
##        for m in range(len(self.lstClef) + len(self.lstMess)):
##            t = Label(self, bg = "lightyellow")
##            self.lstLabel.append(t)
####        print "   ...",len(self.lstLabel)," labels ajoutÃ©s"
##        self.majLabel()
##        
##
##
##
##    ####################################################################################################
##    def ajouterFrame(self, numElem):
####        print "  ajouter frame",elemMess
##        
##        t = FrameBulleElem(self, numElem)
##        t.pack()
##
##        self.attribuerDimensions()
##        
##
##    ####################################################################################################
##    def ajouterFrameSpec(self, frameSpec):
##        t = frameSpec
##        t.__init__(self, t.lstObstacles, t.sens)
##
##        self.attribuerDimensions()
##
##
##    ##################################################################################################
##    def attribuerDimensions(self):
##        self.update_idletasks()
##        self.tipwidth = self.winfo_width()
##        self.tipheight =  self.winfo_height()
##
##        
##    ####################################################################################################
##    def delai(self,event):
##        self.x,self.y = event.x,event.y
##        self.action = self.parent.after(self.tps,self.affiche)
##
##
##    ####################################################################################################
##    def affiche(self):
##        self.update_idletasks()
####        print
####        print "Affichage bulle :"
####        print "  dimensions bulle =",self.tipwidth,self.tipheight
##
##        if self.position == "bord":
##            posX = self.parent.winfo_rootx()+self.parent.winfo_width()/2
##            posY = self.parent.winfo_rooty()+self.parent.winfo_height()
##        else:
##            posX = self.parent.winfo_rootx() 
##            posY = self.parent.winfo_rooty()
##
####        print "  position avant =",posX,posY
##
##        # Correction pour que Ã§a rentre dans l'Ã©cran
##        if posX + self.tipwidth > self.winfo_screenwidth():          
##            posX = posX - self.tipwidth
##        if posY + self.tipheight > self.winfo_screenheight():
##            if self.position == "bord":
##                posY = self.parent.winfo_rooty() - self.tipheight
##            else:
##                posY = posY - self.tipheight
##
####        print "  position aprÃ¨s =",posX,posY
##        #~ print posX,print posY
##        self.geometry('+%d+%d'%(posX,posY))
##        self.deiconify()
##
##    #########################################################################################
##    def efface(self,event):
##        self.withdraw()
##        self.parent.after_cancel(self.action)
##
##

############################################################################################
##class FrameBulleElem(Frame):
##    """ Classe dÃ©finissant l'info-bulle pour un Ã©lÃ©ment """
##    
##    def __init__(self, master, options):
##
##        Frame.__init__(self, bg = "lightyellow")
##
##        numElem = options['numElem']
##        
##        if 'taille' in options:
##            lstTaille = [options['taille']]
##        else:
##            lstTaille = ["P","G"]
##            
##
##        Label(self, text = listeElements[numElem]['nom'],
##              bg = "lightyellow",
##              font = Font_TitreBulle[0],
##              fg = Font_TitreBulle[1],
##              justify = RIGHT) \
##            .grid(row = 0, column = 0,
##                  columnspan = 4, sticky = W)
##
##        c = 1
##        for t in lstTaille:
##            if t == "P":
##                tx = u"petit"
##            else:
##                tx = u"grand"
##            Label(self, text = tx,
##                  bg = "lightyellow",
##                  justify = RIGHT, anchor = E) \
##                .grid(row = 1, column = c, sticky = E)
##            c += 1
##            
##        if listeElements[numElem]['type'] == "R":
##            Label(self, text = u"Indices de charge admissible :",
##                  bg = "lightyellow",
##                  justify = RIGHT, anchor = E,
##                  font = Font_MessBulleG[0]) \
##                .grid(row = 1, column = 0, sticky = E)
##            Label(self, text = u"axiale :",
##                  bg = "lightyellow",
##                  justify = RIGHT, anchor = E) \
##                .grid(row = 2, column = 0, sticky = E)
##            Label(self, text = u"radiale :",
##                  bg = "lightyellow",
##                  justify = RIGHT, anchor = E) \
##                .grid(row = 3, column = 0, sticky = E)
##            Label(self, text = u"combinÃ©e :",
##                  bg = "lightyellow",
##                  justify = RIGHT, anchor = E) \
##                .grid(row = 4, column = 0, sticky = E)
##
##            r = 2
##            c = 1
##            for i in ["axial","radial","combi"]:
##                for t in lstTaille:
##                    Label(self, text = str(coefTaille(listeElements[numElem]['chargeAdm'][i],
##                                                      numElem,t)),
##                          justify = RIGHT, bg = "lightyellow") \
##                        .grid(row = r, column = c)
##                    c += 1
##                Label(self, text = adaptation[listeElements[numElem]['chargeAdm'][i]],
##                      justify = RIGHT, bg = "lightyellow",
##                      font = Font_MessBulleI[0]) \
##                    .grid(row = r, column = c)
##                c = 1
##                r += 1
##
##            Label(self, text = u"Indice de CoÃ»t :",
##                  bg = "lightyellow",
##                  justify = RIGHT, anchor = E,
##                  font = Font_MessBulleG[0]) \
##                .grid(row = r, column = 0, sticky = E)
##            c = 1
##            for t in lstTaille:
##                Label(self, text = str(coefTaille(listeElements[numElem]['cout'],
##                                                      numElem,t)),
##                          justify = RIGHT, bg = "lightyellow") \
##                        .grid(row = r, column = c)
##                c += 1
##         
##        else:
##            Label(self, text = u"Indice de charge admissible :",
##                  bg = "lightyellow",
##                  justify = RIGHT, anchor = E,
##                  font = Font_MessBulleG[0]) \
##                .grid(row = 2, column = 0, sticky = E)
##            c = 1
##            for t in lstTaille:
##                Label(self, text = str(coefTaille(listeElements[numElem]['chargeAdm']["axial"],
##                                                  numElem,t)),
##                          justify = RIGHT, bg = "lightyellow") \
##                        .grid(row = 2, column = c)
##                c += 1
##            
##            Label(self, text = u"Indice de CoÃ»t :",
##                  bg = "lightyellow",
##                  justify = RIGHT, anchor = E,
##                  font = Font_MessBulleG[0]) \
##                .grid(row = 3, column = 0, sticky = E)
##            c = 1
##            for t in lstTaille:
##                Label(self, text = str(coefTaille(listeElements[numElem]['cout'],
##                                                       numElem,t)),
##                          justify = RIGHT, bg = "lightyellow") \
##                        .grid(row = 3, column = c)
##                c += 1
        
        
        
        

################################################################################
#     Types de charge     #
################################################################################

typeCharge = {0 : u"no\nload",
              1 : u"purely\naxial load",
              2 : u"purely\naxial load",
              3 : u"purely\naxial load",
              4 : u"purely\nradial load",
              5 : u"combined\nload",
              6 : u"combined\nload",
              7 : u"combined\nload"}


adaptation = {0 : u"unsuitable",
              1 : u"poor",
              2 : u"adequate",
              3 : u"good",
              4 : u"excellent"}







################################################################################
# Traductions en textes #
################################################################################

cote2text = {"G" : "left",
             "D" : "right"}


###################################################################################################
palierOppose = {"G" : "D",
                "D" : "G"}

##def cote2txt(cote):
##    if cote == "G":
##        return = u"gauche"
##    elif cote == "D":
##        return = u"droit"
##    else:
##        return


        
