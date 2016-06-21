#===============================================================================
# tk8x8.py
#
# Tkinter based GUI for interacting with Adafruit 8x8 LED matrices.
#
# 2016-05-26
# Carter Nelson
#===============================================================================
from Tkinter import *

from Adafruit_LED_Backpack import Matrix8x8

LED_COLOR = {
    "off"           : "#505050",
    "red"           : "#fe3521",
    "green"         : "#30ff30",
    "pure-green"    : "#0fff87",
    "yellow-green"  : "#a8ee19",
    "yellow"        : "#fdb71a",
    "blue"          : "#1ac4ff",
    "white"         : "#fefefe",
}

NX = 8
NY = 8
I2C_ADDRESS = 0x70
LED_ON_COLOR = LED_COLOR["red"]
LED_OFF_COLOR = LED_COLOR["off"]
TXT_FILE = "led8x8.txt"

matrix = Matrix8x8.Matrix8x8(address=I2C_ADDRESS)

class Application(Frame):
    """Tkinter Application to provide interaction with Adafruit 8x8 LED matrix."""

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid() 
        self.vars =[[IntVar() for x in xrange(NX)] for y in xrange(NY)]
        self.checks = [[self.__makecheck__(self.vars[x][y])
                        for x in xrange(NX)]
                        for y in xrange(NY)]

        for x in xrange(NX):
            for y in xrange(NY):
                self.checks[x][y].grid(row=x, column=y, padx=2, pady=2)

        self.b1 = Button(self, text="CLEAR", command=self.clear_all)
        self.b1.grid(row=NX+1,column=0,columnspan=4)
 
        self.b2 = Button(self, text="SAVE", command=self.save_it)
        self.b2.grid(row=NX+1,column=4,columnspan=4)
        
        self.tx_raw64 = Text(self,width=18, height=1)
        self.tx_raw64.grid(row=NX+3,column=0,columnspan=NX)
        self.tx_raw64.insert("1.0","0x0000000000000000")
        
        self.clear_all()
        
    def __makecheck__(self, var=None):
        return Checkbutton(self,
                            text="",
                            indicatoron=False,
                            height=1,
                            width=2,
                            borderwidth=2,
                            background=LED_OFF_COLOR,
                            selectcolor=LED_ON_COLOR,
                            variable=var,
                            command=self.display
                            )

    def report(self):
        """Print current results to screen."""
        print "-"*17
        for x in xrange(NX):
            print "",
            for y in xrange(NY):
                print self.vars[x][y].get(),
            print
        print "-"*17

    def display(self):
        """Display current results on matrix."""
        value = 0
        for y in xrange(NY):
            row_byte = 0
            for x in xrange(NX):
                bit = self.vars[x][y].get()
                row_byte += bit<<x 
                matrix.set_pixel(x, y, bit)
            value += row_byte<<(8*y)    
        matrix.write_display()
        self.tx_raw64.delete("1.0",END)
        self.tx_raw64.insert("1.0",'0x'+format(value,'016x'))

    def clear_all(self):
        """Callback for clear button."""
        for x in xrange(NX):
            for y in xrange(NY):
                self.vars[x][y].set(0)
        self.display()

    def save_it(self):
        """Callback for save button."""
        self.save_txt()
        
    def save_txt(self, filename=TXT_FILE):
        """Save current bitmap to text file."""
        with open(filename,"w") as FILE:
            for y in xrange(NY):
                for x in xrange(NX):
                    FILE.write("{0}, ".format(self.vars[x][y].get()))
                FILE.write("\n")
                                       
#-------------------------------------------------------------------------------
#  M A I N
#-------------------------------------------------------------------------------
if __name__ == "__main__":
    Application(Tk().title("tk8x8")).mainloop()