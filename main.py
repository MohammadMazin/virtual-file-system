import threading
import json



def CreateFile(fname,cwd):
    if(cwd == ""):
        fname = fname
    else:
        fname = cwd + "//" + fname 
    path = fname.split("//")
    count = 0
    return CreateFileSearchRecursively(path, count, home["root"], path[-1])
def CreateFileSearchRecursively(list_e, index, fs, fname):
    #Traversing Directories
    if (list_e[index] in fs and (fname.find(".") == -1)):
        d2 = fs[list_e[index]]
        return CreateFileSearchRecursively(list_e, index + 1, d2, fname)
    else:
        if fname in fs.keys() and (fname.find(".") != -1):
            return "File Already Exists in this Directory!"
        elif fname not in fs.keys() and (fname.find(".") == -1):
            return "Enter an Extension with filename"
        else:
            if index < (len(list_e) - 1):
                d2 = fs[list_e[index]]
                return CreateFileSearchRecursively(list_e, index+1, d2, fname)
            else:
                fs[list_e[index]]= [fname,0, 0, False,[]]
                return "file created"



def CreateDirectory(fname, cwd):
    
    if(cwd == ""):
        fname = fname
    else:
        fname = cwd + "//" + fname 

    path = fname.split("//")
    count = 0
    return CreateDirectorySearchRecursively(path, count, home["root"], path[-1])
def CreateDirectorySearchRecursively(list_e, index, fs, fname):
    #Traversing Directories

    if (list_e[index] in fs and list_e[index]!=fname):
        d2 = fs[list_e[index]]
        return CreateDirectorySearchRecursively(list_e, index + 1, d2, fname)
    else:
        if fname in fs.keys():
            return "Directory Already Exists in this Directory!"
        else:
            fs[list_e[index]] = dict()
        
            if index < (len(list_e) - 1):
                d2 = fs[list_e[index]]
                return CreateDirectorySearchRecursively(list_e, index+1, d2, fname)

            return "New Directory Created"

            


def Delete(fname, cwd):
    if(cwd == ""):
        fname = fname
    else:
        fname = cwd + "//" + fname 
    path = fname.split("//")
    
    count = 0
    return DeleteSearchRecursively(path, count, home["root"], path[-1])
def DeleteSearchRecursively(list_e, index, fs, fname):
    if index < len(list_e) - 1:
        if (list_e[index] in fs):
            # print("directory found..")
            d2 = fs[list_e[index]]
            return DeleteSearchRecursively(list_e, index + 1, d2, fname)
    else:
        if(fname in fs and fs[fname][3] == False):
        # print("directory not found..")
            del fs[fname]
            return ("File " + fname + " has been deleted")
        elif(fname in fs and fs[fname][3] == True):
            return ("File is currently open. Cannot be deleted")
        else:
            return ("File not Found")



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


def WriteToFile(fname,data,cwd):
    if(cwd == ""):
        fname = fname
    else:
        fname = cwd + "//" + fname  
    list_f = fname.split("//")
    count = 0
    return WriteFileSearchRecursively(list_f,data,count,home["root"],list_f[-1])
def WriteFileSearchRecursively(list_e,data, index, fs, fname):
      if (list_e[index] in fs and list_e[index]!=fname):
        d2 = fs[list_e[index]]
        return WriteFileSearchRecursively(list_e,data, index + 1, d2, fname)
      else:
          if(list_e[index]==fname and fs[fname][3] == False):
              return ("File is not open.")
          elif list_e[index]==fname and fs[fname][3] == True: #file found
              chars = list(data)
              print(chars)
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
              return ("Text written to file.")

          



    

def WriteToFileAt(fname,index,input_data,cwd):
    if(cwd == ""):
        fname = fname
    else:
        fname = cwd + "//" + fname  
    list_f = fname.split("//")
    chars = list(input_data)
    print(chars)
    count = 0
    return WriteFileAtIndexSearchRecursively(chars,list_f,count,index,home["root"],list_f[-1])
