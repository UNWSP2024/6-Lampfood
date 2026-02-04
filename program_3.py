#Elliott Morris, 2/3/2026, Taxes

def calculate_sales_tax(total_sales):
    #constants
    STATE_TAX_RATE = 0.05
    COUNTRY_TAX_RATE = 0.025

    #calculates the taxes
    state_tax = total_sales * STATE_TAX_RATE
    county_tax = total_sales * COUNTRY_TAX_RATE
    total_tax = state_tax + county_tax

    return state_tax, county_tax, total_tax

def main():
    #gets user input
    total_sales = float(input("Enter the total sales for the month: $"))

    # multi-variable set from function call
    state_tax, county_tax, total_tax = calculate_sales_tax(total_sales)

    #print statements
    print(f"County sales tax: ${county_tax:.2f}")
    print(f"State sales tax: ${state_tax:.2f}")
    print(f"Total sales tax: ${total_tax:.2f}")

if __name__ == "__main__":
    main()
