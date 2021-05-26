#for processing binary data or store variables in a program

#write into file
# with open("binary", 'bw') as bin_file:
#     for i in range(17):
#         bin_file.write(bytes([i])) #convert numbers in the list into hexadecimal code
#         #bin_file.write(i)  #this will turn line of code into ints
# #read content of file onto terminal
# with open("binary", 'br') as binFile:
#     for b in binFile:
#         print(b)


#--------------------------

# with open("binary", 'bw') as bin_file:
#     bin_file.write(bytes(range(17)))

# with open("binary", 'br') as binFile:
#     for b in binFile:
#         print(b)

#-----------------------------
#character codes with hex equivalent
a = 65534 # FF FE
b = 65535 # FF FF
c = 65536 # 00 01 00 00
x = 2998302 # 00 2D C0 1E

with open("binary2.txt", 'bw') as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'little'))

with open("binary2.txt", 'br') as bin_file:
    print(binFile.readlines())

#review other methods to read out and convert binary numbers <---> hex