from multiprocessing.sharedctypes import Value
from tkinter import *
import tkinter.messagebox
from HashTable import *
import matplotlib.pyplot as plt
from datetime import *

invoice_dictionary=HashTable()

def generate_invoice():
    if len(invoice_dictionary.items())==0:
        tkinter.messagebox.showwarning("Invoice","No medicines are added to bill")
        return
    with open(r"Invoice.txt","w") as file:
        file.write("\n"+" "*14)
        file.write("SRI SARAVANA PHARMACY\n")
        file.write(" "*8+"Mugalivakkam, Chennai, Tamil Nadu")
        file.write("\n"+" "*14+"CONTACT:044 2252 3525")
        file.write("\n"+"_"*50+"\n")
        file.write("\nDate - "+ str(date.today().strftime("%d/%m/%Y"))+" "*19+"Time - "+str(datetime.now().strftime("%H:%M:%S")))
        file.write("\n"+"_"*50+"\n")
        file.write("   {:<20} {:<10}   {:<10}".format("Medicine Name", "Quantity","Price"))
        file.write("\n"+"-"*50+"\n")
        medCount=0
        medPrice=0
        for key, value in invoice_dictionary.items():
            medCount+=value
            medPrice+=med_dict[key][2]*value
            string="   {:<20} {:<10}   Rs.{:<10}".format(key.capitalize(),value,med_dict[key][2]*value)
            file.write(string+"\n")
        file.write("-"*50+"\n")
        file.write("   {:<20} {:<10}   Rs.{:<10}".format("TOTAL",medCount,medPrice))
        file.write("\n"+"_"*50+"\n")
        file.write(" "*15+"Thanks for visiting!"+"\n")
        file.write("="*50)
    tkinter.messagebox.showinfo("Invoice","Invoice Generated")

def reports():
    #when reports button is clicked a new window named inventory opens with its toplevel as dashboard(window)
    if(len(invoice_dictionary.items())==0):
        tkinter.messagebox.showwarning("Reports","No statistics available")     
    else:
        window_reports = Toplevel(window)
        
        window_reports.title("Reports")
        window_reports.geometry("1280x720")
        window_reports.configure(bg = "#ffffff")
        canvas = Canvas(window_reports,bg = "#ffffff",height = 720,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"backgroundreports.png")
        background = canvas.create_image(640.5, 360.0,image=background_img)
        graph1 = PhotoImage(file = f"piechart.png")
        graphlabel = Label(window_reports, image = graph1)
        graphlabel.place(x=300,y=217)

        window_reports.resizable(False, False)
        window_reports.mainloop()

def medicine_shortage():
    #when medicine_shortage button is clicked a new window named inventory opens with its toplevel as dashboard(window)
    window_medicine_shortage = Toplevel(window)
    window_medicine_shortage.title("Invoice")
    window_medicine_shortage.geometry("1280x720")
    window_medicine_shortage.configure(bg = "#ffffff")
    canvas = Canvas(window_medicine_shortage,bg = "#ffffff",height = 720,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)
    background_img = PhotoImage(file = f"backgroundalerts.png")
    background = canvas.create_image(640.5, 360.0,image=background_img)
    
    y_cord=267
    for i in med_dict.keys():
        if med_dict[i][1]<5:
            strtxt="{:<20}".format(i.capitalize())
            medq="{:<20}".format(med_dict[i][1])
            medice_label=Label(window_medicine_shortage,text=strtxt,bg="#D0FF6B",fg="black",font=("Bahnschrift Light", 10))
            medq_label=Label(window_medicine_shortage,text=medq,bg="#D0FF6B",fg="black",font=("Bahnschrift Light", 10))

            medice_label.place(x=297,y=y_cord,width = 216,height = 36)
            medq_label.place(x=513,y=y_cord,width = 216,height = 36)
            y_cord+=36
    y_cord=267
    todays_date=str(date.today().strftime("%d/%m/%Y")).split("/")
   
    for i in med_dict.keys():
        med_txt="{:^50}".format(i.capitalize())
        med_date=med_dict[i][3].split("/")
        if int(todays_date[2])>int(med_date[2]):
            medice_label=Label(window_medicine_shortage,text=med_txt,bg="#FF8585",fg="black",font=("Bahnschrift Light", 10))
            medice_label.place(x=775,y=y_cord,width = 432,height = 36)
            y_cord+=36
        elif  int(todays_date[2])>=int(med_date[2]) and  int(todays_date[1])>int(med_date[1]):
            medice_label=Label(window_medicine_shortage,text=med_txt,bg="#FF8585",fg="black",font=("Bahnschrift Light", 10))
            medice_label.place(x=775,y=y_cord,width = 432,height = 36)
            y_cord+=36
        elif   int(todays_date[2])>=int(med_date[2]) and  int(todays_date[1])>=int(med_date[1]) and int(todays_date[0])>int(med_date[0]):
            medice_label=Label(window_medicine_shortage,text=med_txt  ,bg="#FF8585",fg="black",font=("Bahnschrift Light", 10))
            medice_label.place(x=775,y=y_cord,width = 432,height = 36)
            y_cord+=36
    window_medicine_shortage.resizable(False, False)
    window_medicine_shortage.mainloop()

