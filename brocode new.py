import tkinter as tk
import mysql.connector as mc
from tkinter import messagebox, PhotoImage, Label, Toplevel

# Create the GUI window
window = tk.Tk()
window.geometry("800x800")
window.config(background="#b6d0fc")
window.title("Namak Shamak")

# to add background image
bg = PhotoImage(file="E:\\final pro\\im.png")
label1 = Label(window, image=bg)
label1.place(x=0, y=0)

# Create the database connection
conn = mc.connect(host="localhost", user="root", password="S@hil123")
cur = conn.cursor(buffered=True)

# Create the table
try:
    cur.execute("CREATE DATABASE restaurants")
except:
    cur.execute("USE restaurants")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS data (name varchar(100), location varchar(50), cost int(4), rating decimal(2,1))")

# Insert the data into the database
def submit1():
    # Retrieves the values entered in the entry fields
    
    restaurant_name = name_entry.get().capitalize()
    restaurant_location = location_entry.get().capitalize()
    restaurant_cost = cost_entry.get()
    restaurant_rating = rating_entry.get()

    try:
        # Executes an INSERT statement to insert the entered data into the "data" table
        cur.execute(
            f"INSERT INTO data (name, location, cost, rating) VALUES ('{restaurant_name}', '{restaurant_location}', '{restaurant_cost}', '{restaurant_rating}')")
        conn.commit()
        # Displays a message box indicating successful data submission
        messagebox.showinfo("done", "Thank you for feedback")
    except mc.Error as error:
        # Displays an error message if there is a problem with the data submission
        messagebox.showerror("Incomplete Data","Please Enter correct and complete values ")


# Create the labels
name_label = tk.Label(text=" Restaurant Name ", font=('ARIEL', 15,"bold"), relief=('flat'),borderwidth=(1),fg="#00ff00",bg='black')
location_label = tk.Label(text=" Location ", font=('ARIEL', 15,"bold"), relief=('flat'),  borderwidth=(2),fg="#00ff00",bg='black')
cost_label = tk.Label(text=" Average Cost for 2 People ", font=('ARIEL', 15,"bold"), relief=('flat'), 
                       borderwidth=(2),fg="#00ff00",bg='black')
rating_label = tk.Label(text=" Rating ", font=('ARIEL', 15,"bold"), relief=('flat'),  borderwidth=(2),fg="#00ff00",bg='black')

# Create the Labels fields to the window
name_label.grid(row=1, column=0, padx=40, pady=40)
location_label.grid(row=2, column=0, padx=40, pady=40)
cost_label.grid(row=3, column=0, padx=40, pady=40)
rating_label.grid(row=4, column=0, padx=40, pady=40)

# Create the entry fields
name_entry = tk.Entry(font=('ARIEL', 14), relief=('ridge'), borderwidth=(2),fg="#00ff00",bg='black')
location_entry = tk.Entry(font=('ARIEL', 14), relief=('ridge'), borderwidth=(2),fg="#00ff00",bg='black')
cost_entry = tk.Entry(font=('ARIEL', 14), relief=('ridge'), borderwidth=(2),fg="#00ff00",bg='black')
rating_entry = tk.Entry(font=('ARIEL', 14), relief=('ridge'), borderwidth=(2),fg="#00ff00",bg='black')

# Add the entry fields to the window
name_entry.grid(row=1, column=1, padx=40, pady=40)
location_entry.grid(row=2, column=1, padx=40, pady=40)
cost_entry.grid(row=3, column=1, padx=40, pady=40)
rating_entry.grid(row=4, column=1, padx=40, pady=40)

# Create the buttons
submit_button = tk.Button(text="Submit", command=submit1, relief='raised', activebackground='grey', font=('ARIEL', 16,"bold"),fg="#00ff00",bg='black')
submit_button.grid(row=5, column=0, padx=30, pady=40)

# Create the buttons
submit_button = tk.Button(text="Submit", command=submit1, relief='raised', activebackground='grey',
                          font=('ARIEL', 16,"bold"), fg="#00ff00", bg='black')
submit_button.grid(row=5, column=0, padx=30, pady=40)

# Function to show all data
def show():
    cur.execute("SELECT name, location, ROUND(AVG(cost), 2), ROUND(AVG(rating), 2) FROM data GROUP BY name, location")
    results = cur.fetchall()

    # Create a new window to display the records
    show_window = Toplevel(window)
    show_window.geometry('600x600')
    show_window.title('All Entries')

    # Create labels for the columns
    name_label = tk.Label(show_window, text="Restaurant Name", font=('ARIEL', 15, "bold"), relief='flat')
    location_label = tk.Label(show_window, text="Location", font=('ARIEL', 15, "bold"), relief='flat')
    cost_label = tk.Label(show_window, text="Average Cost for 2 People", font=('ARIEL', 15, "bold"), relief='flat')
    rating_label = tk.Label(show_window, text="Rating", font=('ARIEL', 15, "bold"), relief='flat')

    # Grid the column labels
    name_label.grid(row=0, column=0, padx=10, pady=10)
    location_label.grid(row=0, column=1, padx=10, pady=10)
    cost_label.grid(row=0, column=2, padx=10, pady=10)
    rating_label.grid(row=0, column=3, padx=10, pady=10)

    # Loop through the records and display them
    row_num = 1
    for result in results:
        name = tk.Label(show_window, text=result[0], font=('ARIEL', 15), relief='flat')
        location = tk.Label(show_window, text=result[1], font=('ARIEL', 15), relief='flat')
        cost = tk.Label(show_window, text=result[2], font=('ARIEL', 15), relief='flat')
        rating = tk.Label(show_window, text=result[3], font=('ARIEL', 15), relief='flat')

        name.grid(row=row_num, column=0, padx=10, pady=10)
        location.grid(row=row_num, column=1, padx=10, pady=10)
        cost.grid(row=row_num, column=2, padx=10, pady=10)
        rating.grid(row=row_num, column=3, padx=10, pady=10)

        row_num += 1



