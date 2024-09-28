#this prohram is to convert Roman number to integer
#credit to tutorials point

def Roman_To_integer(s):

    roamn = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    s=s.upper()
    i=0
    num=0
    while i < len(s):
        if i+1<len(s) and s[i:i+2] in roamn:
            num+=roamn[s[i:i+2]]
            i+=2
        else:
            num+=roamn[s[i]]
            i+=1
    return num

if __name__ =="__main__":
    s=input("Enter the Roman number ")
    print(Roman_To_integer(s))