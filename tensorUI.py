from Tkinter import *


class TensorUI:
    def __init__(self, parent):
        #Define basic methods and scenarios as lists and dictionaries
        self.scenarios=["Basic Tensor", "With Auxiliary Info", "Online Tensor Completion"]
        self.methods={"Basic Tensor":["a","b","c"],"With Auxiliary Info":["c","d","e"],"Online Tensor Completion":["f","g","h"]}
        self.selectedScenario=self.scenarios[0]
        self.selectedMethods=self.methods["Basic Tensor"]

        #Define the top level container
        self.myContainer1 = Frame(parent)
        self.myContainer1.pack()

        #Label and Drop Down for Scenarios
        self.label1=Label(self.myContainer1,text="Select Scenario")
        self.label1.grid(row=0,column=0)
        var1 = StringVar()
        var1.set(self.scenarios[0])
        scenario_option=OptionMenu(self.myContainer1, var1, *self.scenarios, command=self.methodOption)
        scenario_option.grid(row=0,column=1)

        #Label and Dynamic Dropdown for Methods
        self.label2 = Label(self.myContainer1, text="Select Method")
        self.label2.grid(row=1, column=0)
        var2 = StringVar()
        var2.set(self.selectedMethods[0])
        method_option = OptionMenu(self.myContainer1, var2, *self.selectedMethods)
        method_option.grid(row=1, column=1)

        #Label and select file option
        self.label3 = Label(self.myContainer1, text="Select File")
        self.label3.grid(row=2, column=0)

        #Operation Lable and Radio Buttons
        self.label4 = Label(self.myContainer1, text="Operation")
        self.label4.grid(row=3, column=0)

        #Submit button
        self.button1 = Button(self.myContainer1, text="Submit",command=self.submitClick)
        self.button1.grid(row=4, column=1)

    #Event Handler for Submit Button
    def submitClick(self):
        print "Submit Clicked"

    #Event Handler for Changing Scenarios from Dorpdown
    def methodOption(self,value):
        self.selectedScenario=value
        var2 = StringVar()
        if self.selectedScenario == self.scenarios[0]:
            self.selectedMethods = self.methods[self.scenarios[0]]
        elif self.selectedScenario == self.scenarios[1]:
            self.selectedMethods = self.methods[self.scenarios[1]]
        else:
            self.selectedMethods = self.methods[self.scenarios[2]]

        var2.set(self.selectedMethods[0])
        method_option=OptionMenu(self.myContainer1, var2, *self.selectedMethods)
        method_option.grid(row=1,column=1)



root = Tk()
myapp = TensorUI(root)
root.mainloop()