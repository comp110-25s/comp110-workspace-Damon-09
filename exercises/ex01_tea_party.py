"""__author__"""

__author__: str = "730720480"


def tea_bags(people: int) -> int:
    num_tea_bags = people * 2
    return num_tea_bags


def treats(people: int) -> float:
    num_treats = tea_bags(people) * 1.5
    return num_treats


def cost(tea_count: int, treat_count: int) -> float:
    total_cost = tea_count * 0.5 + treat_count * 0.75
    return total_cost


def main_planner(guests: int):
    str_tea_bag = str(tea_bags(guests))
    str_Treats = str(treats(guests))
    str_cost = str(cost(tea_bags(guests), treats(guests)))
    guests_str = str(guests)

    print("A Cozy Tea Party for " + guests_str + " People!")
    print("Tea Bags: " + str_tea_bag)
    print("Treats: " + str_Treats)
    print("Cost: " + str_cost)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