def inventory():
    #when inventory button is clicked a new window named inventory opens with its toplevel as dashboard(window)
    window_inv = Toplevel(window)
    window_inv.title("Inventory")
    window_inv.geometry("1280x720")
    window_inv.configure(bg = "#ffffff")
    canvas = Canvas(window_inv,bg = "#ffffff",height = 720,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"backgroundinv.png")
    background = canvas.create_image(640.5, 360.0,image=background_img)

    bin_label=Label(window_inv,text="Search for medicines to get the bin number of the required medicine",font=("Bahnschrift Light", 10))
    bin_label.place(x=360,y=505,width = 474,height = 45)
    
    def med_available():
        string=e_med.get().capitalize().strip()+" available"+"\n"+"Quantity : "+str(med_dict[e_med.get().lower().strip()][1])

        available_label=Label(window_inv,text=string,font=("Bahnschrift Light", 10))
        available_label.place(x=877,y=236,width = 256,height = 92)

    
    def absence_med():
        #label indicating the absence of medicine
        string="Sorry "+e_med.get().capitalize().strip()+" is not available"
        if len(e_med.get().strip())==0:
            string="No medicine is entered. Try again"
        absence_label=Label(window_inv,text=string,font=("Bahnschrift Light", 10))
        absence_label.place(x=877,y=236,width = 256,height = 92)
    def absence_quan():
        #label indicating the absence of medicine
        absence_label=Label(window_inv,text="Sorry the asked quantity is not available",font=("Bahnschrift Light", 10))
        absence_label.place(x=877,y=236,width = 256,height = 92)
    def expired_med():
        string="Sorry "+e_med.get().capitalize().strip()+" is expired"
        absence_label=Label(window_inv,text=string,font=("Bahnschrift Light", 10))
        absence_label.place(x=877,y=236,width = 256,height = 92)
        
    def ok_med():
        #ok med first checks if the medicine is present    
        def ok_quan():
            if str(e_med.get().strip())=="":
                string="No medicine is entered. Try again"
                err_label=Label(window_inv,text=string,font=("Bahnschrift Light", 10))
                err_label.place(x=877,y=236,width = 256,height = 92)

            else:
            
            
            
                #checking the expiry condition here because user could enter a expired medicine after entering a available medicine
                todays_date=str(date.today().strftime("%d/%m/%Y")).split("/")
                med_date=med_dict[e_med.get().lower().strip()][3].split("/")
                if int(todays_date[2])>int(med_date[2]):
                    expired_med()
                elif int(todays_date[2])>=int(med_date[2]) and  int(todays_date[1])>int(med_date[1]):
                    expired_med()
                elif int(todays_date[2])>=int(med_date[2]) and  int(todays_date[1])>=int(med_date[1]) and int(todays_date[0])>int(med_date[0]):
                    expired_med()
                else:
                    try:
                        int(e_quan.get())
                    except ValueError:
                        err_label=Label(window_inv,text="Invalid entry. Try again",font=("Bahnschrift Light", 10))
                        err_label.place(x=877,y=236,width = 256,height = 92)
                    if int(e_quan.get())<=0:
                        err_label=Label(window_inv,text="Invalid entry. Try again",font=("Bahnschrift Light", 10))
                        err_label.place(x=877,y=236,width = 256,height = 92)
                    elif int(e_quan.get())>med_dict[e_med.get().lower().strip()][1]:
                        absence_quan()
                    else:
                        bin_label=Label(window_inv,text=e_med.get().capitalize().strip()+" "*70+str(med_dict[e_med.get().lower().strip()][0])+" "*20,font=("Bahnschrift Light", 10))
                        bin_label.place(x=360,y=505,width = 474,height = 45)

                        before_label=Label(window_inv,text="Available "+e_med.get().capitalize().strip()+" before purchase = "+str(med_dict[e_med.get().lower().strip()][1]),font=("Bahnschrift Light", 10))
                        before_label.place(x=877,y=236,width = 256,height = 46)
                        med_dict[e_med.get().lower().strip()][1]-=int(e_quan.get())

                        #invoice related code
                        if e_med.get().lower().strip() in invoice_dictionary.keys():
                            invoice_dictionary[e_med.get().lower().strip()]+=int(e_quan.get())
                        else:
                            invoice_dictionary[e_med.get().lower().strip()]=int(e_quan.get())

                        # creating the dataset
                        courses = [string.capitalize() for string in invoice_dictionary.keys()]
                        values = list(invoice_dictionary.values())

                        fig = plt.figure(figsize = (8, 4))

                        # creating the bar plot

                        plt.pie(values, labels = courses)
                        
                        plt.title("Statistics")
                        plt.savefig('piechart.png')

                        afterhh_label=Label(window_inv,text="Available "+e_med.get().capitalize().strip()+" after purchase = "+str(med_dict[e_med.get().lower().strip()][1]),font=("Bahnschrift Light", 10))
                        afterhh_label.place(x=877,y=282,width = 256,height = 46) 
                        e_med.delete(0,END)
                        e_quan.delete(0,END)

     
        
        #if the name enter by the user exsists then we enquire about the quantity
        if  e_med.get().strip()=="":
                string="No medicine is entered. Try again"
                err_label=Label(window_inv,text=string,font=("Bahnschrift Light", 10))
                err_label.place(x=877,y=236,width = 256,height = 92)

        
        elif (e_med.get().lower().strip() in med_dict.keys()):

            todays_date=str(date.today().strftime("%d/%m/%Y")).split("/")
            med_date=med_dict[e_med.get().lower().strip()][3].split("/")
            if int(todays_date[2])>int(med_date[2]):
                expired_med()
            elif int(todays_date[2])>=int(med_date[2]) and  int(todays_date[1])>int(med_date[1]):
                expired_med()
            elif int(todays_date[2])>=int(med_date[2]) and  int(todays_date[1])>=int(med_date[1]) and int(todays_date[0])>int(med_date[0]):
                expired_med()
            else:
                med_available()
                #entry box to get the quantity
                e_quan=Entry(window_inv,bg="white",fg="black")
                e_quan.place(x=360,y=351,width = 360,height = 49)
                #once the user clicks ok after typing the quantity of the med,ok_quan function is called
                ok_quan_but=Button(window_inv,image=ok_img,text="OK",command=ok_quan)
                ok_quan_but.place(x=744,y=354,width = 90,height = 46)
        else:
            #we call absence is the med is not present
            absence_med()
  

    #entry box to get the medicine
    e_med=Entry(window_inv,bg="white",fg="black")
    e_med.place(x=360,y=231,width = 360,height = 49)

    #once the user clicks ok after typing the name of the med,ok_med function is called
    ok_img=PhotoImage(file=f"imgOk.png")
    ok_med_but=Button(window_inv,text="OK",command=ok_med,image=ok_img)
    ok_med_but.place(x=744,y=235,width = 90,height = 46)

    window_inv.resizable(False, False)
    window_inv.mainloop()
