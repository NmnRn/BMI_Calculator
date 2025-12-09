import tkinter as tk

width = 250
height = 250
window = tk.Tk()
window.title("BMI Calculator")
window.minsize(width, height)
window.resizable(False, False)
window.config(bg="#a19a89")



label1 = tk.Label(fg="black", text="Enter Your KG")
label2 = tk.Label(fg="black", text="Enter Your Height (cm)")

# label3 = tk.Label(fg="black", text="result")

firstEntry = tk.Entry(fg="black")
secondEntry = tk.Entry(fg="black")

calc_button = tk.Button(text="Calculate", fg="black")



label1.place(relx=0.5, rely=0.18, anchor="center")

firstEntry.place(relx=0.5, rely=0.27, anchor="center")

label2.place(relx=0.5, rely=0.36, anchor="center")

secondEntry.place(relx=0.5, rely=0.45, anchor="center")

calc_button.place(relx=0.5, rely=0.56, anchor="center",)

def calculate():
    try:
        kg = int(firstEntry.get())
        height = int(secondEntry.get())
        result = kg / (height/100 * height/100)

        status = ""
        if result < 18.5:
            status = "You are underweight"

        elif result > 18.5 and result <= 25:
            status = "You are normal"
        elif result > 25 and result <= 29.9:
            status = "You are overweight"
        elif result > 29.9 and result <= 34.9:
            status = "You are medically obese"
        elif result > 34.9 and result <= 39.9:
            status = "You are medically obese"
        elif result > 39.9:
            status = "You are extreme obese"

        label3 = tk.Label(fg="black",wraplength=200,text=f"Your BMI is: {round(result, 2)}. {status}")
        label3.place(relx=0.5,rely=0.70, anchor="center")

    except:
        label3 = tk.Label(fg="black", text="Please enter only your weight and height.")
        label3.place(relx=0.5, rely=0.70, anchor="center")

calc_button.config(command=calculate)








window.mainloop()