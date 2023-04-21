import tkinter
import pandas as pd
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import shutil
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

path=os.getcwd()
file_name ="IndianFoodDataset.xlsx"
file_path = os.path.join(path,file_name)

recipe = pd.read_excel(file_path)

window = tkinter.Tk()
window.attributes("-fullscreen", True)
window.title("RECIPES")
frame_top = tkinter.Frame(window, width=500, height=400)
frame_top.grid(row=0, column=0)

frame_bottom = tkinter.Frame(window, width=1200, height=225)
frame_bottom.grid(row=1, column=0, padx=25)

name = Label(frame_top, font=('comicsansms', 12, 'bold'), text = "RECIPE SUGGESTION (^_^)", fg="dark green")
name.grid(row=0, column=3)

diet_label = Label(frame_top,text="Diet")
diet_label.grid(row=1, column=1)

prep_time_label = Label(frame_top,text="Prep Time Min")
prep_time_label.grid(row=1, column=3)

course_label = Label(frame_top,text="Course")
course_label.grid(row=2, column=1)

cook_time_label = Label(frame_top,text="Cook Time Min")
cook_time_label.grid(row=2, column=3)

cuisine_label = Label(frame_top,text="Cuisine")
cuisine_label.grid(row=3, column=1)

total_time_label = Label(frame_top,text="Total Time Min")
total_time_label.grid(row=3, column=3)

recipe_name_label = Label(frame_top,text="Recipe Name")
recipe_name_label.grid(row=4, column=1)

serving_label = Label(frame_top,text="Serving Time Min")
serving_label.grid(row=4, column=3)

ingredient_label = Label(frame_top,text="Ingredients")
ingredient_label.grid(row=5, column=1)

instruction_label = Label(frame_top,text="Instructions")
instruction_label.grid(row=5, column=3)

ingredient_box = Text(frame_top,height=12, width=60, wrap=WORD)
ingredient_box.grid(row=6, column=2)
ingredient_box.insert(END, "")
ingredient_box.config(state=tkinter.DISABLED)

instruction_box = Text(frame_top,height=12, width=60, wrap=WORD)
instruction_box.grid(row=6, column=4)
instruction_box.insert(END, "")
instruction_box.config(state=tkinter.DISABLED)

prep_time = Text(frame_top,height=1, width=10, wrap=WORD)
prep_time.grid(row=1, column=4)
prep_time.insert(END, "")
prep_time.config(state=tkinter.DISABLED)

cook_time = Text(frame_top,height=1, width=10, wrap=WORD)
cook_time.grid(row=2, column=4)
cook_time.insert(END, "")
cook_time.config(state=tkinter.DISABLED)

total_time = Text(frame_top,height=1, width=10, wrap=WORD)
total_time.grid(row=3, column=4)
total_time.insert(END, "")
total_time.config(state=tkinter.DISABLED)

serving_time = Text(frame_top,height=1, width=10, wrap=WORD)
serving_time.grid(row=4, column=4)
serving_time.insert(END, "")
serving_time.config(state=tkinter.DISABLED)

image = Image.open("family.png")
image = image.resize((300,300))
my = ImageTk.PhotoImage(image)
C = tkinter.Label(frame_bottom, image=my)
C.pack()

diet = [""]
for i in recipe["Diet"].unique():
    diet.append(i)

diet_drop =ttk.Combobox(frame_top, values=diet, width=40)
diet_drop.grid(row=1, column=2)


def course_fn(e):
    course_drop.set("")
    cuisine_drop.set("")
    recipe_name_drop.set("")
    diet_value = diet_drop.get()
    course = [""]
    for j in recipe[recipe["Diet"] == diet_value]["Course"].unique():
        course.append(j)
    course_drop.config(values=course)

    prep_time.config(state=tkinter.NORMAL)
    prep_time.delete(0.0, END)
    prep_time.config(state=tkinter.DISABLED)

    cook_time.config(state=tkinter.NORMAL)
    cook_time.delete(0.0, END)
    cook_time.config(state=tkinter.DISABLED)

    total_time.config(state=tkinter.NORMAL)
    total_time.delete(0.0, END)
    total_time.config(state=tkinter.DISABLED)

    serving_time.config(state=tkinter.NORMAL)
    serving_time.delete(0.0, END)
    serving_time.config(state=tkinter.DISABLED)

    ingredient_box.config(state=tkinter.NORMAL)
    ingredient_box.delete(0.0, END)
    ingredient_box.config(state=tkinter.DISABLED)

    instruction_box.config(state=tkinter.NORMAL)
    instruction_box.delete(0.0, END)
    instruction_box.config(state=tkinter.DISABLED)

    new_image = Image.open("family.png")
    new_image = new_image.resize((300, 300))
    by = ImageTk.PhotoImage(new_image)
    C.config(image=by)
    C.my = by

diet_drop.bind("<<ComboboxSelected>>", course_fn)
course_drop = ttk.Combobox(frame_top, values=[""], width=40)
course_drop.grid(row=2, column=2)

