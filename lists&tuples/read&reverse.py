#! /bin/usr/env python3
#
#   Author: Dal Whelpley
#   Project: Read from file and reverse
#   Date: 4/24/2019

def main():
    flipit = []
    reversd = []
    f = open("reverseit.txt", "r")

    f1 = f.readlines()

    for i in f1:
        reversd.append(i[::-1].lstrip('\n'))

    f.close()

    flipit.append(reversd[::-1])

    #with open("flipit.txt", "w") as f2:
    #    for item in flipit:
    #        #print("%s\n" % item)
    #        f2.write("\n".join(str(item)))
    #
    #f2.close()

if __name__ == "__main__":
    main()