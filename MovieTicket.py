from tkinter import *
from tkinter import ttk
import tkinter.messagebox

def notify(preview_pg):
    tkinter.messagebox.showinfo('Notification', "Ticket Booked Successfully")
    preview_pg.destroy()

def preview(seat_pg, user_name, dropvar1, dropvar2, seat_name, price):
    if not seat_name:
        tkinter.messagebox.showerror("No Seats Selected", "Please select at least one seat.")
        return

    seat_pg.destroy()
    preview_pg = Tk()
    preview_pg.title("Preview and Confirm")
    window_width = preview_pg.winfo_screenwidth()
    window_height = preview_pg.winfo_screenheight()
    preview_pg.geometry(f'{window_width}x{window_height}')

    bg_frame = Frame(preview_pg, bg="darkgray")
    bg_frame.pack(fill=BOTH, expand=True)

    f1 = Frame(bg_frame, bg="lightblue", borderwidth=5, relief=SUNKEN)
    f1.pack(side=TOP, fill="x")
    Label(f1, text="BookMyTicket", bg="lightblue", fg="black").pack()

    Label(bg_frame, text="Booking Details", bg="darkgray").place(x=725, y=100)
    Label(bg_frame, text="Name: " + user_name.get(), bg="darkgray").place(x=700, y=150)
    Label(bg_frame, text="Movie Name: " + dropvar1.get(), bg="darkgray").place(x=700, y=200)
    Label(bg_frame, text="Show Time: " + dropvar2.get(), bg="darkgray").place(x=700, y=250)
    Label(bg_frame, text="Selected Seat(s): " + seat_name, bg="darkgray").place(x=700, y=300)
    Label(bg_frame, text="Price: " + str(price), bg="darkgray").place(x=700, y=350)
    Button(bg_frame, text="Confirm Booking", command=lambda: notify(preview_pg)).place(x=725, y=450)
    preview_pg.mainloop()

