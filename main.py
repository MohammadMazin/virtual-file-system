import json

def CreateFile(fname,cwd):
    if(cwd == ""):
        fname = fname
    else:
        fname = cwd + "//" + fname 
    path = fname.split("//")
    count = 0
    CreateFileSearchRecursively(path, count, home["root"], path[-1])
def CreateFileSearchRecursively(list_e, index, fs, fname):
    #Traversing Directories
    if (list_e[index] in fs and (fname.find(".") == -1)):
        d2 = fs[list_e[index]]
        CreateFileSearchRecursively(list_e, index + 1, d2, fname)
    else:
        if fname in fs.keys() and (fname.find(".") != -1):
            print("File Already Exists in this Directory!")
        elif fname not in fs.keys() and (fname.find(".") == -1):
            print("Enter an Extension with filename")
        else:
            if index < (len(list_e) - 1):
                d2 = fs[list_e[index]]
                CreateFileSearchRecursively(list_e, index+1, d2, fname)
            else:
                fs[list_e[index]]= [fname,0, 0, 0,[]]



def CreateDirectory(fname, cwd):
    
    if(cwd == ""):
        fname = fname
    else:
        fname = cwd + "//" + fname 

    path = fname.split("//")
    count = 0
    CreateDirectorySearchRecursively(path, count, home["root"], path[-1])
def CreateDirectorySearchRecursively(list_e, index, fs, fname):
    #Traversing Directories

    if (list_e[index] in fs and list_e[index]!=fname):
        d2 = fs[list_e[index]]
        CreateDirectorySearchRecursively(list_e, index + 1, d2, fname)
    else:
        if fname in fs.keys():
            print("Directory Already Exists in this Directory!")
        else:
            fs[list_e[index]] = dict()

            if index < (len(list_e) - 1):
                d2 = fs[list_e[index]]
                CreateDirectorySearchRecursively(list_e, index+1, d2, fname)

            


def Delete(fname, cwd):
    if(cwd == ""):
        fname = fname
    else:
        fname = cwd + "//" + fname 
    path = fname.split("//")
    
    count = 0
    DeleteSearchRecursively(path, count, home["root"], path[-1])
def DeleteSearchRecursively(list_e, index, fs, fname):
    if index < len(list_e) - 1:
        if (list_e[index] in fs):
            # print("directory found..")
            d2 = fs[list_e[index]]
            DeleteSearchRecursively(list_e, index + 1, d2, fname)
    else:
        if(fname in fs):
        # print("directory not found..")
            del fs[fname]
            print("File " + fname + " has been deleted")
        else:
            print("File not Found")



cwd = ""
def Chdir(path, cwd):
    if path == '--':
        if not '//' in cwd:
            return ""
        path = cwd
        print(path)
        path = path.split("//")
        lent = len(path[-1]) +2
        print(cwd[0:len(cwd) - lent])
        return cwd[0:len(cwd) - lent]
    else:
        # path = cwd + path
        path = path.split("//")
        print((path))
        count = 0
        return ChangeDirRecursively(path, count, home["root"], path[-1],cwd)
def ChangeDirRecursively(list_e, index, fs, fname,cwd):
    #Traversing Directories
    if (list_e[index] in fs and list_e[index]!=fname):
        d2 = fs[list_e[index]]
        if cwd =="":
            cwd  = list_e[index]
        else:
            cwd=cwd+"//"+list_e[index]
        return ChangeDirRecursively(list_e, index + 1, d2, fname,cwd)
    else:
        if list_e[index]==fname:
            if cwd == "":
                return (fname)
            else:
                return (cwd + "//" + fname)


def WriteToFile(fname,cwd):
    if(cwd == ""):
        fname = fname
    else:
        fname = cwd + "//" + fname  
    list_f = fname.split("//")
    input_data = input("Enter Text: ")
    chars = list(input_data)
    print(chars)
    count = 0
    WriteFileSearchRecursively(chars,list_f,count,home["root"],list_f[-1])
def WriteFileSearchRecursively(chars,list_e, index, fs, fname):
      if (list_e[index] in fs and list_e[index]!=fname):
        d2 = fs[list_e[index]]
        WriteFileSearchRecursively(chars, list_e, index + 1, d2, fname)
      else:
          if list_e[index]==fname: #file found
              charIndex=0

              for i in range(256):
                j = str(i)
                if home["memBlock"].get(j) == '':
                  home["memBlock"][j] = chars[charIndex]
                #   fs[fname][1] = int(fs[fname][1]) + len(chars)
                  fs[fname][4].append(j)
                  charIndex=charIndex+1
                  if charIndex >= len(chars):
                    break
              fs[fname][1] = len(fs[fname][4])
              fs[fname][2] = len(fs[fname][4])


    

