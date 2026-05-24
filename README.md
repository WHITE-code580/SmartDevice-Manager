“SmartDevice Manager”

This small project illustrates the use of Object-Oriented Programming (OOP) principles in Python, which include:

•	Classes and Objects

•	Inheritance

•	Encapsulation through Properties

•	Method Overriding

The program defines a base class named ElectronicDevice and a derived class called Smartphone.

Features:

ElectronicDevice Class

The ElectronicDevice class delivers comprehensive information about electronic devices, including:

•	Brand

•	Model

•	Description

•	Price

Additionally, it also includes:

-Getters and setters using @property

-A method to display device information

Smartphone Class

The Smartphone class inherits from ElectronicDevice and adds smartphone-specific features such as:

-Operating System

-Screen Size

-Battery Capacity

-Camera Resolution

-Storage Capacity

Furthermore, the class overrides the make_electronic_device() method to include extra smartphone details.

Programming Language Used:

Python 3

Project Structure:

project/

│

├── main.py

└── README.md

OOP Concepts Demonstrated:

1.	Encapsulation
   
Private attributes were used with getters and setters through @property.

Example:

@property

def brand(self):

return self._brand

2.	Inheritance
   
Class Smartphone inherits all attributes and methods from Class ElectronicDevice.

class Smartphone(ElectronicDevice):

3.	Method Overriding
   
The child class overrides the make_electronic_device() method to give more comprehensive information.

How to Run:

1.	Install Python 3
   
2.	Save the code in a file named main.py
   
3.	Run the file: main.py
   
Future Improvements:

Possible improvement for this project:

1.	Add more device types, such as Laptop and Tablet

2.	Display prices with two decimal places
   
3.	Add a Simple Discount Method
   
Author:

Created by Maria S. S. - [WHITE-code58]

