#Author-Abhijit Nimbalkar
#Andrew ID- asnimbal


#a. Output for Fahrenheit temperatures 0, 32, 45, 60, 70, 95, and 212.
fahr_list = [0,32,45,60,70,95,212]      #Creating List
print("""Program 1.a : For converting temperatures from Fahrenheit to Celcius=""")
for temp_point in fahr_list:            #Using for Loop 
    print(temp_point)
    print(temp_point,'Fahrenheit is',5/9*(temp_point-32),"Celsius")   #Printing the Output


#b.Display output for Celsius temperatures 0, 10, 15, 20, 25, 30, and 100
cels_list = [0,10,15,20,25,30,100]      #Creating List
print("""\n\nProgram 1.b : For converting temperatures from Celcius to Fahrenheit to=""")
for temp_point in cels_list:            #Using for Loop 
    print(temp_point)
    print(temp_point,'Celsius is',(9*temp_point/5)+32,"Fahrenheit")   #Printing the Output


#c.Commenting the given table
"""
Date    Hi(F)  Lo(F)  %Hum
AUG 30     79     64    60
AUG 31     82     66    20
SEP  1     85     68    20
SEP  2     85     68    30
SEP  3     87     69    30
SEP  4     87     69    20
SEP  5     87     69    20
SEP  6     85     67    20
SEP  7     81     63    30
SEP  8     79     61    20
SEP  9     77     61    20
SEP 10     77     59    20
SEP 11     77     59    20
SEP 12     77     59    20
SEP 13     77     59    50
"""

#d & e.Displaying the commented table
dt=['AUG 30','AUG 31','SEP  1','SEP  2','SEP  3','SEP  4','SEP  5','SEP  6','SEP  7','SEP  8','SEP  9','SEP 10','SEP 11','SEP 12','SEP 13']   #Creating List for Date
hi=[79,82,85,85,87,87,87,85,81,79,77,77,77,77,77]     #Creating List for High Temperature
lo=[64,66,68,68,69,69,69,67,63,61,61,59,59,59,59]     #Creating List for Low Temperature
hm=[60,20,20,30,30,20,20,20,30,20,20,20,20,20,50]     #Creating List for Humudity
print('\nProgram 1.d & e: Displaying the commented table=')
print('Date    Hi(F)  Lo(F)  %Hum')
num_days = len(dt)                                    #Using Len function for length table rows with the help of dt list
for i in range(num_days):                             #Applying For loop for displaying table      
    print(dt[i],"   ", hi[i],"   ", lo[i],"  ", hm[i])