def cuisine_fn(e):
    cuisine_drop.set("")
    recipe_name_drop.set("")
    diet_value = diet_drop.get()
    course_value = course_drop.get()
    cuisine = [""]
    for k in recipe[(recipe["Diet"]==diet_value) & (recipe["Course"]== course_value)]["Cuisine"].unique():
        cuisine.append(k)
    cuisine_drop.config(values=cuisine)

    prep_time.config(state=tkinter.NORMAL)
    prep_time.delete(0.0, END)
    prep_time.config(state=tkinter.DISABLED)

    cook_time.config(state=tkinter.NORMAL)
    cook_time.delete(0.0, END)
    cook_time.config(state=tkinter.DISABLED)

    total_time.config(state=tkinter.NORMAL)
    total_time.delete(0.0, END)
    total_time.config(state=tkinter.DISABLED)

    serving_time.config(state=tkinter.NORMAL)
    serving_time.delete(0.0, END)
    serving_time.config(state=tkinter.DISABLED)

    ingredient_box.config(state=tkinter.NORMAL)
    ingredient_box.delete(0.0, END)
    ingredient_box.config(state=tkinter.DISABLED)

    instruction_box.config(state=tkinter.NORMAL)
    instruction_box.delete(0.0, END)
    instruction_box.config(state=tkinter.DISABLED)

    new_image = Image.open("family.png")
    new_image = new_image.resize((300, 300))
    by = ImageTk.PhotoImage(new_image)
    C.config(image=by)
    C.my = by

course_drop.bind("<<ComboboxSelected>>", cuisine_fn)
cuisine_drop = ttk.Combobox(frame_top, values=[""], width=40)
cuisine_drop.grid(row=3, column=2)

def recipe_name_fn(e):
    recipe_name_drop.set("")
    diet_value = diet_drop.get()
    course_value = course_drop.get()
    cuisine_value = cuisine_drop.get()
    recipe_name = [""]
    for l in recipe[(recipe["Diet"] == diet_value) & (recipe["Course"] == course_value) & (recipe["Cuisine"]== cuisine_value)]["TranslatedRecipeName"].unique():
        recipe_name.append(l)
    recipe_name_drop.config(values=recipe_name)

    prep_time.config(state=tkinter.NORMAL)
    prep_time.delete(0.0, END)
    prep_time.config(state=tkinter.DISABLED)

    cook_time.config(state=tkinter.NORMAL)
    cook_time.delete(0.0, END)
    cook_time.config(state=tkinter.DISABLED)

    total_time.config(state=tkinter.NORMAL)
    total_time.delete(0.0, END)
    total_time.config(state=tkinter.DISABLED)

    serving_time.config(state=tkinter.NORMAL)
    serving_time.delete(0.0, END)
    serving_time.config(state=tkinter.DISABLED)

    ingredient_box.config(state=tkinter.NORMAL)
    ingredient_box.delete(0.0, END)
    ingredient_box.config(state=tkinter.DISABLED)

    instruction_box.config(state=tkinter.NORMAL)
    instruction_box.delete(0.0, END)
    instruction_box.config(state=tkinter.DISABLED)

    new_image = Image.open("family.png")
    new_image = new_image.resize((300, 300))
    by = ImageTk.PhotoImage(new_image)
    C.config(image=by)
    C.my = by

cuisine_drop.bind("<<ComboboxSelected>>", recipe_name_fn)
recipe_name_drop = ttk.Combobox(frame_top, values=[""], width=40)
recipe_name_drop.grid(row=4, column=2)

def clear(e):
    prep_time.config(state=tkinter.NORMAL)
    prep_time.delete(0.0, END)
    prep_time.config(state=tkinter.DISABLED)

    cook_time.config(state=tkinter.NORMAL)
    cook_time.delete(0.0, END)
    cook_time.config(state=tkinter.DISABLED)

    total_time.config(state=tkinter.NORMAL)
    total_time.delete(0.0, END)
    total_time.config(state=tkinter.DISABLED)

    serving_time.config(state=tkinter.NORMAL)
    serving_time.delete(0.0, END)
    serving_time.config(state=tkinter.DISABLED)

    ingredient_box.config(state=tkinter.NORMAL)
    ingredient_box.delete(0.0, END)
    ingredient_box.config(state=tkinter.DISABLED)

    instruction_box.config(state=tkinter.NORMAL)
    instruction_box.delete(0.0, END)
    instruction_box.config(state=tkinter.DISABLED)

    new_image = Image.open("family.png")
    new_image = new_image.resize((300, 300))
    by = ImageTk.PhotoImage(new_image)
    C.config(image=by)
    C.my = by

recipe_name_drop.bind("<<ComboboxSelected>>", clear)

