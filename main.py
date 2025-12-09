import tkinter as tk

width = 250
height = 250
pad = 5
window = tk.Tk()
window.title("BMI Calculator")
window.minsize(width, height)

bg_color = "#a19a89"
window.config(bg=bg_color)



label1 = tk.Label(bg=bg_color,fg="black", text="Enter Your KG")
label2 = tk.Label(bg=bg_color,fg="black", text="Enter Your Height (cm)")
label3 = tk.Label(bg=bg_color,fg="black", anchor="center")

firstEntry = tk.Entry(fg="black")
secondEntry = tk.Entry(fg="black")

calc_button = tk.Button(text="Calculate", fg="black")


label1.pack(pady= pad)

firstEntry.pack(pady= pad)

label2.pack(pady= pad)

secondEntry.pack(pady= pad)

calc_button.pack(pady= pad)


def calculate():
    try:
        kg = int(firstEntry.get())
        height = int(secondEntry.get())
        result = kg / (height/100 * height/100)

        status = ""
        if result < 18.5:
            status = "You are underweight"

        elif 18.5 < result <= 25:
            status = "You are normal"
        elif 25 < result <= 29.9:
            status = "You are overweight"
        elif 29.9 < result <= 34.9:
            status = "You are medically obese"
        elif 34.9 < result <= 39.9:
            status = "You are medically obese"
        elif result > 39.9:
            status = "You are extreme obese"

        label3.pack(pady= pad)
        label3.config(fg="black",wraplength=200,text=f"Your BMI is: {round(result, 2)}. {status}")


    except Exception as e:
        label3.pack(pady= pad)
        label3.config(text="Please enter only your weight and height.")

calc_button.config(command=calculate)


window.mainloop()