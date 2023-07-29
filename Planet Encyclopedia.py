from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
root = Tk()
root.title("Planet Encyclopedia")
root.geometry("500x500")
root.configure(background="lightblue")

Mercury = ImageTk.PhotoImage(Image.open("mercury.jpg"))
Venus = ImageTk.PhotoImage(Image.open("venus.jpg"))
Earth = ImageTk.PhotoImage(Image.open("earth.jpg"))
Mars =  ImageTk.PhotoImage(Image.open("a.jpg"))
Jupiter = ImageTk.PhotoImage(Image.open("b.jpg"))
Saturn = ImageTk.PhotoImage(Image.open("c.jpg"))
Uranus = ImageTk.PhotoImage(Image.open("d.jpg"))
Neptune = ImageTk.PhotoImage(Image.open("e.jpg"))


label_planet = Label(root, text = "Planet : ", bg = "lightblue")
label_planet_name = Label(root, font = ("courier",18,"bold"), bg = "lightblue")
label_planet_image = Label(root, bg = "gold2", highlightthickness=5, borderwidth=2, relief=SOLID)
label_gravity_radius = Label(root, font = ("casteller"), bg = "lightblue")
label_info = Label(root, font = ("courier",10,"bold"),bg = "lightblue", wraplength=500)

planets = ["Mercury", "Venus", "Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
selectedval = StringVar()
dropdown = ttk.Combobox(root, value = planets, textvariable = selectedval)
def planetInfo():
    planet = selectedval.get()
    if planet=="Mercury":
        label_planet_name["text"] = "Mercury"
        label_planet_image["image"] = Mercury
        label_gravity_radius["text"] = "Gravity : 3.7 m/s² \n Radius : 2,439.7 km"
        label_info["text"] = "Mercury is the smallest planet in our solor system. I it is just little bigger than Earth's moon."
    if planet=="Venus":
         label_planet_name["text"] = "Venus"
         label_planet_image["image"] = Venus
         label_gravity_radius["text"] = "Gravity : 8.87 m/s² \n Radius : 6,051.8 km"
         label_info["text"] = "Venus is the brightest object in the sky after the Sun and the Moon, and sometimes looks like a bright star in the morning or evening sky."
    if planet=="Earth":
        label_planet_name["text"] = "Earth"
        label_planet_image["image"] = Earth
        label_gravity_radius["text"] = "Gravity : 9.807 m/s² \n Radius : 6,371 km"
        label_info["text"] = "Earth is the only planet in the known universe confirmed to host life and it's the only one known for sure to have liquid water on its surface."
    if planet=="Mars":
       label_planet_name["text"] = "Mars"
       label_planet_image["image"] = Mars
       label_gravity_radius["text"] = "Gravity : 3.71 m/s² \n Radius : 3,389.5 km"
       label_info["text"] = "​Mars is the fourth planet from the Sun. It has very thin atmosphere .Mars is also a dynamic planet with seasons, polar ice caps, canyons, extinct volcanos active in the past."
    if planet=="Jupiter":
       label_planet_name["text"] = "Jupiter"
       label_planet_image["image"] = Jupiter
       label_gravity_radius["text"] = "Gravity : 24.79 m/s² \n Radius : 69,911 km"
       label_info["text"] = "Jupiter is the fifth planet. Jupiter is called a gas giant planet. Its atmosphere is made up of mostly hydrogen gas and helium gas, like the sun."
    if planet=="Saturn":
       label_planet_name["text"] = "Saturn"
       label_planet_image["image"] = Saturn
       label_gravity_radius["text"] = "Gravity : 10.44 m/s² \n Radius : 58 232 km"
       label_info["text"] = "Saturn is the sixth planet from the Sun and the second-largest planet in our solar system. Saturn is a massive ball made mostly of hydrogen and helium."
    if planet=="Uranus":
       label_planet_name["text"] = "Uranus"
       label_planet_image["image"] = Uranus
       label_gravity_radius["text"] = "Gravity : 8.87 m/s² \n Radius : 25,362 km"
       label_info["text"] = "Uranus is the seventh planet from the Sun, and has the third-largest diameter in our solar system. It was the first planet found with the aid of a telescope"
    if planet=="Neptune":
       label_planet_name["text"] = "Neptune"
       label_planet_image["image"] = Neptune
       label_gravity_radius["text"] = "Gravity : 11.15 m/s² \n Radius : 24,622 km"
       label_info["text"] = "Neptune is the eighth planet from the sun, the fourth largest, and a gas planet. It is named after the Roman god of the sea. Neptune is four times the size of Earth."
    
dropdown.place(relx = 0.5, rely = 0.1, anchor = CENTER)
    
btn = Button(root, text = "Show Planet Info", command = planetInfo)
btn.place(relx = 0.5, rely = 0.18, anchor = CENTER)

label_planet.place(relx = 0.2, rely = 0.1, anchor = CENTER)
label_planet_name.place(relx = 0.5, rely = 0.25, anchor = CENTER)
label_planet_image.place(relx = 0.5, rely = 0.5, anchor = CENTER)
label_gravity_radius.place(relx = 0.5, rely = 0.8, anchor = CENTER)
label_info.place(relx = 0.5, rely = 0.9, anchor = CENTER)

root.mainloop()
