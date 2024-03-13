from L8module.MCm import simulate_stock_market

def main():
    num_days = 1000  # You can adjust the number of days for simulation
    fractions = simulate_stock_market(num_days)
    print(f'Fractions of days in each state over {num_days} days:')
    print(f'Bull: {fractions[0]:.2f}')
    print(f'Bear: {fractions[1]:.2f}')
    print(f'Recession: {fractions[2]:.2f}')

if __name__ == "__main__":
    main()
