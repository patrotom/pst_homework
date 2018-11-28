import csv
Fe3=[]
Fe4=[]
with open('data/data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
           #print(row)
           if row[1]=='Fe3':
               Fe3.append(row[0])
           elif row[1]=='Fe4':
               Fe4.append(row[0])


print("Fe3: "+str(Fe3)+"\n")
print("Fe4: "+str(Fe4)+"\n")
            
