import os
import re
from collections import defaultdict


def find_duplicates(folder):
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    base_map = defaultdict(list)

    # Pattern to detect numbered duplicate: "name (1).txt"
    numbered_pattern = re.compile(r"^(.*)\((\d+)\)(\.[^.]+)$")

    for file in files:
        name, ext = os.path.splitext(file)
        m = numbered_pattern.match(file)
        if m:
            # Key: base name without "(n)"
            base = m.group(1).strip()
            key = (base.lower(), None)
        else:
            base = name
            # Key for same-name different extensions
            key = (base.lower(), None)

        base_map[key].append(file)

    # Now refine groups: numbered vs different extensions
    numbered_groups = []
    ext_groups = []

    # Find numbered sets
    for key, group in base_map.items():
        numbered_files = []
        for f in group:
            if numbered_pattern.match(f):
                # extract actual base
                name, _ = os.path.splitext(f)
                base_name = re.sub(r"\(\d+\)$", "", name).strip()
                numbered_files.append((base_name, f))
        if len(numbered_files) > 1:
            numbered_groups.append([f for _, f in numbered_files])

    # Find extension groups
    ext_map = defaultdict(list)
    for file in files:
        name, ext = os.path.splitext(file)
        ext_map[name.lower()].append(file)

    for name, group in ext_map.items():
        if len(group) > 1:
            ext_groups.append(group)

    return numbered_groups, ext_groups


def present_and_delete(folder, numbered, ext_groups):
    all_groups = []
    print("\n===== DUPLICATE GROUPS FOUND =====\n")
    count = 1

    # Display numbered duplicate groups
    for group in numbered:
        print(f"Group {count}: Numbered duplicates")
        for idx, f in enumerate(group, start=1):
            print(f"  {idx}. {f}")
        all_groups.append(("num", group))
        count += 1
        print()

    # Display extension groups
    for group in ext_groups:
        print(f"Group {count}: Same name, different extensions")
        for idx, f in enumerate(group, start=1):
            print(f"  {idx}. {f}")
        all_groups.append(("ext", group))
        count += 1
        print()

    # If no duplicates
    if not all_groups:
        print("No duplicates found.")
        return

    print("Enter your choices, one line per group:")
    print("Format: group_number choice_number")
    print("For example: '2 1' means in Group 2 keep file #1 and delete rest.\n")

    selections = []
    for i in range(len(all_groups)):
        sel = input(f"Selection for Group {i + 1}: ").strip()
        try:
            g, c = map(int, sel.split())
            selections.append((g, c))
        except ValueError:
            print("Invalid input, skipping this group.")
            selections.append((i + 1, None))

    # Perform deletion
    for g_idx, sel_choice in selections:
        if sel_choice is None:
            continue
        group_type, group_list = all_groups[g_idx - 1]
        keep_index = sel_choice - 1

        if 0 <= keep_index < len(group_list):
            keep_file = group_list[keep_index]
            for f in group_list:
                if f != keep_file:
                    path = os.path.join(folder, f)
                    try:
                        os.remove(path)
                        print(f"Deleted: {f}")
                    except Exception as e:
                        print(f"Failed to delete {f}: {e}")
        else:
            print(f"Choice {sel_choice} out of range for group {g_idx}!")

    print("\nDone!")


def main():
    folder = input("Enter folder path to scan: ").strip()
    if not os.path.isdir(folder):
        print("Invalid folder.")
        return

    numbered, ext_groups = find_duplicates(folder)
    present_and_delete(folder, numbered, ext_groups)


if __name__ == "__main__":
    main()
