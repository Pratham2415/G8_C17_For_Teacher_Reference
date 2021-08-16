import matplotlib.pyplot as plt

Engine_Size = [3.5, 1.8, 2.8, 4.2, 2.5, 2.8, 2.8, 3.1, 3.8, 3.8, 3.8, 3.5, 1.8, 2.8, 4.2, 2.5, 2.8, 2.8, 3.1, 3.8]

Price = [42, 23, 33, 62, 26, 33, 38, 21, 25, 31, 85, 42, 23, 33, 62, 26, 33, 38, 21, 25]

New_Price=[]
New_Engine_Size=[]

plt.xlabel("Engine Size")
plt.ylabel("Count")
plt.hist(Engine_Size)
plt.show()

for i in range(len(Price)):
    if Engine_Size[i]>=2:
        New_Price.append(Price[i])
        New_Engine_Size.append(Engine_Size[i])
        
plt.xlabel("Engine Size in Cubic Centimeters(cc)")
plt.ylabel("Price in thousands")
plt.bar(New_Engine_Size, New_Price)
plt.show()