########################code for dashboard#######################################################################

window = Tk()
window.title("Pharmacy Management System")
window.geometry("1280x720")
window.configure(bg = "#03a9f5")
canvas = Canvas(window,bg = "#03a9f5",height = 720,width = 1280,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"backgrounddashboard.png")
background = canvas.create_image(641.0, 360.5,image=background_img)


#the one which says inventory on the left
img1 = PhotoImage(file = f"img1.png")
b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = inventory,relief = "flat")
b1.place(x = 0, y = 133,width = 256,height = 46)

#the one which says reports on the left
img2 = PhotoImage(file = f"img2.png")
b2 = Button(image = img2,borderwidth = 0,highlightthickness = 0,command = reports,relief = "flat")
b2.place(x = 0, y = 179,width = 256,height = 46)

#the one which says generate invoice on the left
img3 = PhotoImage(file = f"img3.png")
b3 = Button(image = img3,borderwidth = 0,highlightthickness = 0,command = generate_invoice,relief = "flat")
b3.place(x = 0, y = 225,width = 256,height = 46)



img4= PhotoImage(file = f"img4.png")
b4 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = medicine_shortage,relief = "flat")
b4.place(x = 0, y = 271,width = 256,height = 46)

#the one which says invoice in the middle
img5 = PhotoImage(file = f"img4dashboard.png")
b5 = Button(image = img5,borderwidth = 0,highlightthickness = 0,command = generate_invoice,relief = "flat")
b5.place(x = 370, y = 200,width = 284,height = 152)

#the one which says inventory in the middle
img6 = PhotoImage(file = f"img5dashboard.png")
b6 = Button(image = img6,borderwidth = 0,highlightthickness = 0,command = inventory,relief = "flat")
b6.place(x = 840, y = 200,width = 284,height = 152)

no_of_med_label=Label(window,text=str(len(med_dict.items())),bg="white",font=("Verdana", 11))
no_of_med_label.place(x=970,y=267,width=20,height=20)

#the one which says medicine shortage in the middle
img7 = PhotoImage(file = f"img6dashboard.png")
b7 = Button(image = img7,borderwidth = 0,highlightthickness = 0,command = medicine_shortage,relief = "flat")
b7.place(x = 840, y = 464,width = 284,height = 152)

#the one which says reports in the middle
img8 = PhotoImage(file = f"img7dashboard.png")
b8 = Button(image = img8,borderwidth = 0,highlightthickness = 0,command = reports,relief = "flat")
b8.place(x = 370, y = 464,width = 284,height = 152)

window.resizable(False, False)
window.mainloop()