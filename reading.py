class Reading:
    def __init__(self):
        self.db = dict()

    def setSystolic(self, systolic:int) -> None:
        self.systolic = systolic

    def getSystolic(self)->int:
        return self.systolic
    
    def setDiastolic(self, diastolic: int)->None:
        self.diastolic = diastolic

    def getDiastolic(self)->int:
        return self.diastolic

    def setPulse(self, pulse: int)->None:
        self.pulse = pulse

    def getPulse(self)->int:
        return self.pulse
    
    def __str__(self):
        return f"SYSTOLIC: \t{self.getSystolic()}\nDIASTOLIC:\t{self.getDiastolic()}\nPULSE:\t{self.getPulse()}"
    

