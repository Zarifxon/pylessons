import warnings
from inspect import getframeinfo , currentframe

class Backpack:
    def __init__(self , name) -> None:
        self.__name = name 
        self.content = [] 

    
    def __str__(self):
        return f"Backpack <{self.__name}> : {','.join(self.content)}"

    def add(self , item,):
        self.content.append(item)

    
    def __eq__(self, item):
        if(isinstance(item, Backpack)):
            pass 
        else:
            warnings.warn(f"Обьект Ссравнивается с другим типом. {getframeinfo(currentframe()).lineno}")            
            return False

bp = Backpack("kwutge")



if(bp == 5):
    print("fsjdf")
else:
    print("Hello world")




