from core import rename


def control_panel():
    print("Choose the appropriate options:")
    print("1. Remove a substring from files.")
    choice = int(input(">>> "))

    match choice:
        case 1:
            rename.rename_files(input("Enter Substring :"))
        case _:
            print("Exiting...")


if __name__ == "__main__":
    control_panel()
