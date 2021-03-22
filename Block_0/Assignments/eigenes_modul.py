'''
Created on 19.03.2021

@author: Lena Huber
'''

class ListKeeper:
    def __init__(self):
        self.data = dict()
        self.data['Liste'] = [1,2,3,4,5]
        
        
    #alle existierende Listnamen zeigen    
    def show(self):                     
        return self.data.keys()
           
    #neue Liste hinzufuegen
    def add(self, name, list_values):          
        if not name:
            return "Bitte geben Sie einen Namen an"
        self.data[name] = list_values
        return "Liste wurde hinzugefuegt"
    
    
    #Liste loeschen
    def delete(self, name):                    
        if name in self.data:
            self.data.pop(name)
            return "Erfolgreich entfernt"
        return "Fehler"
    
    
    #Liste sortieren
    def sort(self,name):                   
        if name in self.data:
            self.data[name].sort()
            return self.data[name]
        return "Fehler"
    
    
    #Listen erweitern
    def append(self,name, list_values):     
        if name in self.data:
            self.data[name].append(list_values)
            return "Liste erfolgreich erweitert"
        return "Name fehlt oder falscher Name"
    
    
    
        
                
        