def WriteFileAtIndexSearchRecursively(chars,list_e, index,start, fs, fname):
      if (list_e[index] in fs and list_e[index]!=fname):
        d2 = fs[list_e[index]]
        return WriteFileAtIndexSearchRecursively(chars, list_e, index + 1,start, d2, fname)
      else:
          if list_e[index]==fname and fs[fname][3] == True: #file found
              charIndex=0
              file = fs[fname][4]
              originalFileLength = len(fs[fname][4])
              start = int(start)
              for i in range(len(chars)):
                  if start < originalFileLength:
                    home["memBlock"][file[start]] = chars[i]
                    charIndex = charIndex+1
                    start= start+1
                    return "Text has been added to file"
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
                      return "Text has been added to file"
          elif list_e[index]==fname and fs[fname][3] == False:
               return "File is not open. Cannot be edited"

def OverwriteFileData(fname,input_data, cwd):
    if(cwd == ""):
        fname = fname
    else:
        fname = cwd + "//" + fname  
    list_f = fname.split("//")
    chars = list(input_data)
    count = 0
    return WriteFileAtIndexSearchRecursively(chars,list_f,count,0,home["root"],list_f[-1])

def ReadFromFile(fname,cwd):
    if(cwd == ""):
        fname = fname
    else:
        fname = cwd + "//" + fname 
    list_f = fname.split("//")
    count=0
    return ReadFileSearchRecursively(list_f,count,home["root"],list_f[-1])
def ReadFileSearchRecursively(list_e, index, fs, fname):
    if (list_e[index] in fs and list_e[index]!=fname):
        d2 = fs[list_e[index]]
        return ReadFileSearchRecursively(list_e, index + 1, d2, fname)
    else:
        if list_e[index]==fname and fs[fname][3] == True: #file found
              textoffile=""
            #   print( home["memBlock"].get(str(fs[fname][4])))
              for i in range(len(fs[fname][4])):
                if (home["memBlock"].get(str(fs[fname][4][i]))) is not None:
                    textoffile+=(home["memBlock"].get(str(fs[fname][4][i])))
                #(home["memBlock"].get(str(fs[fname][4][i])),end="")
              return textoffile
        elif list_e[index]==fname and fs[fname][3] == False:
            return ("File is not open. Cannot read text.")           



def ReadFromFileAt(fname,start,size, cwd):
    if(cwd == ""):
        fname = fname
    else:
        fname = cwd + "//" + fname   
    count = 0
    list_f = fname.split("//")
    start = int(start)
    size = int(size)
    return ReadIndexFileSearchRecursively(list_f, count, home["root"], list_f[-1], start, size)
def ReadIndexFileSearchRecursively(list_e, index, fs, fname,start, size):
    if (list_e[index] in fs and list_e[index]!=fname):
        d2 = fs[list_e[index]]
        return ReadIndexFileSearchRecursively(list_e, index + 1, d2, fname, start, size)
    else:
        if list_e[index]==fname and fs[fname][3] == True:
            cc=0
            strr = ""
            for c in range(len(fs[fname][4])):

                if (c >= start and cc< size):
                  strr = strr + home["memBlock"].get(str(fs[fname][4][c]))
                  cc+=1

            return (strr)
        if list_e[index]==fname and fs[fname][3] == False:
            return ("File is not open. Cannot read.")



def TruncateSize(size,fname, cwd):
    if(cwd == ""):
        fname = fname
    else:
        fname = cwd + "//" + fname  
    print("here we shall truncate file size")
    count = 0
    list_f = fname.split("//")
    return TruncateIndexFileSearchRecursively(list_f, count, home["root"], list_f[-1], size)
