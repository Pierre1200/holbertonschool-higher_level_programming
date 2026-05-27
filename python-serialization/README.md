Python - Serialization
Introduction:
Welcome to our exploration of marshaling and serialization, two fundamental concepts in computer science that enable the efficient storage and transmission of data. In this programming project, you will delve deep into how data can be transformed and communicated between different parts of a system, or even across different systems. This project is designed to enhance your understanding and practical skills in handling data in real-world applications.

What is Marshaling?
Marshaling is the process of transforming memory objects into a format that can be stored or transmitted over a network. It involves packaging complex objects and their attributes into a simpler, often binary, format. This is crucial in scenarios such as remote procedure calls, where objects need to be represented in a standard format across different computing platforms.

What is Serialization?
Serialization, closely related to marshaling, specifically involves converting data structures or object states into a format that can be easily saved to a file or sent over a network. The main goal of serialization is to preserve the state of an object, so it can be recreated in an identical state elsewhere. This becomes essential in developing applications that require data persistence, distributed computing, and data sharing between different software components.

Learning Objectives:
Articulate the differences and similarities between marshaling and serialization.
Implement serialization in a practical programming task.
Understand how serialized data can be used in web applications, databases, and network communications.
Evaluate the performance implications of different serialization formats, like JSON, XML, and binary formats.
Resources:
Real Python Serialization
Real Python: Working With JSON Data in Python
Python's pickle documentation
Corey Schafer on Pickle
CSV to JSON in Python
Python XML ElementTree Guide
Socket Programming Guide
This project will equip you with the skills needed to manipulate and manage data effectively, preparing you for more advanced topics in computer science and software development. Get ready to build a solid foundation in data handling that will support your future projects and career in the technology sector.

Tasks
0. Basic Serialization
Create a basic serialization module that adds the functionality to serialize a Python dictionary to a JSON file and deserialize the JSON file to recreate the Python Dictionary.

Instructions:
Write a Python module named task_00_basic_serialization.py with the following functions:

def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    pass

def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    pass
The function serialize_and_save_to_file take 2 parameters:

data: A Python Dictionary with data
filename: The filename of the output JSON file. If the output file already exists it should be replaced.
The function load_and_deserialize take 1 parameters:

filename: The filename of the input JSON file This function returns a Python Dictionary with the deserialized JSON data from the file.