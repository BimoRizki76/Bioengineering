import sys


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


def choose_toppings(ask=input):
    show_menu("Toppings (pick any, e.g. 1 3 5, or press Enter for none):", TOPPINGS)
    while True:
        answer = ask("Your toppings: ").replace(",", " ").split()
        if all(a.isdigit() and 1 <= int(a) <= len(TOPPINGS) for a in answer):
            picks = sorted(set(int(a) for a in answer))
            return [TOPPINGS[p - 1] for p in picks]
        print(f"Please enter numbers between 1 and {len(TOPPINGS)}.")


def choose_crust(ask=input):
    show_menu("Stuffed crust (pick one):", CRUSTS)
    while True:
        answer = ask("Your crust: ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(CRUSTS):
            return CRUSTS[int(answer) - 1]
        print(f"Please enter a number between 1 and {len(CRUSTS)}.")


def scripted_answers(answers):
    """Return an input-like function that types the given answers for you."""
    remaining = iter(answers)

    def ask(prompt):
        answer = next(remaining)
        print(f"{prompt}{answer}")
        return answer

    return ask


def main(ask=input):
    print("Welcome to the Pizza Builder!")
    toppings = choose_toppings(ask)
    crust = choose_crust(ask)

    print("\nYour pizza:")
    print(f"  Crust: {crust} stuffed crust")
    print(f"  Toppings: {', '.join(toppings) if toppings else 'Plain (no toppings)'}")
    print("Enjoy your pizza!")


def simulate():
    # Topping 6 = Hot honey drizzle, crust 2 = Sausages
    print("=== Simulated order ===")
    main(scripted_answers(["6", "2"]))


if __name__ == "__main__":
    if "--simulate" in sys.argv:
        simulate()
    else:
        main()