# Create a new window to search for restaurants
def search_restaurants():
    search_window = Toplevel(window)
    search_window.geometry("450x450")
    search_window.title("Search Restaurants")
    search_window.config(bg='#1f84a3')

    # Create the labels
    name_label = tk.Label(search_window, text=" Restaurant Name ", font=('ARIEL', 15,"bold"), relief=('flat'), bg='pink',
                          borderwidth=(1))
    location_label = tk.Label(search_window, text=" Location ", font=('ARIEL', 15,"bold"), relief=('flat'), bg='pink',
                              borderwidth=(2))
    
    # Create the Labels fields to the window
    name_label.grid(row=1, column=0, padx=30, pady=20)
    location_label.grid(row=2, column=0, padx=30, pady=20)

    # Create the entry fields
    name_entry = tk.Entry(search_window, font=('ARIEL', 14,"bold"), relief=('ridge'), bg='sky blue', borderwidth=(2))
    location_entry = tk.Entry(search_window, font=('ARIEL', 14,"bold"), relief=('ridge'), bg='sky blue', borderwidth=(2))

    # Add the entry fields to the window
    name_entry.grid(row=1, column=1, padx=35, pady=20)
    location_entry.grid(row=2, column=1, padx=30, pady=20)

    # Create the search button
    search_button = tk.Button(search_window, text="Search", command=lambda: search(name_entry.get(), location_entry.get()),
                              relief='raised', activebackground='grey', font=('ARIEL', 13,'bold'))
    search_button.grid(row=3, column=0, padx=30, pady=20)
    # Function to search for restaurants based on name and location
    def search(name, location):
        if name and location:
            cur.execute(f"SELECT name, location, round(avg(cost),2), round(avg(rating),2) FROM data WHERE name LIKE '%{name}%' AND location LIKE '%{location}%' GROUP BY name, location")
        elif name:
            cur.execute(f"SELECT name, location, round(avg(cost),2), round(avg(rating),2) FROM data group by name,location having name LIKE '%{name}%'")
        elif location:
            cur.execute(f"SELECT name, location, round(avg(cost),2), round(avg(rating),2) FROM data group by name,location having location LIKE '%{location}%'")
        else:
            # Handle case where no parameters are provided
            return []

        results = cur.fetchall()
        
        
        # Create a new window to display the search results
        result_window = Toplevel(search_window)
        result_window.geometry("650x300")
        result_window.title("Search Results")
        result_window.config(bg='#dbdcff')

        # Create the labels for the search results
        name_label = tk.Label(result_window, text=" Restaurant Name ", font=('ARIEL', 15,"bold"), relief=('flat'), bg='white',
                              borderwidth=(1))
        location_label = tk.Label(result_window, text=" Location ", font=('ARIEL', 15,"bold"), relief=('flat'), bg='white',
                                  borderwidth=(2))
        cost_label = tk.Label(result_window, text=" Average Cost for 2 People ", font=('ARIEL', 15,"bold"), relief=('flat'),
                              bg='white', borderwidth=(2))
        rating_label = tk.Label(result_window, text=" Rating ", font=('ARIEL', 15,"bold"), relief=('flat'), bg='white',
                                 borderwidth=(2))

        # Create the Labels fields to the window
        name_label.grid(row=1, column=0, padx=40, pady=30)
        location_label.grid(row=1, column=1, padx=40, pady=30)
        cost_label.grid(row=1, column=2, padx=40, pady=30)
        rating_label.grid(row=1, column=3, padx=40, pady=30)

        # Add the search results to the window
        row_num = 2
        for result in results:
            name = tk.Label(result_window, text=result[0], font=('ARIEL', 15,"bold"), relief=('ridge'), bg='sky blue',
                            borderwidth=(2))
            location = tk.Label(result_window, text=result[1], font=('ARIEL', 15,"bold"), relief=('ridge'), bg='sky blue',
                                borderwidth=(2))
            cost = tk.Label(result_window, text=result[2], font=('ARIEL', 15,"bold"), relief=('ridge'), bg='sky blue',
                            borderwidth=(2))
            rating = tk.Label(result_window, text=result[3], font=('ARIEL', 15,"bold"), relief=('ridge'), bg='sky blue',
                              borderwidth=(2),)

            name.grid(row=row_num, column=0, padx=40, pady=30)
            location.grid(row=row_num, column=1, padx=40, pady=30)
            cost.grid(row=row_num, column=2, padx=40, pady=30)
            rating.grid(row=row_num, column=3, padx=40, pady=30)

            row_num += 1

    # Create the search button
    search_button = tk.Button(search_window, text="Search", command=lambda: search(name_entry.get(), location_entry.get()),
                              relief='raised', activebackground='grey', font=('ARIEL', 13,'bold'))
    search_button.grid(row=3, column=0, padx=30, pady=20)

    # Create the ShowAll button
    show_button = tk.Button(search_window, text="ShowAll", command=show, relief='raised', activebackground='grey',
                            font=('ARIEL', 16,"bold"), fg="#00ff00", bg='black')
    show_button.grid(row=5, column=1, padx=30, pady=40)


# Create Search Button 
search_button = tk.Button(text="Search", command=search_restaurants, relief='raised', activebackground='grey',
                           font=('ARIEL', 16,"bold"),fg="#00ff00",bg='black')
search_button.grid(row=5, column=1, padx=30, pady=40)


# Run the GUI
window.mainloop()