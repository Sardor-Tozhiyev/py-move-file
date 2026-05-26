import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source, destination = parts

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
                current_path = os.path.join(current_path, part)
            if not os.path.exists(current_path):
                os.makedirs(current_path, exist_ok=True)

    os.rename(source, destination)
