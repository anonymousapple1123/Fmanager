import logging

from core import rename
from logger_conf import setup_logging

setup_logging()
logger = logging.getLogger()


def input_user_choice():
    while True:
        try:
            choice = int(input(">>> "))
            return choice
        except ValueError:
            print("Try Again.")
        except Exception as e:
            logger.exception("Error in Input<control_panel()>")


def control_panel():
    print(
        "\n\n============================================================================\n"
    )
    print("Choose the appropriate options:")
    print("1. Remove a substring from files.")
    print(
        "_____________________________________________________________________________"
    )
    choice = input_user_choice()
    print(
        "\n============================================================================"
    )

    match choice:
        case 1:
            rename.rename_files(input("Enter Substring :"))
        case _:
            print("Exiting...")
            exit()


if __name__ == "__main__":
    control_panel()
