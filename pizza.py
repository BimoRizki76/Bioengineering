TOPPINGS = [
    "Pepperoni",
    "Mushrooms",
    "Caramelized onions",
    "Roasted garlic",
    "Pineapple",
    "Hot honey drizzle",
    "Truffle oil",
]

CRUSTS = [
    "Cheese",
    "Sausages",
]


def show_menu(title, options):
    print(f"\n{title}")
    for number, option in enumerate(options, start=1):
        print(f"  {number}. {option}")


def choose_toppings():
    show_menu("Toppings (pick any, e.g. 1 3 5, or press Enter for none):", TOPPINGS)
    while True:
        answer = input("Your toppings: ").replace(",", " ").split()
        if all(a.isdigit() and 1 <= int(a) <= len(TOPPINGS) for a in answer):
            picks = sorted(set(int(a) for a in answer))
            return [TOPPINGS[p - 1] for p in picks]
        print(f"Please enter numbers between 1 and {len(TOPPINGS)}.")


def choose_crust():
    show_menu("Stuffed crust (pick one):", CRUSTS)
    while True:
        answer = input("Your crust: ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(CRUSTS):
            return CRUSTS[int(answer) - 1]
        print(f"Please enter a number between 1 and {len(CRUSTS)}.")


def main():
    print("Welcome to the Pizza Builder!")
    toppings = choose_toppings()
    crust = choose_crust()

    print("\nYour pizza:")
    print(f"  Crust: {crust} stuffed crust")
    print(f"  Toppings: {', '.join(toppings) if toppings else 'Plain (no toppings)'}")
    print("Enjoy your pizza!")


if __name__ == "__main__":
    main()
