def monthly_installment(price, down_payment, annual_rate, years):
    loan = price - down_payment
    r = annual_rate / 100 / 12
    n = years * 12
    if r == 0:
        return loan / n
    return loan * r * (1 + r) ** n / ((1 + r) ** n - 1)


if __name__ == "__main__":
    price = float(input("Car price (PKR): "))
    down = float(input("Down payment (PKR): "))
    rate = float(input("Annual interest rate %: "))
    years = int(input("Loan duration (years): "))
    m = monthly_installment(price, down, rate, years)
    print(f"Monthly installment: PKR {m:,.0f}")
