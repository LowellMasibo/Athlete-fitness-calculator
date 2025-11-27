###Athlete fitness & health calculator
## This program calculates athlete BMI and VO2 max
## Inputs: weight, maximum heart rate, minimum heart rate



class HealthCalculator:
    def __init__(self):
         # Initialize a dictionary with athlete positions and their corresponding heights
        self.dict1 = {
            "Point guard 1": "188",
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

    def BMI(self, weight, height):
        # Calculate BMI using weight (in kg) and height (in cm)
            return weight / ((height / 100) ** 2)

        
    def VO2(self, max_heart_rate, resting_heart_rate):
         # Calculate VO2 max using max heart rate and resting heart rate
            return (max_heart_rate / resting_heart_rate) * 15.3

    def main(self):
        while True: 
            print(" === Player Options === ")
            for player in self.dict1:
                print(f'\t{player}')

            player = input("Choose the athlete (or type 'exit' to quit): ")
            if player == 'exit':
                return

            if player in self.dict1:
                weight = float(input("Enter athlete's weight (in kilograms): "))
                height = float(self.dict1[player])
                BMI_calculation = self.BMI(weight, height)
                print(f"Athlete's BMI:{BMI_calculation: .2f}")
            else:
                print("Please choose a valid player from the list.")
                return

            max_heart_rate = int(input("Enter max heart rate in timed mile: "))
            if max_heart_rate > 200:
                print("Invalid maximum heart rate.")
                return

            resting_heart_rate = int(input("Enter resting heart rate: "))
            if resting_heart_rate < 45:
                print("Invalid resting heart rate.")
                return

            VO2_max = self.VO2(max_heart_rate, resting_heart_rate)
            print(f"The athlete's VO2 max is {VO2_max: .2f}")
       
# Instance of  HealthCalculator class is created and main method called
if __name__ == "__main__":
    calculator = HealthCalculator()
    calculator.main()



    
