#!/usr/bin/env/python
#Program that will merge two different gzipped files line by line, based on a unique ID
#Author Runar Reve
#Email: runar.reve@kaust.edu.sa
#argv[1] zipped file 1
#argv[2] zipped file 2 
#argv[3] outfile 
import sys
import gzip

def main():
   file1name = sys.argv[1]
   file2name = sys.argv[2]
   outname   = sys.argv[3]

   size = 15000000
   header = 1
   table = [[] for _ in range(size)]
   print("Hashtable done!")
   #Take file 1 and put it in a hash table...
   for line in  gzip.open(file1name, 'rt'): 
      sline = line.replace('\n','').split('\t')
      if (header == 1):
         header = 0 
         continue 
      if (sline[2] == ""):
         continue 
      insert(table, sline, size)
   
   print("First file done hashing!")
   #...then add the next file too file 1 based on a unique ID
   header = 1 
   for line in  gzip.open(file2name, 'rt'):
      sline = line.replace('\n','').split('\t')
      #print(sline)
      if (header == 1):       
         header = 0  
         continue     
      if (sline[2] == ""):    
         continue   
      addTo(table, sline, size)
      
   printout(table, outname)
#-------------------------------------------------------------

def printout(table, outname):
   out = open(outname, 'w')
   for each in table:
      for peach in each:
         out.write(str('\t'.join(peach))+ '\n')


def addTo(table, string, size):
   compstring = string[2].replace(';','')
   key = hash_fun(hash(compstring), size)
   #Check if its there
   hashlist = table[key]
   for x in range(len(hashlist)):
      #print(hashlist[x][0] + " == " + compstring)
      if (hashlist[x][0] == compstring):
         print("Found one, Runar!")
         hashlist[x].append(string[3]) #add the last tab seperated 
   return
      

def insert(table, string, size):
   key = hash_fun(hash(string[0]), size)
   table[key].append(string)
   
def extract(table, ID, size):
   IDint = hash(ID)
   key = hash_fun(ID, size)
   hashlist = table[key]
   for each in hashlist:
      if (each[0] == ID):
         return each
   return 0

def hash_fun(x, size):
   return x%size

if __name__ == '__main__':
   main()

