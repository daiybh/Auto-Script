from genericpath import isdir
import os
import configparser

def updateToMatser_follow_submoduleFile(folder):
    if(os.path.exists(folder+'/.gitmodules')==False):
        return
    os.chdir(folder)
    print('\n\n\n\n'+folder+'\n\n\n\n')
    config= configparser.ConfigParser()
#0 update currrent
    cmd = 'git pull'
    print(os.popen(cmd).read())
    config.read(folder+'/.gitmodules')

    section_list = config.sections()
    #print(section_list)
#1   git submodule foreach git pull origin master
    cmd = 'git submodule foreach git pull origin master'
    print(os.popen(cmd).read())
    
   #2  git status
    status = os.popen('git status').read()
    v1 = (status.split('\n'))
    vlist=[]
    for v in v1:
        a = v.find('modified:')
        
        if  a>0:
            b=v.find('(new commits')
            if(b>0):
                vlist.append(v[10:b].strip())
    if(len(vlist)==0):
        return


    cdict={}
    for a in section_list:
        path=config.get(a,"path")
        url=config.get(a,"url")
        #print(a,path,url)
        v = a.split('/')
        if(len(v)<2):
            continue
        cdict[path]=v[1][0:-1]    

    for v in vlist:
        if v in cdict.keys():            
            #3 git add v
            cmd =f'git add {v}'            
            print(os.popen(cmd).read())
            #4 git commit -m "update submodule"            
            cmd = f'git commit -m "update submodule {v}"'            
            print(os.popen(cmd).read())









def firstDir(path):
    list=[]
    if(os.path.exists(path)):
        files = os.listdir(path)        
        for file in files:
            m = os.path.join(path,file)            
            #os.chdir(path)
            if(os.path.isdir(m)):  
               # print('mmmmmmmmmmmmmmmmmmmmmmmmmmmmm',m)              
                updateToMatser_follow_submoduleFile(m)
                #print(os.getcwd())

firstDir(os.getcwd())