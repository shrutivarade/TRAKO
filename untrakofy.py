#!/usr/bin/env python3
import trako as TKO
import argparse, os, re, sys
import vtk

def untrakofy(input, output):
  '''
  '''

  if os.path.splitext(output)[1].lower() == '.vtp':

    polydata = TKO.Decoder.toVtp(input)

    w = vtk.vtkXMLPolyDataWriter()
    w.SetFileName(output)
    w.SetInputData(polydata)
    w.Update()

    restoredsize = os.path.getsize(output)

    return restoredsize

  else:
    print('ERROR: Only writing .vtp files is currently supported.')
    sys.exit(2)



if __name__ == "__main__":

  parser = argparse.ArgumentParser(description='T R A K O: Un-Compress streamlines.')
  parser.add_argument('-i','--input', help='Input compressed file (.tko)', required=True)
  parser.add_argument('-o','--output', help='Output streamline file (.vtp)', required=True)

  args = parser.parse_args()

  print()
  print('>> T R A K O.')
  print()

  restoredsize = untrakofy(args.input, args.output)

  print()
  print('Restored', restoredsize, 'bytes.')
  print()
  print(' (x_x) tko-ed.')
  print()