def TruncateIndexFileSearchRecursively(list_f, index, fs, fname,size):
    if (list_f[index] in fs and list_f[index]!=fname):
        d2 = fs[list_f[index]]
        return TruncateIndexFileSearchRecursively(list_f, index + 1, d2, fname, size)
    else:
        if fs[fname][3] == True:
            newList = fs[fname][4][0:size]
            for i in range(size, len(fs[fname][4])):
                j = str(fs[fname][4][i])
                home["memBlock"][j] = ''
            fs[fname][4] = newList
            fs[fname][1] = len(fs[fname][4])
            fs[fname][2] = len(fs[fname][4])

            return ("File has been truncated")
        elif fs[fname][3] == False:
            return ("File is not Open")

def Move(src,dest, cwd):
    
  src = cwd + src 
  s_list = src.split("//")
  d_list = dest.split("//")
  count = 0
  return MoveSearchRecursive(s_list, d_list,count, home["root"], s_list[-1],d_list[-1])
def MoveSearchRecursive(s_list, d_list, index, fs, sName, dName):
    if (s_list[index] in fs and s_list[index]!=sName):
        d2 = fs[s_list[index]]
        return MoveSearchRecursive(s_list,d_list, index + 1, d2,sName, dName)
    else:
      #File found
      if fs[sName][3] == False:
        fileContent = fs.get(s_list[index])
        key = sName
        del fs[s_list[index]]
        return MoveFileRecursive(fileContent, key, d_list, 0, home["root"], d_list[-1]) #IMPORTANT BUG MAYBE
      elif fs[sName][3] == True:
         return ("File is open and cannot be moved")
def MoveFileRecursive(fileContent, key, d_list,index, fs, dName):
      if (d_list[index] in fs.keys() and d_list[index]!=dName):
        d2 = fs[d_list[index]]
        return MoveFileRecursive(fileContent, key,d_list, index + 1, d2,dName)
      else:
        print(fs)
        fs[d_list[index]][key] = fileContent
        return ("File Has been moved")

def MoveWithinFile(fname,startIndex,size,toIndex, cwd):
    if(cwd == ""):
        fname = fname
    else:
        fname = cwd + "//" + fname   
    list = fname.split("//")
    count = 0
    startIndex = int(startIndex)
    size = int(size)
    toIndex = int(toIndex)
    return MoveWithinFileRecrusively(list, startIndex, size, toIndex, count, home["root"], list[-1])
def MoveWithinFileRecrusively(d_list, startIndex, endIndex, toIndex, index, fs, fName):
    if (d_list[index] in fs.keys() and d_list[index]!=fName):
        d2 = fs[d_list[index]]
        return MoveFileRecursive(d_list, startIndex,endIndex,toIndex,index + 1,d2,fName)
    else: #FileFound
        if fs[fName][3] == True:
            listData = fs[fName][4]
            for i in range(endIndex):
                listData[startIndex], listData[toIndex] =  listData[toIndex],  listData[startIndex]
                startIndex = startIndex+1
                toIndex = toIndex+1
            print(fs[fName][4]) 
            return ("File Data Has Been Moved")
        elif fs[fName][3] == False:
            return ("File is not Open")

def OpenFile(fname,cwd):
    if(cwd == ""):
        fname = fname
    else:
        fname = cwd + "//" + fname 
    list_f = fname.split("//")
    count=0
    return OpenFileSearchRecursively(list_f,count,home["root"],list_f[-1])
def OpenFileSearchRecursively(list_e, index, fs, fname):
    if (list_e[index] in fs and list_e[index]!=fname):
        d2 = fs[list_e[index]]
        return OpenFileSearchRecursively(list_e, index + 1, d2, fname)
    else:
        if list_e[index]==fname: #file found
            fs[fname][3] = True #File is opened
            return (fs[fname][0] + " is now open!")

def CloseFile(fname,cwd):
    if(cwd == ""):
        fname = fname
    else:
        fname = cwd + "//" + fname 
    list_f = fname.split("//")
    count=0
    return CloseFileSearchRecursively(list_f,count,home["root"],list_f[-1])
def CloseFileSearchRecursively(list_e, index, fs, fname):
    if (list_e[index] in fs and list_e[index]!=fname):
        d2 = fs[list_e[index]]
        return CloseFileSearchRecursively(list_e, index + 1, d2, fname)
    else:
        if list_e[index]==fname and fs[fname][3] == True: #file found and is open
            fs[fname][3] = False #File is opened
            return (fs[fname][0] + " has now been closed!")


