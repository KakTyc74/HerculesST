f = open ('Exported ST.txt', 'r')
fnew = open ('HerculesST.seq', 'w')
addresses = ['E', 'AB', 'AD', 'AW', 'A', 'EB', 'ED', 'EW', 'M', 'MB', 'MW', 'T', 'Z', 'FC', 'DB', 'UDT', 'SFC', 'PAW', 'PEW', 'IDB', 'OB', 'FB', 'SFB', 'SFC', 'MD']
doubletype = ['FC', 'FB', 'OB', 'DB', 'UDT', 'SFB', 'SFC']
n=0
for actline in f:
#    actline = f.readline()
    for vartype in addresses:
        addresstype = str(' ' + vartype + ' ')
        spos = actline.find (addresstype)
##        try:
##            a = int (actline[spos + len(addresstype) : ].split(' ')[0])
##        except:
##            print (actline[spos + len(addresstype) : ])
##            pass
##        else:
##            print (str(a))
#        print (type (actline[spos + len(addresstype) : ].split(' ')[0]))
#        if type (actline[spos + len(addresstype) : ].split(' ')[0]) == int :
#            pass
#        else:
#            spos = actline[spos + len(addresstype) : ].find(addresstype)
        if spos != -1:
#            perc = (f.readline-f.index(actline))/len(f)
#            print(str(perc) + '%\r', end='')
            try:
                symbolname = actline[0:spos]
            except:
                pass
            try:
                address = actline [spos + len(addresstype):].split(' ')[0]
            except:
                address = ''
                pass
            try:
                if vartype in doubletype:
                    datatype = actline [spos + len(addresstype):].split(' ')[1] + actline [spos + len(addresstype):].split(' ')[2]
                else:    
                    datatype = actline [spos + len(addresstype):].split(' ')[1]
            except:
#                print ('Ошибка в строке: ', f.index(actline))
                pass
            try:
                comment = actline [spos + len(addresstype) + len(address) + len(datatype) + len(2 * ' '):-1]
            except:
                comment = ''
                pass

            fnew.writelines('\t' + addresstype + address + '\t' + symbolname + '\t' + comment + '\n')
            break
  

          # comment = actline [spos + len(addresstype) + len(address) + len(datatype) + len(2 * ' '):]

f.close()
fnew.close()
