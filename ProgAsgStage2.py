###Athlete fitness & health calculator
## This program calculates athlete BMI and VO2 max and wraps it in a GUI
## Inputs: weight, maximum heart rate, minimum heart rate


import tkinter

class HealthCalculatorGUI:
    def calculate_BMI(self):
        # Calculate BMI using weight (in kg) and height (in cm)
        if self.player_entry.get() in self.dict1:
            height = float(self.dict1[self.player_entry.get()])
            weight = float(self.weight_entry.get())
            BMI = weight/ (height/100) ** 2
            self.BMI.set(f"{BMI:.2f}")

        else:
            self.BMI.set("Invalid player entry")

    def calculate_VO2(self):
        # Calculate VO2 max using max heart rate and resting heart rate
            MHR = float(self.MHR_entry.get())
            RHR = float(self.RHR_entry.get())
            if 120 <= MHR <= 200 and 45 <= RHR <= 85:
                VO2max = MHR/ RHR * 15.3 
                self.VO2.set(f"{VO2max:.2f}")
            else:
                self.VO2.set("Invalid heart rate entry")

    def reset_inputs(self):
        # Resets inputs to allow for different entries
        self.player_entry.delete(0, tkinter.END)
        self.weight_entry.delete(0, tkinter.END)
        self.BMI.set("")    
        self.MHR_entry.delete(0, tkinter.END)
        self.RHR_entry.delete(0, tkinter.END)
        self.VO2.set("")

      
    def __init__(self):
        # Initialize a dictionary with athlete positions and their corresponding heights
        self.dict1 = {
            "Point guard 1": "181",
            "Point guard 2": "183",
            "Shooting guard 1": "191",
            "Shooting guard 2": "193",
            "Small forward 1": "198",
            "Small forward 2": "190",
            "Power forward 1": "201",
            "Power forward 2": "203",
            "Centre 1": "213",
            "Centre 2": "212"
        }

        # Create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title ("Health and Fitness Calculator")

        self.main_window.configure(bg='lightblue')

        # Create labels, entry fields, and buttons
        self.title_label = tkinter.Label(self.main_window, text="Player options:")
        self.title_label.grid(row = 1, column = 0)
        
        self.listbox = tkinter.Listbox(self.main_window, height = 5)
        self.listbox.grid(row = 2, column = 0)

        self.scrollbar = tkinter.Scrollbar(self.main_window,command=self.listbox.yview)
        self.scrollbar.grid(row=2, column=1, sticky='ns') 
        
        self.player_label = tkinter.Label(self.main_window, text="Select a player from the list: ")
        self.player_label.grid(row = 0, column = 2)
        
        self.player_entry=tkinter.Entry(self.main_window, width = 15)
        self.player_entry.grid(row = 0, column = 3)
        
        self.weight_label = tkinter.Label(self.main_window, text = "Enter athlete's weight (kgs): ")
        self.weight_label.grid(row = 1, column = 2)

        self.weight = tkinter.StringVar()
        self.weight_entry = tkinter.Entry(self.main_window, width = 7, textvariable = self.weight)
        self.weight_entry.grid(row = 1, column = 3)

        self.calculate_button = tkinter.Button(self.main_window, text="Calculate BMI", command=self.calculate_BMI)
        self.calculate_button.grid(row=2, column=3, pady = 35)
        
        self.BMI_label = tkinter.Label(self.main_window, text = "Athlete's BMI is: ")
        self.BMI_label.grid(row = 3, column = 2)

        self.BMI = tkinter.StringVar()
        self.BMI_entry = tkinter.Entry(self.main_window, state = "readonly",width = 20,textvariable = self.BMI)
        self.BMI_entry.grid (row=3,column=3)
        
        self.MHR_label = tkinter.Label (self.main_window, text = "Enter maximum heart rate (bpm): ")
        self.MHR_label.grid(row = 0, column = 4)

        self.MHR = tkinter.StringVar()
        self.MHR_entry = tkinter.Entry(self.main_window, width = 10, textvariable = self.MHR)
        self.MHR_entry.grid (row = 0, column = 5)
        
        self.RHR_label = tkinter.Label(self.main_window, text = "Enter resting heart rate(bpm): ")
        self.RHR_label.grid (row = 1, column =4)

        self.RHR = tkinter.StringVar()
        self.RHR_entry = tkinter.Entry(self.main_window, width =10, textvariable = self.RHR)
        self.RHR_entry.grid (row = 1, column = 5)

        self.calculateVO2_button = tkinter.Button(self.main_window, text= "Calculate VO2 max ", command = self.calculate_VO2)
        self.calculateVO2_button.grid(row = 2, column = 5)
                                      
        self.VO2_label = tkinter.Label(self.main_window, text = "Athlete's VO2 max is: ")
        self.VO2_label.grid (row = 3, column = 4)

        self.VO2 = tkinter.StringVar()
        self.VO2_entry = tkinter.Entry(self.main_window, state = "readonly",width = 10, textvariable = self.VO2)
        self.VO2_entry.grid (row = 3, column = 5)

        self.Restart_button = tkinter.Button(self.main_window, text = 'Restart with different player', command = self.reset_inputs)
        self.Restart_button.grid(row = 9, column = 3)

        self.Quit_button = tkinter.Button(self.main_window, text = 'Quit',command = self.main_window.destroy)
        self.Quit_button.grid (row = 9, column = 4)
        
        for player in self.dict1:
            self.listbox.insert(tkinter.END,player)
        self.player_entry.grid(row=0,column=3)

        
# Create an instance of the HealthCalculator class    
def main():       
    if __name__ == "__main__":
        calculator = HealthCalculatorGUI()
main()
