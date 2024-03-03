import re


vlan_line = []
print("input config\n")
while True:
    try:
        line = input()
        if re.search("switchport trunk allowed", line):
            m = re.search("\d(.*)", line).group()
            vlan_line.append(m)
    except EOFError:
        break
for vlans in vlan_line:
    vlans = vlans.split(",")

    for i in range (0,len(vlans)):
        if (vlans[i].find("-")) != -1:
            vlan_range = vlans[i]
            list = []
            list = vlan_range.split("-")
            start = int(list[0])
            end = int(list[1])

            for j in range (start,end+1):
                print (j)
        else:
            print (vlans[i])
