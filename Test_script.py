#!/usr/bin/python
import os
import scipy

# To execute the gnu radio scipt in a shell

os.system("./uhd_fft.py")
os.system('clear')  #clear the terminal
print 'Done executing script'
# A one line python command to read the entire file into a numpy array

f= scipy.fromfile(open("value"), dtype=scipy.float32)  # file value is the file generated by the gnu radios scripts file sink block

print f # to print the values of the fft , need to figure this out further, what the values is and so forth


#Rest of the psuedo code

#Take value of the first 16 Mhz segment, save in an array , do the same for the rest of the spectrum

# Figure out a way commute the total in the end