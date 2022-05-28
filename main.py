import numbers
from tokenize import Number

class Student:
    # [assignment] Skeleton class. Add your code here


    
    def __init__(self, name, age, tracks, score):
       
    
        self.name = name
        self.age = age
        self.score = score
        self.tracks = tracks


    def change_name(self,name: str) -> str:
        """
        Takes a string data type and and throws up the error message not a strring if it recieves any other datatype.
        :param a: any text of typestring
        :return : returns the result of the value entered in name"""
        
        self.name = name 
        if not isinstance(name,(str)):
            raise TypeError("Not a string")
        return self.name

        

    def change_age(self, age: int) -> int:
        """
        Takes an int data type and and throws up the error message not an integer if it recieves any other datatype.
        :param a: any text of type string
        :return : returns the result of the value entered in a"""
      
        self.age = age
        if not isinstance(age,(int)):
            raise TypeError("Not an integer")
        return self.age
        

    def add_track(self, tracks) -> list:
        """
        Takes a list data type 
        :param tracks: any string in a list 
        :return : returns the list of the value entered in tracks"""
        
        self.tracks.append(tracks)
        return self.tracks

      

    def get_score(self) -> Number:
        
        """
        Takes a number data type 
        :return : gets the score of the Student"""

        return self.score
    

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)


# Expected methods
print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_track("UI/UX"))
print(Bob.get_score())

# with open (Student.Bob) as f:
#     lines = f.readlines()


