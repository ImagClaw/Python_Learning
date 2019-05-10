class Date:
    def __init__(self,m, d):
        self.__month = int(m)
        self.__day = int(d)

    def compareTo(self, m, d):
        self.__cmonth = m
        self.__cday = d
        if (self.__month < self.__cmonth or (self.__cmonth == self.__month and self.__day < self.__cday)):
             return -1     
        elif (self.__month == self.__cmonth and self.__cday == self.__day):
            return 0
        else:        
            return 1
         

def main():
    sep19 = Date(9, 19)
    dec15 = Date(12, 15)
    temp = Date(9, 19)
    sep11 = Date(9, 11)

    sep19bool = sep19.compareTo(9, 11) > 0
    sep11bool = sep11.compareTo(9, 19) < 0
    tempbool = temp.compareTo(9, 19) == 0
    dec15bool = dec15.compareTo(9,11) > 0

    print(sep19bool)
    print(sep11bool)
    print(tempbool)
    print(dec15bool)


if __name__ == "__main__":
    main()