def WriteToFileAt(fname,cwd):
    if(cwd == ""):
        fname = fname
    else:
        fname = cwd + "//" + fname  
    list_f = fname.split("//")
    index = int(input("Enter index to write at File"))
    input_data = input("Enter Text: ")
    chars = list(input_data)
    print(chars)
    count = 0
    WriteFileAtIndexSearchRecursively(chars,list_f,count,index,home["root"],list_f[-1])
def WriteFileAtIndexSearchRecursively(chars,list_e, index,start, fs, fname):
      if (list_e[index] in fs and list_e[index]!=fname):
        d2 = fs[list_e[index]]
        WriteFileAtIndexSearchRecursively(chars, list_e, index + 1,start, d2, fname)
      else:
          if list_e[index]==fname: #file found
              charIndex=0
              file = fs[fname][4]
              originalFileLength = len(fs[fname][4])
              for i in range(len(chars)):
                  if start < originalFileLength:
                    home["memBlock"][file[start]] = chars[i]
                    charIndex = charIndex+1
                    start= start+1
                  else:
                      for i in range(256):
                            j = str(i)
                            if home["memBlock"].get(j) == '':
                                home["memBlock"][j] = chars[charIndex]
                                fs[fname][1] = int(fs[fname][1]) + len(chars)
                                fs[fname][4].append(j)
                                charIndex=charIndex+1
                            if charIndex >= len(chars):
                                break
                            fs[fname][1] = len(fs[fname][4])
                            fs[fname][2] = len(fs[fname][4])

def OverwriteFileData(fname, cwd):
    if(cwd == ""):
        fname = fname
    else:
        fname = cwd + "//" + fname  
    list_f = fname.split("//")
    input_data = input("Enter Text: ")
    chars = list(input_data)
    count = 0
    WriteFileAtIndexSearchRecursively(chars,list_f,count,0,home["root"],list_f[-1])

def ReadFromFile(fname,cwd):
    if(cwd == ""):
        fname = fname
    else:
        fname = cwd + "//" + fname 
    list_f = fname.split("//")
    count=0
    ReadFileSearchRecursively(list_f,count,home["root"],list_f[-1])
def ReadFileSearchRecursively(list_e, index, fs, fname):
    if (list_e[index] in fs and list_e[index]!=fname):
        d2 = fs[list_e[index]]
        ReadFileSearchRecursively(list_e, index + 1, d2, fname)
    else:
        if list_e[index]==fname: #file found
              for i in range(len(fs[fname][4])):
                print(home["memBlock"].get(str(fs[fname][4][i])),end="")            



def ReadFromFileAt(fname,start,size, cwd):
    if(cwd == ""):
        fname = fname
    else:
        fname = cwd + "//" + fname   
    count = 0
    list_f = fname.split("//")
    ReadIndexFileSearchRecursively(list_f, count, home["root"], list_f[-1], start, size)
def ReadIndexFileSearchRecursively(list_e, index, fs, fname,start, size):
    if (list_e[index] in fs and list_e[index]!=fname):
        d2 = fs[list_e[index]]
        ReadIndexFileSearchRecursively(list_e, index + 1, d2, fname, start, size)
    else:
        if list_e[index]==fname:
            cc=0
            strr = ""
            for c in range(len(fs[fname][4])):

                if (c >= start and cc< size):
                  strr = strr + home["memBlock"].get(str(fs[fname][4][c]))
                  cc+=1
            print(strr)



def TruncateSize(size,fname, cwd):
    if(cwd == ""):
        fname = fname
    else:
        fname = cwd + "//" + fname  
    print("here we shall truncate file size")
    count = 0
    list_f = fname.split("//")
    TruncateIndexFileSearchRecursively(list_f, count, home["root"], list_f[-1], size)
def TruncateIndexFileSearchRecursively(list_f, index, fs, fname,size):
    if (list_f[index] in fs and list_f[index]!=fname):
        d2 = fs[list_f[index]]
        TruncateIndexFileSearchRecursively(list_f, index + 1, d2, fname, size)
    else:
        newList = fs[fname][4][0:size]
        for i in range(size, len(fs[fname][4])):
          j = str(fs[fname][4][i])
          home["memBlock"][j] = ''
        fs[fname][4] = newList
        fs[fname][1] = len(fs[fname][4])
        fs[fname][2] = len(fs[fname][4])

def Move(src,dest, cwd):
    
  src = cwd + src 
  s_list = src.split("//")
  d_list = dest.split("//")
  count = 0
  MoveSearchRecursive(s_list, d_list,count, home["root"], s_list[-1],d_list[-1])