def recipe_menu():
    diet_value = diet_drop.get()
    course_value = course_drop.get()
    cuisine_value = cuisine_drop.get()
    recipe_name_value = recipe_name_drop.get()
    if (diet_value=="" or course_value=="" or cuisine_value=="" or recipe_name_value==""):
        messagebox.showerror("Error", "Select all the field")
    else:
        prep_time_value = recipe[(recipe["Diet"]==diet_value) & (recipe["Course"]==course_value) & (recipe["Cuisine"]==cuisine_value) & (recipe["TranslatedRecipeName"]==recipe_name_value)]["PrepTimeInMins"].values
        prep_time.config(state=tkinter.NORMAL)
        prep_time.delete(0.0, END)
        prep_time.insert(END, prep_time_value[0])
        prep_time.config(state=tkinter.DISABLED)

        cook_time_value = recipe[(recipe["Diet"] == diet_value) & (recipe["Course"] == course_value) & (recipe["Cuisine"] == cuisine_value) & (recipe["TranslatedRecipeName"] == recipe_name_value)]["CookTimeInMins"].values
        cook_time.config(state=tkinter.NORMAL)
        cook_time.delete(0.0, END)
        cook_time.insert(END, cook_time_value[0])
        cook_time.config(state=tkinter.DISABLED)

        total_time_value = recipe[(recipe["Diet"] == diet_value) & (recipe["Course"] == course_value) & (recipe["Cuisine"] == cuisine_value) & (recipe["TranslatedRecipeName"] == recipe_name_value)]["TotalTimeInMins"].values
        total_time.config(state=tkinter.NORMAL)
        total_time.delete(0.0, END)
        total_time.insert(END, total_time_value[0])
        total_time.config(state=tkinter.DISABLED)

        serving_time_value = recipe[(recipe["Diet"] == diet_value) & (recipe["Course"] == course_value) & (recipe["Cuisine"] == cuisine_value) & (recipe["TranslatedRecipeName"] == recipe_name_value)]["Servings"].values
        serving_time.config(state=tkinter.NORMAL)
        serving_time.delete(0.0, END)
        serving_time.insert(END, serving_time_value[0])
        serving_time.config(state=tkinter.DISABLED)

        ingredient_value = recipe[(recipe["Diet"] == diet_value) & (recipe["Course"] == course_value) & (recipe["Cuisine"] == cuisine_value) & (recipe["TranslatedRecipeName"] == recipe_name_value)]["TranslatedIngredients"].values
        ingredient_box.config(state=tkinter.NORMAL)
        instruction_box.delete(0.0, END)
        ingredient_box.insert(END, ingredient_value[0])
        instruction_box.config(state=tkinter.DISABLED)

        instruction_value = recipe[(recipe["Diet"] == diet_value) & (recipe["Course"] == course_value) & (recipe["Cuisine"] == cuisine_value) & (recipe["TranslatedRecipeName"] == recipe_name_value)]["TranslatedInstructions"].values
        instruction_box.config(state=tkinter.NORMAL)
        instruction_box.delete(0.0, END)
        instruction_box.insert(END, instruction_value[0])
        instruction_box.config(state=tkinter.DISABLED)

        url = Service(ChromeDriverManager().install())
        option =Options()
        option.add_argument("--disable-notifications")
        option.add_argument("--headless")

        driver = webdriver.Chrome(service=url, chrome_options=option)

        link = recipe[(recipe["Diet"] == diet_value) & (recipe["Course"] == course_value) & (recipe["Cuisine"] == cuisine_value) & (recipe["TranslatedRecipeName"] == recipe_name_value)]["URL"].values[0]
        driver.get(link)
        driver.maximize_window()



        try:
            img = driver.find_element(By.CSS_SELECTOR, "#content-area > div > div:nth-child(3) > div > img")
            src = img.get_attribute("src")
            url = src
            response = requests.get(url, stream=True)
            with open("img.png", "wb") as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
            new_image = Image.open("img.png")
            new_image = new_image.resize((300, 300))
            by = ImageTk.PhotoImage(new_image)
            C.config(image=by)
            C.my = by
        except:
            try:
                title = driver.title
                a = "img[title="
                b = "'"
                c = title  # "Spicy Haryana Style Egg Curry Recipe"
                d = "']"
                e = a + b + c + d
                f = e.replace(" by Archana's Kitchen", "")
                img = driver.find_element(By.CSS_SELECTOR, f)
                src = img.get_attribute("src")
                url = src
                response = requests.get(url, stream=True)
                with open("img.png", "wb") as out_file:
                    shutil.copyfileobj(response.raw, out_file)
                del response
                new_image = Image.open("img.png")
                new_image = new_image.resize((300, 300))
                by = ImageTk.PhotoImage(new_image)
                C.config(image=by)
                C.my = by
            except:
                new_image = Image.open("family.png")
                new_image = new_image.resize((300, 300))
                by = ImageTk.PhotoImage(new_image)
                C.config(image=by)
                C.my = by


        driver.close()


generate_button = Button(frame_top, text="Generate", command=recipe_menu)
generate_button.grid(row=9, column=3)

Exit_button = Button(frame_top, text="Quit", command=window.destroy)
Exit_button.grid(row=10, column=3)



window.mainloop()