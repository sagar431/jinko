import typer
from typing_extensions import Annotated

def hello(name: Annotated[str, typer.Argument()]):
    print("Hello " + name)
    return 

def main():
    typer.run(hello)

# if __name__ == "__main__":
#     typer.run(hello)