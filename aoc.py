from typing import Callable, Any


def run(
    part_1: Callable[[str], Any], part_2: Callable[[str], Any], input_fname: str
) -> None:
    input_data = input_fname
    try:
        with open(input_fname) as f:
            input_data = f.read()
    except (FileNotFoundError, OSError):
        print("File not found, treating as string.")

    print("[+] Part 1 output:")
    print(part_1(input_data))

    print("------------------")
    print("[+] Part 2 output:")
    print(part_2(input_data))
