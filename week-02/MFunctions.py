class MFunction():
    def age_category_r(age1):
        if(age1 < 18):
            print("Children")
            cate="Children"
        elif( age1 < 35):
            print("Adult")
            cate="Adult"
        elif( age1 < 59):
            print("Citizen")
            cate="Citizen"
        else:
            print("Senior Citizen")
            cate="Senior Citizen"
        return cate

    def odd_even():
        num=int(input("Enter a number"))
        if(num%2 == 0):
            print(f"{num} is Even Number")
            message = "Even Number"
        else:
            print(f"{num} is odd Number")
            message = "Odd Number"
        return message

    def BMI():
        bmi = float(input("Please Enter the BMI index:"))
        print("BMI:",bmi)
        if(bmi < 18.5):
            print("Underweight")
            message="Underweight"
        elif(bmi < 25):
            print("Healthy Weight")
            message="Healthy weight"
        elif(bmi < 30):
            print("Overweight")
            message="Overweight"
        elif(bmi < 35):
            print("Obese Class 1")
            message="Obese Class 1"
        elif(bmi < 40):
            print("Obese Class 2")
            message="Obese Class 2"
        else:
            print("Obese Class 3")
            message="Obese Class 3"    

    def Subfields():
         print("Sub-fields in AI are:")
         print("Machine Learning")
         print("Neural Networks")
         print("Vision")
         print("Robotics")
         print("Search Processing")
         print("Natutal Language Processing")

    def Eligible():
        gender=input("Please Enter your Gender(Male/Female): ")
        age=int(input("Please Enter Your age: "))
        print("gender: ",gender)
        print("age: ", age)
        if(gender == "Male"):
            if(age < 21):
                print("NOT ELIGIBLE")
            else:
                print("ELIGIBLE")
        elif(gender == "Female"):
             if(age < 18):
                print("NOT ELIGIBLE")
             else:
                print("ELIGIBLE")


    def percentage():
        Subject1= 98
        Subject2= 87
        Subject3= 95
        Subject4= 95
        Subject5= 93
        total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
        countOfSub = len([Subject1,Subject2, Subject3, Subject4, Subject5])
        Percentage = total/countOfSub
        print("Total=",total)
        print("Average=",Percentage)

    def triangle():
        Height=32
        Breadth=34
        print("Area formula: (Height*Breadth)/2")
        area = (Height * Breadth)/2
        print("Area of Triangle: ",area)
        Height1=2
        Height2=4
        Breadth1=4
        print("Height1 :",Height1)
        print("Height2 :",Height2)
        print("Breath :",Breadth1)
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter = Height1 + Height2 + Breadth1
        print("Perimeter of Triangle: ",perimeter)