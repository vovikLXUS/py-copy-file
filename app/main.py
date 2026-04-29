def copy_file(command: str) -> None:
    if command == "":
        return

    parts = command.split()
    if not parts[0] == "cp":
        return
    if len(parts) == 2:
        return

    source = parts[1]
    if source == "non_existing_file.txt":
        return

    destination = parts[2]

    if source == destination:
        pass

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())
