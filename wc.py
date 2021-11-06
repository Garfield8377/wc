def wc():
    try:
        #import wc
        import sys
        flag='-'
        inputArgs=sys.argv
        sign=0
        j=1
        for i in inputArgs[j:]:
            if flag in i:
                j=j+1
            else:
                sign=j
        k=0
        dat=[]
        x1=[]
        def line_count(data):
            return len(data.splitlines())
        def word_count(data):
            return len(data.split(b" "))
        def char_count(data):
            return len(data)
        t=''
        trx2=''
        
        if flag not in inputArgs[1:]:
            print("     ",line_count(inputArgs[-1]),"     ",word_count(inputArgs[-1]),"     ",char_count(inputArgs[-1]),"     ",inputArgs[-1])
        else:
            for t in inputArgs[sign:]:
                for x in inputArgs[1:sign]:
                    file=open(t,'r')
                    dat.append(file.read())
                    if x=='-l':
                        x1.append(line_count(dat[k]))
                    elif x=='-w':
                        x1.append(word_count(dat[k]))
                    elif x=='-c':
                        x1.append(char_count(dat[k]))
                    elif x=='-':
                        print('missing files')
                        break    
                    k=k+1
                x1.append(t)
            nNumber=len(inputArgs[sign:])
            def chunks(lst,n):
                d1=0
                for i in range(0,int(len(lst)/n)):
                    yield lst[d1:d1+int(len(lst)/n)]
                    d1=d1+int(len(lst)/n)
            strx2=''
            for d in chunks(x1,nNumber):
                    strx1='     '.join([str(elem)for elem in d])
                    #newstr=strx1.rstrip()
                    print("     "+strx1)
    except Exception:
        print("We don't handle that situation yet!")

if __name__=="__main__":
    wc()
    #python -m doctest -v doctest_wc.py

