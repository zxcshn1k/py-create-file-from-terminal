import os
import sys
from datetime import datetime


def parse_arguments() -> tuple[list[str], str | None]:
    args = sys.argv[1:]
    directories = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                directories.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args) and not args[i].startswith("-"):
                file_name = args[i]
                i += 1
        else:
            i += 1

    return directories, file_name


def create_directories(directories: list[str]) -> str:
    target_dir = os.path.join(*directories) if directories else ""
    if target_dir:
        os.makedirs(target_dir, exist_ok=True)
    return target_dir


def collect_content() -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_lines = [timestamp]

    idx = 1
    while True:
        try:
            line = input("Enter content line: ")
        except (EOFError, KeyboardInterrupt):
            break
        if line == "stop":
            break
        formatted_lines.append(f"{idx} {line}")
        idx += 1

    return "\n".join(formatted_lines) + "\n"


def write_to_file(file_path: str, content: str) -> None:
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(content)


def main() -> None:
    directories, file_name = parse_arguments()
    target_dir = create_directories(directories)

    if not file_name:
        return

    file_path = os.path.join(target_dir, file_name) if target_dir else file_name
    new_content = collect_content()
    write_to_file(file_path, new_content)


if __name__ == "__main__":
    main()
