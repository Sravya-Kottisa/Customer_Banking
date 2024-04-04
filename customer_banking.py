# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    while True:
        try:
            savings_balance = float(input("Enter the savings account balance: "))
            break  # Exit the loop if conversion is successful
        except ValueError:
            print("Invalid input! Please enter a valid float value for the balance.")

    while True:
        try:
            savings_interest = float(input("Enter the interest rate for savings account (%): "))
            break  # Exit the loop if conversion is successful
        except ValueError:
            print("Invalid input! Please enter a valid float value for the interest rate.")

    while True:
        try:
            savings_maturity = int(input("Enter the number of months for savings account: "))
            break  # Exit the loop if conversion is successful
        except ValueError:
            print("Invalid input! Please enter a valid integer value for the number of months.")

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Savings Account - Interest Earned: ${interest_earned:.2f}, Updated Balance: ${updated_savings_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    while True:
        try:
            cd_balance = float(input("Enter the CD account balance: "))
            break  # Exit the loop if conversion is successful
        except ValueError:
            print("Invalid input! Please enter a valid float value for the balance.")

    while True:
        try:
            cd_interest = float(input("Enter the interest rate for CD account (%): "))
            break  # Exit the loop if conversion is successful
        except ValueError:
            print("Invalid input! Please enter a valid float value for the interest rate.")

    while True:
        try:
            cd_maturity = int(input("Enter the number of months for CD account: "))
            break  # Exit the loop if conversion is successful
        except ValueError:
            print("Invalid input! Please enter a valid integer value for the number of months.")


    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"CD Account - Interest Earned: ${interest_earned:.2f}, Updated Balance: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    # Call the main function.
     main()