#----------------------------------------------------------------------



def readFile(num, thread_number):
    
    outlist = []

    # f2 = open('block.json')
    # home["memBlock"] = json.load(f2)

    cwd = ""

    f = open("input_thread"+str(thread_number)+".txt")
    
    for line in f:
        print("thread#"+ str(thread_number)+ ": "+line, end=" ")
        lineargs = line.split()
        if (lineargs[0] == "create_directory"):  ##
            op = CreateDirectory(lineargs[1], cwd)
            op +='\n'
            outlist.append(op)


        elif (lineargs[0] == "create"):  ##
            op = CreateFile(lineargs[1],cwd)
            op +='\n'
            outlist.append(op)

        elif (lineargs[0] == "delete_file"): ##
            op = Delete(lineargs[1],cwd)
            op += '\n'
            outlist.append(op)

        elif (lineargs[0] == "show_memory_map"): ##
            aa = json.dumps(home["root"], indent=4)
            aa+= '\n'
            outlist.append(aa)


        elif (lineargs[0] == "change_directory"):
            cwd = Chdir(lineargs[1], cwd)
            cwd+= '\n'
            outlist.append("currentPath: " +cwd)

        elif (lineargs[0] == "write_to_file"): ##
            op =WriteToFile(lineargs[1],lineargs[2],cwd)
            op +='\n'
            outlist.append(op)


        elif (lineargs[0] == "read_file"): ##
            op = ReadFromFile(lineargs[1],cwd)
            op +='\n'
            outlist.append(op)

        elif (lineargs[0] == "read_file_at"): ## #ReadFromFileAt(file,index,size,cwd)
            op = ReadFromFileAt(lineargs[1],lineargs[2],lineargs[3],cwd)
            op +='\n'
            outlist.append(op)


        elif (lineargs[0] == "truncate_file"): ## #TruncateSize(size,file,cwd)
            op = TruncateSize(int(lineargs[2]),lineargs[1],cwd)
            op +='\n'
            outlist.append(op)


        elif (lineargs[0] == "move_file"): #Move(src,dest,cwd)
            op = Move(lineargs[1],lineargs[2],cwd)
            op +='\n'
            outlist.append(op)

        elif (lineargs[0] == "write_to_file_at"): #filename, index, content  ##
            op = WriteToFileAt(lineargs[1],lineargs[2],lineargs[3], cwd)
            print(op)
            op +='\n'
            outlist.append(op)

        elif (lineargs[0] == "move_within_file"): #file, startindex, size, toindex
            op = MoveWithinFile(lineargs[1],lineargs[2],lineargs[3],lineargs[4], cwd)
            op +='\n'
            outlist.append(op)

        elif (lineargs[0] == "overwrite_file"): ## #file, data
            op = OverwriteFileData(lineargs[1],lineargs[2],cwd)
            op +='\n'
            outlist.append(op)

        elif (lineargs[0] == "open"):  ##
            op = OpenFile(lineargs[1],cwd)
            op +='\n'
            outlist.append(op)

        elif (lineargs[0] == "close_file"): ##
            op = CloseFile(lineargs[1],cwd)
            op +='\n'
            outlist.append(op)

        elif (lineargs[0] == "exit"):       ##
            with open('data.dat', 'w') as f:
                json.dump(home, f)
            
        
    
    with open("output_thread"+str(thread_number)+".txt","w+") as outf:
        for element in outlist:
            outf.write(element)
        outf.close()



  
if __name__ == "__main__":
    f = open('data.dat')
    home = json.load(f)
    
    # creating thread
    numthread = int(input("Enter number of threads (Min:1  , Max:4): "))

    for i in range(1,numthread+1):
        # output=[]
        t = threading.Thread(target=readFile, args=(10,i))
        t.start()

        #open output_thread<i>.txt

        #dump in text file