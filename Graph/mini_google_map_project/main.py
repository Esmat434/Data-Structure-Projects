import cv2
import matplotlib.pyplot as plt

from mini_google_map import MiniGoogleMaps
from cities import nodes,cities,routes

if __name__ == '__main__':

    while True:
        st = input("Please Enter Your Place: ")
        dist = input("Please Enter Your Distanation: ")
        st = st.title().strip()
        dist = dist.title().strip()
        if st in nodes and dist in nodes:
            break
        if st not in nodes:
            print("Your place is incorrect.")
        if dist not in nodes:
            print("Your distanation is incorrect.") 

    my_map = MiniGoogleMaps(nodes,routes)
    shortest_path = my_map.get_shortest_path_cost(st,dist)

    fig, ax = plt.subplots(figsize=(10,10))
    ax.set_xlim(0, 500)  
    ax.set_ylim(0, 500)
    
    img = cv2.imread(r"C:\Users\DELL\Videos\Python\Data_Structure\Data_Structure\Graph\mini_google_map_project\city.png")
    if img is None:
        raise FileNotFoundError("❌ عکس شهر پیدا نشد! مسیر را چک کنید.")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (30, 30))  
    
    for name, (x, y) in cities.items():
        ax.imshow(img, extent=(x-5, x+5, y-5, y+5)) 
        ax.text(x, y-10, name, ha='center', fontsize=5)  
    
    for start, end, _ in routes:
        x1, y1 = cities[start]
        x2, y2 = cities[end]
        ax.plot([x1, x2], [y1, y2], 'b-', linewidth=1.5)
    
    if shortest_path:
        shortest_path = shortest_path[:-1]
        for index in range(len(shortest_path)-1):
            x1, y1 = cities[shortest_path[index]]
            x2, y2 = cities[shortest_path[index+1]]
            ax.plot([x1,x2], [y1,y2], 'r-', linewidth=1.5)
        plt.axis('off')
        plt.show()
    else:
        print("This target is invalid.")