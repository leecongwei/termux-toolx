# Tool Name :- termux-toolx
# Author :- 黑k江湖
# Date :- 15/10/2020

import os
import sys
from time import sleep
from modules.logo import *
from modules.system import *

class tool:
  @classmethod
  def install(self):
    while True:
      system=sys()
      os.system("clear")
      logo.ins_tnc()
      inp=input("\033[1;33m 前方施工不能下载 [不给你开/没有选择]> \033[00m")                               if inp=="y" or inp=="yes":
        os.system("clear")
        logo.installing()
        if system.sudo is not None:
          #require root permission
          if os.path.exists(system.conf_dir+"/termux-toolx"):
            pass                                                                                               else:
            os.system(system.sudo+" mkdir "+system.conf_dir+"/termux-toolx")
          os.system(system.sudo+" cp -r modules core termux-toolx.py "+system.conf_dir+"/termux-toolx")
          os.system(system.sudo+" cp -r core/termux-toolx "+system.bin)
          os.system(system.sudo+" cp -r core/toolx "+system.bin)
          os.system(system.sudo+" chmod +x "+system.bin+"/termux-toolx")
          os.system(system.sudo+" chmod +x "+system.bin+"/toolx")
          os.system("cd .. && "+system.sudo+" rm -rf termux-toolx")
          if os.path.exists(system.bin+"/termux-toolx") and os.path.exists(system.conf_dir+"/termux-toolx"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("\033[1;36m ##> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("\033[1;36m ##> \033[00m")
            break
        else:
          if os.path.exists(system.conf_dir+"/termux-toolx"):
            pass
          else:
            os.system("mkdir "+system.conf_dir+"/termux-toolx")
          os.system("cp -r modules core termux-toolx.py "+system.conf_dir+"/termux-toolx")
          os.system("cp -r core/termux-toolx"+system.bin)
          os.system("cp -r core/toolx "+system.bin)
          os.system("chmod +x "+system.bin+"/termux-toolx")
          os.system("chmod +x "+system.bin+"/toolx")
          os.system("cd .. && rm -rf termux-toolx")
          if os.path.exists(system.bin+"/termux-toolx") and os.path.exists(system.conf_dir+"/termux-toolx"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("\033[1;36m ##> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("\033[1;36m ##> \033[00m")
            break
      else:
        break
       else:
        break

if __name__=="__main__":
  try:
    tool.install()
  except KeyboardInterrupt:
    os.system("clear")
    logo.exit()
