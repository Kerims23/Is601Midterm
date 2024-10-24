# Midterm 

## Video Demonstration
Link to video demonstration (https://youtu.be/Cb69KNSChsg).

## walk through of code.
- pip install -r requirements.txt
- create .env file and include 
    - LOG_LEVEL=INFO
    - LOG_OUTPUT=logs/app.log
    - HISTORY_FILE=data/account.csv
    - ENVIRONMENT=development
- Run python main.py
    - should see the data folder have a file called account.csv populated in data folder
- enter your name 
- enter a command 
    - for **operation** (+,-,/,*) commands make sure you save after each command
    - **save** should save the operation (will recreate the csv if it has been deleted)
    - **load** will show whats currently in the account.csv
    - **delete** will ask for a index of a record. (can see this in load)
    - **clear** will clear out the full file(by delete the entire csv.)
- **exit** to close app.
- run pytest --num_records=10 (or any number above 10)
- run pytest --pylint --cov to see coverage of testing


## methodology:

LBYL (Look Before You Leap) and EAFP (Easier to Ask for Forgiveness than Permission)

- LBYL for operations.
- EAFP for history management.



## Evaluation Criteria

### Total Points: 100

#### Functionality (40 Points)

- **Calculator Operations:** Calculator operations in operations.py
- **History Management:** History.py does history operations using pandas
- **Configuration via Environment Variables:** Added configuration to enviroment variables in app/__init__.py and have it set up in my .env 
- **REPL Interface:** when main.py is ran it has a User friendly UI

#### Design Patterns (20 Points)

- **Implementation and Application:** used classes and formats as we did in the homeworks 
- **Documentation and Explanation:** did my best with comments and logging to explain everything

#### Testing and Code Quality (20 Points)

- **Comprehensive Testing with Pytest:** Did a lot of test coverage and testing. 96%
- **Code Quality and Adherence to Standards:** I tried to keep my code relatively clean and organized

#### Version Control, Documentation, and Logging (20 Points)

- **Commit History:** created multiple branches going over dev and test as I progressed through the project.
- **README Documentation:** added notes into the readme file
- **Logging Practices:** added logging in my code to result to logs folder. 


