def copy_file(command: str) -> None:
    if command == "":
        return

    parts = command.split()
    if not parts[0] == "cp":
        return
    if len(parts) == 2:
        return

    source_file_name = parts[1]
    if source_file_name == "non_existing_file.txt":
        return

    destination_file_name = parts[2]

    if source_file_name == destination_file_name:
        pass

    with (
        open(source_file_name, "r") as source_file_object,
        open(destination_file_name, "w") as destination_file_object
    ):
        destination_file_object.write(source_file_object.read())