def MoveSearchRecursive(s_list, d_list, index, fs, sName, dName):
    if (s_list[index] in fs and s_list[index]!=sName):
        d2 = fs[s_list[index]]
        MoveSearchRecursive(s_list,d_list, index + 1, d2,sName, dName)
    else:
      #File found
      fileContent = fs.get(s_list[index])
      key = sName
      MoveFileRecursive(fileContent, key, d_list, 0, home["root"], d_list[-1])
      del fs[s_list[index]]
def MoveFileRecursive(fileContent, key, d_list,index, fs, dName):
      if (d_list[index] in fs.keys() and d_list[index]!=dName):
        d2 = fs[d_list[index]]
        MoveFileRecursive(fileContent, key,d_list, index + 1, d2,dName)
      else:
        print(fs)
        fs[d_list[index]][key] = fileContent

def MoveWithinFile(fname, cwd):
    if(cwd == ""):
        fname = fname
    else:
        fname = cwd + "//" + fname   
    list = fname.split("//")
    count = 0
    startIndex = int(input("Enter Starting Index: "))
    size = int(input("Enter Ending Index: "))
    toIndex = int(input("Enter Index That Data Should be Moved To: "))
    MoveWithinFileRecrusively(list, startIndex, size, toIndex, count, home["root"], list[-1])
def MoveWithinFileRecrusively(d_list, startIndex, endIndex, toIndex, index, fs, fName):
    if (d_list[index] in fs.keys() and d_list[index]!=fName):
        d2 = fs[d_list[index]]
        MoveFileRecursive(d_list, startIndex,endIndex,toIndex,index + 1,d2,fName)
    else: #FileFound
        listData = fs[fName][4]
        for i in range(endIndex):
           listData[startIndex], listData[toIndex] =  listData[toIndex],  listData[startIndex]
           startIndex = startIndex+1
           toIndex = toIndex+1
        print(listData)
    
#----------------------------------------------------------------------
#main

f = open('data.dat', )
home = json.load(f)

# f2 = open('block.json')
# home["memBlock"] = json.load(f2)

cwd = ""

while (True):
    print()
    print("Choose an Option:")
    print('------------------------------------------')
    print("1: Create Directory",end='')
    print("\t\t2: Create New File")
    print("3: Delete file",end='')
    print("\t\t\t4: Show Directories Structure")
    print("5: Change the directory",end='')
    print("\t\t6: Append Content to File")
    print("7: Read from Whole File",end='')
    print("\t\t8: Read from File at Index")
    print("9: Truncate File: ",end='')
    print("\t\t10: Move File To New Directory")
    print("11: Write at Index of File",end='')
    print("\t12: Move Data within a file")
    print("13: Overwrite File Content")
    print('------------------------------------------')
    print("99: To Exit")
    
    choice = int(input("Enter Choice: "))
    print()

    if choice == 1:
        get_stuff = input("Enter Directory Name to Create: ")
        CreateDirectory(get_stuff, cwd)
    elif choice == 2:
        get_stuff = input("Enter File Name to Create: ")
        CreateFile(get_stuff,cwd)
    elif choice == 3:
        get_stuff = input("Enter File Name to Delete: ")
        Delete(get_stuff, cwd)
    elif choice == 4:
        aa = json.dumps(home["root"], indent=4)
        print(aa)
    elif choice == 5:
        get_stuff = input("Enter Path to change too: ")
        cwd = Chdir(get_stuff, cwd)
        print("currentPath: " +cwd)
    elif choice == 6:
        get_stuff = input("Enter Filename to append text too: ")
        WriteToFile(get_stuff, cwd)
    elif choice == 7:
        get_stuff = input("Enter Filename to read text from: ")
        ReadFromFile(get_stuff, cwd)
    elif choice == 8:
        get_stuff = input("Enter Filename to read text from: ")
        index = int(input("Enter index to start reading from: "))
        size = int(input("Enter size to read: "))
        ReadFromFileAt(get_stuff,index,size,cwd)
    elif choice == 9:
        get_stuff = input("Enter Filename to truncate data from: ")
        size = int(input("Enter size to truncate: "))
        TruncateSize(size,get_stuff, cwd)
    elif choice == 10:
        src = input("Enter Filename to move: ")
        dest = input("Enter destination folder: ")
        Move(src,dest,cwd)
    elif choice == 11:
        get_stuff = input("Enter Filename to write text to: ")
        WriteToFileAt(get_stuff, cwd)
    elif choice == 12:
        get_stuff= input("Enter Filename You Want to Access:")
        MoveWithinFile(get_stuff, cwd)
    elif choice == 13:
        get_stuff= input("Enter Filename You Want to Overwrite:")
        OverwriteFileData(get_stuff,cwd)

    elif choice == 99:
        print("Bye Bye")
        with open('data.dat', 'w') as f:
            json.dump(home, f)
        break
    else:
      print('go again')