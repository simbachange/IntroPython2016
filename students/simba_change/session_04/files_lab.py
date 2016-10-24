import glob
for x in glob.glob('C:\\Users\\simba\\IntroPython2016\\Examples\\Session05/*'):
    print (x)

 import csv

with open(r'C:\\Users\\simba\\IntroPython2016\\Examples\\Session01\\students.txt', 'r') as f:
   reader = csv.reader(f,delimiter=':')
   for row in reader:
       print (row[-1])