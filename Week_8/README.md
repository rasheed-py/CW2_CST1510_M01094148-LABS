# Week 7: Secure Authentication System

Student Name: Abdulrasheed Tayibu  
Student ID: M01094148   
Course: CST1510 -CW2 -  Multi-Domain Intelligence Platform 

## Project Description

A command-line authentication system implementing secure password hashing
This system allows users to register accounts and log in with proper pass

## Features

- Secure password hashing using bcrypt with automatic salt generation
- User registration with duplicate username prevention
- User login with password verification
- Input validation for usernames and passwords
- File-based user data persistence

## Technical Implementation

- Hashing Algorithm: bcrypt with automatic salting
- Data Storage: Plain text file (`users.txt`) with comma-separated values
- Password Security: One-way hashing, no plaintext storage
- Validation: Username (3-20 alphanumeric characters), Password (6-50 characters)


# Week 8: Data Pipeline & CRUD (SQL)

## Project Description

This week focuses on building a simple data pipeline using SQLite.  
The system supports structured data storage and full CRUD operations.

## Features

- SQLite database for persistent storage  
- Full CRUD (Create, Read, Update, Delete)  
- Basic input validation  
- Automatic database/table creation  

## Technical Implementation

- **Database:** SQLite via Python’s `sqlite3`  
- **Pipeline Flow:** Input → Validate → Store → Retrieve  
- **CRUD:** Insert, read, update, and delete rows  
- **Security:** Uses parameterized SQL queries  
