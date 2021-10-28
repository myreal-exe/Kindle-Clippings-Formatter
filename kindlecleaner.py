# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 00:18:50 2021

@author: myreal-exe
"""

s=""
with open("clips.txt","r",encoding='utf-8-sig') as f:
	f.seek(0)
	s=f.read()
    
s=s.split("==========\n")

titles=list([])

for i in range(len(s)):
    s[i]=s[i].replace("\ufeff","")
    note = s[i].split("\n")
    titles.append((note[0].replace("\ufeff","")))

titles=list(set(titles))[1:]

loc_dict_list=dict.fromkeys(titles)
for k in loc_dict_list.keys():
    loc_dict_list[k]=[]
    

for t in range(len(titles)):
    f=open(str(titles[t])+".txt","a")
    f.seek(0)
    
    for i in range(len(s)-1):
        
        note=s[i]
        note=note.split("\n") 
        
        if note[0] != titles[t]:
            continue
        
        loc=note[1].split(" ")[5]
        loc = loc.split("-")[0] if loc.find("-") != -1 else loc
        
        if loc in loc_dict_list[titles[t]] :
            continue
        loc_dict_list[titles[t]].append(loc)
 
        f.write(note[3]+"\n\n")
    f.close()
		

	
	