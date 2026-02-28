import logging

from core import (
    purge_dupicates,
    purge_substring,
    purge_targets_from_refrence,
    sync_dirs,
)
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
        "\n\n============================================================================"
    )
    print("Choose the appropriate options:")
    print("1. Remove a substring from files.")
    print("2. Remove all duplicates")
    print("3. Sync Folders")
    print("4. Remove duplicates from other folder.")
    print(
        "_____________________________________________________________________________"
    )
    choice = input_user_choice()
    print(
        "\n============================================================================"
    )

    match choice:
        case 1:
            purge_substring.rename_files(
                input("Enter Substring to remove :")
            )  # could have been done gracefully :\
        case 2:
            purge_dupicates.initiate_remove_duplicate()
        case 3:
            sync_dirs.initiate_sync()
        case 4:
            purge_targets_from_refrence.initiate_purge_matches()
        case _:
            print("Exiting...")
            exit()


if __name__ == "__main__":
    control_panel()
