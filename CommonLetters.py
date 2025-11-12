#Common letters jo sabme hain unhe print kare
names =["vanshika","ashi","alshifa","harshita"]
common = set(names[0])
for i in names[1:]:
    common&=set(i)

print(common)