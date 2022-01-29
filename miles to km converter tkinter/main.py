from tkinter import *

def miles_2_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilo_results_label.config(text=f"{km}")

window = Tk()
window.title("Miles to KM converter")
window.config(padx=40, pady=20)

miles_input = Entry(width= 7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilo_results_label = Label(text="0")
kilo_results_label.grid(column=1, row=1)

kilo_label = Label(text="km")
kilo_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_2_km)
calculate_button.grid(column=1, row=2)

window.mainloop()