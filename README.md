# Banking Program

## Overview

This repository contains a banking program written in Python. The program enables users to create savings and Certificate of Deposit (CD) accounts, calculate interest earned based on user-provided parameters, and update account balances accordingly.

## File Structure

- **Accounts.py**: Defines the Account class with methods to set the balance and interest.
- **savings_account.py**: Implements the create_savings_account function to instantiate a savings account, compute interest earned, update the balance, and return the results.
- **cd_account.py**: Implements the create_cd_account function to instantiate a CD account, calculate interest earned, update the balance, and return the results.
- **customer_banking.py**: Main file responsible for user interaction. It prompts users to input account details, invokes the appropriate functions, and displays the results.

## Usage

1. **savings_account.py**:
Import the Account class from Accounts.py.
Implement the create_savings_account function to create a savings account instance, calculate interest earned, update the balance, and return the results.

2. **cd_account.py**:
Import the Account class from Accounts.py.
Implement the create_cd_account function to create a CD account instance, calculate interest earned, update the balance, and return the results.

3. **customer_banking.py**:
Import the create_savings_account and create_cd_account functions.
Implement the main function to prompt users for account details, call the corresponding functions, and display the results.
Execute the main function to run the program.

### Requirements

- Python 3.x

### How to Run

1. Ensure all files (Accounts.py, savings_account.py, cd_account.py, and customer_banking.py) are in the same directory.
2. Execute the customer_banking.py file.
3. Follow the prompts to input account details.
4. View the interest earned and updated account balances.
