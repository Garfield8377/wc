import argparse
import sys
def line_count(data):
    return len(data.split(b'\n'))-1

def word_count(data):
        word = data.split()
        word_num = []
        for w in word:
            for character in w:
                if chr(character).isprintable():
                    word_num.append(w)
                    break
        return len(word_num)
def char_count(data):
    count=0
    for c in data:
        if chr(c).isprintable():
            count=count+1
    return count 
def width_calculator(line):
    count=0
    for c in line:
        if chr(c).isprintable():
            count=count+1
        elif chr(c)=='\t':
            count=count+8
    return count   
def folder_reader(txt):
    filefolder=[]
    with open(txt) as f1:
        data=f1.read()
    filename=data.split("\00")
    for f in filename[:-1]:
        filefolder.append(f)
    return filefolder
def max_line(file): #a.txt
    max_width = 0
    #line=str(file).split(b'\f','\r')
    for line in file:
       # print(line)
        if(width_calculator(line) > max_width):
            max_width=width_calculator(line)
    return(max_width) 
def wc():
    l_total=0
    w_total=0
    c_total=0
    m_total=0
    L_total=0
    list1=[]
    inputArgs=sys.argv
    #print(inputArgs[-1])
    filefolder=[]
    if '--files0-from=' in inputArgs[-1]:
        parser=argparse.ArgumentParser(description="calculate the word count in files")
        parser.add_argument('-l',action='store_true')
        parser.add_argument('-w',action='store_true')
        parser.add_argument('-c',action='store_true')
        parser.add_argument('-m',action='store_true')
        parser.add_argument('-L',action='store_true')
    #args=parser.parse_args() 
        args, unknown = parser.parse_known_args()
        #print(inputArgs[-1])
        input1=inputArgs[-1].split('=')
       # print(input1)
        filefolder=(folder_reader(str(input1[-1])))
        for f in filefolder:
       # data=open_argfile(args.filepath)
            with open(f,'rb') as f1:
                data=f1.read()
                c=f1.tell()
            #print(f)
            l = line_count(data)
            w = word_count(data)
            m = char_count(data)
            with open(f,'rb') as file:
                #print(file)
                L=max_line(file)
                list1.append(L)
            l_total=l_total+l
            w_total=w_total+w
            c_total=c_total+c
            m_total=m_total+m
       
            if args.l or args.w or args.c or args.m or args.L:
                print("\t"+args.l*(str(l)+"\t")+args.w*(str(w)+"\t")+args.c*(str(c)+"\t")+args.m*(str(m)+"\t")+args.L*(str(L)+"\t")+f)   
            else:
                print("\t"+str(l)+"\t"+str(w)+"\t"+str(c)+"\t"+f)
        L_total=max(list1)
        if len(filefolder)>1:
            #print("f.name>1")
            if args.l or args.w or args.c or args.m or args.L:
                #print("filepath>0")
                print('\t'+args.l*(str(l_total)+'\t')+args.w*(str(w_total)+'\t')+args.c*(str(c_total)+'\t')+args.m*(str(m_total)+'\t')+args.L*(str(L_total)+'\t')+"total")
            else:
                print("\t"+str(l_total)+"\t"+str(w_total)+"\t"+str(c_total)+"\t"+"total")
    #try:
    else:
        parser=argparse.ArgumentParser(description="calculate the word count in files")
        parser.add_argument('filepath',type=argparse.FileType('rb'), nargs='+')
        parser.add_argument('-l',action='store_true')
        parser.add_argument('-w',action='store_true')
        parser.add_argument('-c',action='store_true')
        parser.add_argument('-m',action='store_true')
        parser.add_argument('-L',action='store_true')
        args=parser.parse_args() 
        for f in args.filepath:
        # print(f) 
        # data=open_argfile(args.filepath)
            with open(f.name,'rb') as f1:
                data=f1.read()
                c=f1.tell()
                #L=max_line(f1)
            #print(f)
            l = line_count(data)
            w = word_count(data)
            m = char_count(data)
            L=max_line(f)
            list1.append(L)
            l_total=l_total+l
            w_total=w_total+w
            c_total=c_total+c
            m_total=m_total+m
           # L_total=max(list1)
            if args.l or args.w or args.c or args.m or args.L:
                print("\t"+args.l*(str(l)+"\t")+args.w*(str(w)+"\t")+args.m*(str(m)+"\t")+args.c*(str(c)+"\t")+args.L*(str(L)+"\t")+f.name)   
            else:
                print("\t"+str(l)+"\t"+str(w)+"\t"+str(c)+"\t"+f.name)
        
        L_total=max(list1)
           # print(i)
        #L_total=max(list1)
        if len(args.filepath)>1:
            if args.l or args.w or args.c or args.m or args.L:
                print('\t'+args.l*(str(l_total)+'\t')+args.w*(str(w_total)+'\t')+args.m*(str(m_total)+'\t')+args.c*(str(c_total)+'\t')+args.L*(str(L_total)+'\t')+"total")
            else:
                print("\t"+str(l_total)+"\t"+str(w_total)+"\t"+str(c_total)+"\t"+"total")
   

   # except Exception as e:
           # print("missing files")
            #print(e)
if __name__=="__main__":
        wc()
#python3 -m doctest -v doctest_unit_wc.py
#l w m c L


