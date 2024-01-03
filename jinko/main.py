import typer
from typing_extensions import Annotated

def hello(name: Annotated[str, typer.Argument()]):
    print("Hello " + name)
    return 

def app(
    yaml: Annotated[str, typer.Option(help="Path to yaml file")],
    train: Annotated[bool, typer.Option(help="Enable the flag to train")] = False,
    quantise: Annotated[bool, typer.Option(help="Enable the flag to quantise")] = False,
    serve: Annotated[bool, typer.Option(help="Enable the flag to serve")] = False,
    ):
    ## To be removed
    print("Path: ",path_to_yaml)
    print("train:", train)
    return


def main():
    typer.run(app)

if __name__ == "__main__":
    main()