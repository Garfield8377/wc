try:
    import sys
    file=open(sys.argv[-1],'r')
    data = file.read()
    NumberOfLines=len(data.splitlines())
    NumberOfWords=len(data.split())
    NumberOfChars=len(data)
    #flag='-'
    #class flags:
        #lines=len(data.splitlines())
        #words=len(data.split())
        #chars=len(data)
    #for input in flags:
# single combination
    if sys.argv[1]=='-l' and sys.argv[2]==sys.argv[-1]:
        print("   ",NumberOfLines,"   ",f"{ sys.argv[-1]}")
    elif sys.argv[1]=='-w' and sys.argv[2]==sys.argv[-1]:
        print("   ",NumberOfWords,"   ",f"{ sys.argv[-1]}")
    elif sys.argv[1]=='-c' and sys.argv[2]==sys.argv[-1]:
        print("   ",NumberOfChars,"   ",f"{ sys.argv[-1]}")
#lines
    elif sys.argv[1]=='-l' and sys.argv[2]=='-l' and sys.argv[3]==sys.argv[-1]:
        print("   ",NumberOfLines,"   ",f"{ sys.argv[-1]}")
    elif sys.argv[1]=='-l' and sys.argv[2]=='-l' and sys.argv[3]=='-l':   
        print("   ",NumberOfLines,"   ",f"{ sys.argv[-1]}")
#words
    elif sys.argv[1]=='-w' and sys.argv[2]=='-w'and sys.argv[3]==sys.argv[-1]:
        print("   ",NumberOfWords,"   ",f"{ sys.argv[-1]}")
    elif sys.argv[1]=='-w' and sys.argv[2]=='-w' and sys.argv[3]=='-w':
        print("   ",NumberOfWords,"   ",f"{ sys.argv[-1]}")
#chars
    elif sys.argv[1]=='-c'and sys.argv[2]=='-c'and sys.argv[3]==sys.argv[-1]:
        print("   ",NumberOfChars,"   ",f"{ sys.argv[-1]}")
    elif sys.argv[1]=='-c'and sys.argv[2]=='-c'and sys.argv[3]=='-c':
        print("   ",NumberOfChars,"   ",f"{ sys.argv[-1]}")
# double combination
    elif sys.argv[1]=='-l' and sys.argv[2]=='-w'and sys.argv[3]==sys.argv[-1]:
        print("   ",NumberOfLines,"   ",NumberOfWords,"   ",f"{ sys.argv[-1]}")
    elif sys.argv[1]=='-w' and sys.argv[2]=='-l'and sys.argv[3]==sys.argv[-1]:
        print("   ",NumberOfWords,"   ",NumberOfLines,"   ",f"{ sys.argv[-1]}")

    elif sys.argv[1]=='-l' and sys.argv[2]=='-c'and sys.argv[3]==sys.argv[-1]:
        print("   ",NumberOfLines,"   ",NumberOfChars,"   ",f"{ sys.argv[-1]}")
    elif sys.argv[1]=='-c' and sys.argv[2]=='-l'and sys.argv[3]==sys.argv[-1]:
        print("   ",NumberOfChars,"   ",NumberOfLines,"   ",f"{ sys.argv[-1]}")
    
    elif sys.argv[1]=='-w' and sys.argv[2]=='-c'and sys.argv[3]==sys.argv[-1]:
        print("   ",NumberOfWords,"   ",NumberOfChars,"   ",f"{ sys.argv[-1]}")
    elif sys.argv[1]=='-c' and sys.argv[2]=='-w'and sys.argv[3]==sys.argv[-1]:
        print("   ",NumberOfChars,"   ",NumberOfWords,"   ",f"{ sys.argv[-1]}")
# thiple combination
    elif sys.argv[1]=='-l' and sys.argv[2]=='-w' and sys.argv[3]=='-c':
        print("   ",NumberOfLines,"   ",NumberOfWords,"   ",NumberOfChars,f"{ sys.argv[-1]}")
# lines 
    elif sys.argv[1]=='-w' and sys.argv[2]=='-w' and sys.argv[3]=='-c':
        print("   ",NumberOfWords,"   ",NumberOfChars,f"{ sys.argv[-1]}")
    elif sys.argv[1]=='-c' and sys.argv[2]=='-w' and sys.argv[3]=='-c':
        print("   ",NumberOfChars,"   ",NumberOfWords,f"{ sys.argv[-1]}")
#w
    elif sys.argv[1]=='-l' and sys.argv[2]=='-l' and sys.argv[3]=='-c':
        print("   ",NumberOfLines,"   ",NumberOfChars,f"{ sys.argv[-1]}")
    elif sys.argv[1]=='-l' and sys.argv[2]=='-c' and sys.argv[3]=='-c':
        print("   ",NumberOfLines,"   ",NumberOfChars,f"{ sys.argv[-1]}")
#c
    elif sys.argv[1]=='-l' and sys.argv[2]=='-w' and sys.argv[3]=='-l':
        print("   ",NumberOfLines,"   ",NumberOfWords,f"{ sys.argv[-1]}")
    elif sys.argv[1]=='-l' and sys.argv[2]=='-w' and sys.argv[3]=='-w':
        print("   ",NumberOfLines,"   ",NumberOfWords,f"{ sys.argv[-1]}")
    #print(NumberOfLines,"   ",NumberOfWords,"   ",NumberOfChars,"   ",f"{ sys.argv[1]}") 
except Exception:
    print("We don't handle that situation yet!'")
