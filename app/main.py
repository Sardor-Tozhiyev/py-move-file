import os


def move_file(command: str) -> None:
    parts = command.split()

    if parts[0] != "mv":
        return

    source = parts[1]
    destination = parts[2]

    if destination.endswith("/"):
        destination = destination + os.path.basename(source)

    dest_dir = os.path.dirname(destination)
    if dest_dir:
        parts_dir = dest_dir.split("/")
        current_path = ""
        for part in parts_dir:
            if not current_path:
                current_path = part
            else:
                current_path = current_path + "/" + part
            if not os.path.exists(current_path):
                os.mkdir(current_path)

    os.rename(source, destination)
