#!/usr/bin/env/python
#author Runar Reve
#argv[1] innfile
#argv[2] outfile 
import sys 




def main():
   filename = sys.argv[1]
   outname  = sys.argv[2]
   out= open(outname, 'w') 
   for line in open(filename, 'r'):
      sline = line.split()
      temp = sline[3]
      #Now find GO
      for each in range(len(sline)-1, 0, -1):
         if (sline[each][0] != 'G'):
            break
         temp2 = sline[each].replace(';','').replace(':','_')
         #print ('<http://' + temp + '>\t<http://has_function>\t<http://' + temp2 + '>')
         out.write('<http://' + temp + '>\t<http://has_function>\t<http://' + temp2 + '> .\n')





if __name__ == '__main__':
   main()
