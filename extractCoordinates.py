# encoding: utf-8

from gvsig import *
from gvsig.commonsdialog import *
 
def main(*args):
    """Read wkt"""
    sel = currentLayer().getSelection()
    pfile = str(saveFileDialog("Seleccionar fichero texto de salida")[0])
    f = open(pfile,'w')
    for s in sel:
        f.write("\n\n================\n\n")
        f.write("\n"+str(s.getValues())+"\n\n")
        g = str(s.geometry().convertToWKT())
        f.write(g)
    f.close()
    print pfile
