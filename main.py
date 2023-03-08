
import datetime
# create a file with a unique datetime
filename = 'ipFile_{}.txt'.format(datetime.datetime.now().strftime("%m-%d-%Y_%H%M%S"))
f = open(filename, 'w')

def firstIP():
    userIP = (input('put an ip number: '))
    return userIP

def numSIMs():
    userNum = (input('Put a sim number: '))
    userNum = int(userNum)
    return userNum

def ipGenerator(ip, sNum):
    ipArray = ip.split(".")
    quad1 = int(ipArray[0])
    quad2 = int(ipArray[1])
    quad3 = int(ipArray[2])
    quad4 = int(ipArray[3])

    # let's make a funtion we can use later to convert the IP into proper format
    def formatIP(q1, q2, q3, q4):
        # let's transfer our address into 12 digit format
        tupArray = ['%03d' % q1, '%03d' % q2, '%03d' % q3, '%03d' % q4]
        # let's join the quads with '.' separators
        formattedIP = ('.'.join((x) for x in tupArray))
        return formattedIP

    counter = 0
    maxIP = 254

    print("Your file is in this directory under: " + f.name)
    f.write(formatIP(quad1, quad2, quad3, quad4) + "\n")
    # let's print a succession of IPs by incrementing until reached sim Number
    while (counter < sNum - 1):
        print(formatIP(quad1, quad2, quad3, quad4))
        quad4 += 1
        counter += 1
        if (quad4 <= maxIP):
            f.write(formatIP(quad1, quad2, quad3, quad4) + "\n")
        else:
            quad4 = 1
            if (quad3 <= maxIP):
                quad3 += 1
                f.write(formatIP(quad1, quad2, quad3, quad4) + "\n")
            else:
                quad3 = 1
                if (quad2 <= maxIP):
                    quad2 += 1
                    f.write(formatIP(quad1, quad2, quad3, quad4) + "\n")
                else:
                    print("You've exceeded your network allocation!")
                    return


ipGenerator(firstIP(), numSIMs())