def choice(seat_vars):
    seat_name = ""
    price = 0
    for idx, seat_var in enumerate(seat_vars):
        if seat_var.get() == 1:
            row = chr(65 + idx // 10)  # Convert index to letter (A, B, C, ...)
            col = idx % 10 + 1  # Column number (1, 2, 3, ...)
            seat_name += f"{row}{col} "
            price += 150 if row in 'ABC' else 200
    return seat_name, price

def seats(select_pg, user_name, dropvar1, dropvar2):
    select_pg.destroy()
    seat_pg = Tk()
    seat_pg.title("Choose seat(s)")
    window_width = seat_pg.winfo_screenwidth()
    window_height = seat_pg.winfo_screenheight()
    seat_pg.geometry(f'{window_width}x{window_height}')

    bg_frame = Frame(seat_pg, bg="darkgray")
    bg_frame.pack(fill=BOTH, expand=True)

    f1 = Frame(bg_frame, bg="lightblue", borderwidth=5, relief=SUNKEN)
    f1.pack(side=TOP, fill="x")
    Label(f1, text="BookMyTicket", bg="lightblue", fg="black").pack()

    seat_vars = [IntVar() for _ in range(50)]
    seat_labels = ["A", "B", "C", "D", "E"]
    seat_prices = [150, 150, 150, 200, 200]

    Label(bg_frame, text="                                                               SCREEN                                                            ", bg="black", fg="white").place(x=525, y=125)

    for i, label in enumerate(seat_labels):
        Label(bg_frame, text=label, bg="darkgray").place(x=475, y=200 + i * 50)
        for j in range(10):
            Checkbutton(bg_frame, text=f"{label}{j+1}", variable=seat_vars[i * 10 + j], onvalue=1, offvalue=0, bg="darkgray").place(x=500 + j * 50, y=200 + i * 50)
        Label(bg_frame, text=f"Rs. {seat_prices[i]}", bg="darkgray").place(x=1000, y=200 + i * 50)

    Button(bg_frame, text="OK", command=lambda: preview(seat_pg, user_name, dropvar1, dropvar2, choice(seat_vars)[0], choice(seat_vars)[1])).place(x=700, y=500)
    seat_pg.mainloop()

def movie_time(login_pg, user_name, dropvar1, dropvar2):

    def on_selectseat():
        if dropvar1.get() == '---Select Movie---' or dropvar2.get() == '---Select Time---':
            tkinter.messagebox.showerror("Incomplete Selection", "Please select both a movie and a show time.")
            return
        seats(select_pg, user_name, dropvar1, dropvar2)

    login_pg.destroy()
    select_pg = Tk()
    select_pg.title("Choose movie and time")
    window_width = select_pg.winfo_screenwidth()
    window_height = select_pg.winfo_screenheight()
    select_pg.geometry(f'{window_width}x{window_height}')

    bg_frame = Frame(select_pg, bg="darkgray")
    bg_frame.pack(fill=BOTH, expand=True)

    def getvalues(selected):
        dm2.set_menu(*option2.get(selected))

    f1 = Frame(bg_frame, bg="lightblue", borderwidth=5, relief=SUNKEN)
    f1.pack(side=TOP, fill="x")
    Label(f1, text="BookMyTicket", bg="lightblue", fg="black").pack()

    Label(bg_frame, text="Movie Name", bg="darkgray").place(x=650, y=200)
    dropvar1=StringVar()
    option1 = ["Avengers", "Black Widow", "Spiderman", "Hulk"]
    dm1 = ttk.OptionMenu(bg_frame, dropvar1, '---Select Movie---', *option1, command=getvalues)
    dm1.place(x=750, y=200)

    Label(bg_frame, text="Show time", bg="darkgray").place(x=650, y=300)
    option2 = {
        'Avengers': ["---Select Time---", "10.00AM - 13.00PM", "14.00PM - 17.00PM", "18.00PM - 21.00PM", "22.00PM - 01.00AM"],
        'Black Widow': ["---Select Time---", "10.00AM - 13.00PM", "18.00PM - 21.00PM", "22.00PM - 01.00AM"],
        'Spiderman': ["---Select Time---", "14.00PM - 17.00PM", "18.00PM - 21.00PM", "22.00PM - 01.00AM"],
        'Hulk': ["---Select Time---", "10.00AM - 13.00PM", "18.00PM - 21.00PM", "22.00PM - 01.00AM"]
    }
    dropvar2=StringVar()
    dm2 = ttk.OptionMenu(bg_frame, dropvar2, '---Select Time---')
    dm2.place(x=750, y=300)

    Button(bg_frame, text="Select seat(s)", command=on_selectseat).place(x=750, y=400)
    select_pg.mainloop()

def on_login(login_pg, user_name, mobile_num, dropvar1, dropvar2):
    username = user_name.get()
    mobilenumber = mobile_num.get()

    if not username:
        tkinter.messagebox.showerror("Missing Username", "Please enter your username.")
        return

    if not mobilenumber:
        tkinter.messagebox.showerror("Missing Mobile Number", "Please enter your mobile number.")
        return

    if not username.isalpha():
        tkinter.messagebox.showerror("Invalid Username", "Username should contain only alphabetic characters.")
        return

    if not (mobilenumber.isdigit() and len(mobilenumber) == 10):
        tkinter.messagebox.showerror("Invalid Mobile Number", "Mobile number should be exactly 10 digits.")
        return

    movie_time(login_pg, user_name, dropvar1, dropvar2)

login_pg = Tk()
login_pg.title("Login")
window_width = login_pg.winfo_screenwidth()
window_height = login_pg.winfo_screenheight()
login_pg.geometry(f'{window_width}x{window_height}')

bg_frame = Frame(login_pg, bg="darkgray", relief=SUNKEN)
bg_frame.pack(fill=BOTH, expand=True)

f1 = Frame(bg_frame, bg="lightblue", borderwidth=5, relief=SUNKEN)
f1.pack(side=TOP, fill="x")
Label(f1, text="BookMyTicket", bg="lightblue", fg="black").pack()

user_name = StringVar()
mobile_num = StringVar()
dropvar1 = StringVar()
dropvar2 = StringVar()

Label(bg_frame, text="Username", bg="darkgrey").place(x=650, y=200)
Entry(bg_frame, textvariable=user_name).place(x=750, y=200)
Label(bg_frame, text="Mobile Number", bg="darkgrey").place(x=650, y=300)
Entry(bg_frame, textvariable=mobile_num).place(x=750, y=300)
Button(bg_frame, text="Login", command=lambda: on_login(login_pg, user_name, mobile_num, dropvar1, dropvar2)).place(x=750, y=400)
login_pg.mainloop()