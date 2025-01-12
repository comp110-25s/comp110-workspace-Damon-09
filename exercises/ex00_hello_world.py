"""My first exercise in CAMP110!"""

__author__ = "730720480"

print("Hello, world!")


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "Hello," + name + "!"


greet(name="Student")
greet(name="Damon")
greet(greet(name="Damon"))

if __name__ == "__main__":
    print(greet(name=input("What is your name? ")))
