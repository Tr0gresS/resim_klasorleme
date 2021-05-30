import os , shutil , datetime 
from colorama import Fore 

content = set()



print(Fore.RED+'''


_________         _________
\__   __/|\     /|\__   __/
   ) (   | )   ( |   ) (   
   | |   | (___) |   | |   
   | |   |  ___  |   | |   
   | |   | (   ) |   | |   
   | |   | )   ( |   | |   
   )_(   |/     \|   )_(   
                          
                    Resim Düzenleyici

[1] Başka dizine Geç 
[2] Çıkış

Klasörlenecek Uzantılar : .png / .jpg / .gif / .jpeg
''')

print(Fore.CYAN+"Kullanıcı'ya ait olan dizin -> ",os.path.expanduser("~"))

def move_image_():
    while True:  
        user_ = input(Fore.GREEN+"Seçiminiz ---->  ")
  
        if(user_ == "1"):
            try:
                user_path = input(Fore.LIGHTBLUE_EX+"Dizini Girin ]> ")
            except FileNotFoundError:
                pass

            os.chdir(user_path)
            for i in os.listdir():
                pathValue = os.path.splitext(i)[1]
                if(pathValue ==".png" or pathValue == ".jpg" or pathValue ==  ".jpeg" or pathValue ==  ".gif"):
                    file_time = datetime.datetime.fromtimestamp(os.stat(i).st_mtime).strftime("%Y-%m-%d'")
                    content.add(file_time)
                    for cont in content:
                        if(cont == file_time):
                            dosya_yolu = os.path.abspath(cont)
                            resim_yolu = os.path.abspath(i) 
                            try:
                                os.mkdir(cont) 
                            except FileExistsError :
                                    pass
                            try:
                                shutil.move(resim_yolu , dosya_yolu)
                            except shutil.Error:
                                pass
                            
       
                    
                    
         
        if(user_ == "2"):
            __import__("sys").exit()


if __name__ == "__main__":
    move_image_()