#f.Calculating Mean, Median and Standard Deviation for above table
#Calculating the Mean of all columns from the above table
hi_mean=sum(hi)/len(hi)
lo_mean=sum(lo)/len(lo)
hm_mean=sum(hm)/len(hm)
#Sorting all the lists and copying to new list
hi_copy=hi.copy()
lo_copy=lo.copy()
hm_copy=hm.copy()
hi_copy.sort()
lo_copy.sort()
hm_copy.sort()
#Calculating the Median of all columns from above table
hi_med=hi_copy[len(hi_copy)//2]
lo_med=lo_copy[len(lo_copy)//2]
hm_med=hm_copy[len(hm_copy)//2]
#Calculating the standard deviation of for all columns from above table
#Calculating standard deviation for High Temperature
hi_temp=0
for val in hi:
    hi_temp+=(val-hi_mean)**2
hi_std=(hi_temp/(len(hi)-1))**0.5
#Calculating standard deviation for Low Temperature
lo_temp=0
for val in lo:
    lo_temp+=(val-lo_mean)**2
lo_std=(lo_temp/(len(lo)-1))**0.5
#Calculating standard deviation for Humidity
hm_temp=0
for val in hm:
    hm_temp+=(val-hm_mean)**2
hm_std=(hm_temp/(len(hm)-1))**0.5
# Printing all calculated values
print("\nProgram 1.f:Calculating Mean, Median and Standard Deviation of numbers from above table")
print("{:=<24s}{:>0.2f}{:2s}{:=<24s}{:>2d}{:2s}{:=<40s}{:0>5.2f}".format("Mean of High Temperature=",hi_mean," ","Median of High Temperature=",hi_med," ","Standard Deviation of High Temperature=",hi_std))
print("{:=<25s}{:>0.2f}{:2s}{:=<27s}{:>2d}{:2s}{:=<40s}{:0>5.2f}".format("Mean of Low Temperature=",lo_mean," ","Median of Low Temperature=",lo_med," ","Standard Deviation of Low Temperature=",lo_std))
print("{:=<25s}{:>0.2f}{:2s}{:=<27s}{:>2d}{:2s}{:=<40s}{:>4.2f}".format("Mean of Humidity=",hm_mean," ","Median of Humidity=",hm_med," ","Standard Deviation of Humidity=",hm_std))

#g.Displaying the given table with Format()
dt2=['AUG 30','AUG 31','SEP  1','SEP  2','SEP  3','SEP  4','SEP  5','SEP  6','SEP  7','SEP  8','SEP  9','SEP 10','SEP 11','SEP 12','SEP 13']
hi2=[107,109,104,101,99,98,95,98,98,102,104,101,99,96,99]
lo2=[78,80,79,78,77,78,78,78,77,80,81,80,78,77,78]
hm2=[15,8,12,13,9,8,8,10,10,10,12,8,15,15,12]
print("\nProgram 1.g: Displaying the given table with format()")
print('{0:<6s}{1:>7s}{2:>7s}{3:>6s}'.format("Date","Hi(F)","Lo(F)","%Hum"))
for i in range(len(dt2)):
    print("{0:<6s}{1:>7d}{2:>7d}{3:>6d}".format(dt2[i],hi2[i],lo2[i],hm2[i]))

#h.Displaying the given table with Format() (In Celsius)
print("\nProgram 1.h: Displaying the given table with format() (In Celsius)")
print('{0:<6s}{1:>7s}{2:>7s}{3:>6s}'.format("Date","Hi(C)","Lo(C)","%Hum"))
for i in range(len(dt2)):
    print("{:<6s}{:>7.2f}{:>7.2f}{:>6d}".format(dt2[i],5/9*(hi2[i]-32),5/9*(lo2[i]-32),hm2[i]))

#i.Format Strings examples from Python 3.6 Documentation
print("\nProgram 1.i: Format Strings examples from Python 3.6 Documentation")
print("\n-----Example 1-----")
print('{0}, {1}, {2}'.format('a', 'b', 'c'))
print('{}, {}, {}'.format('a', 'b', 'c'))  
print('{2}, {1}, {0}'.format('a', 'b', 'c'))
print('{2}, {1}, {0}'.format(*'abc'))      
print('{0}{1}{0}'.format('abra', 'cad'))

print("\n-----Example 2-----")
print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord))

print("\n-----Example 3-----")
print("Using the comma as a thousands separator:")
print("{:,}".format(1026899640))

print("\n-----Example 4-----")
print("Expressing a percentage:")
print("The total percent is {:0.2%}".format(25/75))

print("\n-----Example 5-----")
print("Using type-specific formatting:")
import datetime
d=datetime.datetime(2015,7,4,8,25,58)
print("{:%Y-%m-%d %H:%M:%S}".format(d))

print("\n-----Example 6-----")
print('{:+f}; {:+f}'.format(3.14, -3.14))
print('{: f}; {: f}'.format(3.14, -3.14))  
print('{:-f}; {:-f}'.format(3.14, -3.14))

print("\n-----Example 7-----")
for align, text in zip('<^>', ['left', 'center', 'right']):
    print('{0:{fill}{align}16}'.format(text, fill=align, align=align))

print("\n-----Example 8-----")
octets = [192, 168, 0, 1]
print('{:02X}{:02X}{:02X}{:02X}'.format(*octets))

print("\n-----Example 9-----")
width = 5
for num in range(5,12): 
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()

print("\n-----Example 10-----")
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))

print("\n-----Example 11-----")
c = 3-5j
print('The complex number {0} is formed from the real part {0.real} and the imaginary part {0.imag}.'.format(c))

print("\n-----Example 12-----")
print("repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2'))

print("\n-----Example 13-----")
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)
new_string=str(Point(4, 2))
print(new_string);

#j.Using for loop to display the required table of cube root, square root, integer value, square and cube
print("\nProgram 1.j: Using Nested for Loop\n")
print("{:>15s}{:>18s}{:>17s}{:>17s}{:>17s}".format("Cube Root","Square Root","Integer Value","Square","Cube"))  #Defining the heading of the table
for row in range(0,20):                                                                                         #for loop for calculating values from 0 to 19
    print("{:>15.6f}{:>18.6f}{:>17.6f}{:>17.6f}{:>17.6f}".format((row**0.33333333333333333),(row**0.5),row,(row**2),(row**3)))
        
