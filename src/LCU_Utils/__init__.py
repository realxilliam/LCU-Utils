import os
import shutil

def init_mod(folder, name = "Custom mod"):

    folder = None
    lvl=30
    os.mkdir(folder+"/inst_tmp")
    shutil.copyfile('./script.sf', folder+'/inst_tmp/script.sf')
    os.chdir(folder)
    file=open("SCRIPT.TXT", 'r')
    content = file.read()
    found=False
    while (found==False):
        if ("level"+str(lvl)) in content:
            print('level'+str(lvl)+" already exits! testing next one")
            tmp=int(lvl)+1
            lvl=str(tmp)
        else:
            print('finally! level'+str(lvl)+" does not exist. embedding plugin there")
            file.close
            found=True
    file=open("SCRIPT.TXT", 'a') 
    file.write("\nlevel"+lvl+name)
    file.close
    shutil.copyfile('inst_tmp/script.sf', './level'+lvl+'.sf')
    shutil.rmtree("inst_tmp")
    return True