import os
import sys
from datetime import datetime


def main() -> None:
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

    target_dir = os.path.join(*directories) if directories else ""
    if target_dir:
        os.makedirs(target_dir, exist_ok=True)

    if not file_name:
        return

    file_path = os.path.join(target_dir, file_name) if target_dir else file_name

    lines = []
    while True:
        try:
            line = input("Enter content line: ")
        except (EOFError, KeyboardInterrupt):
            break
        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_lines = [timestamp]
    for idx, line in enumerate(lines, start=1):
        formatted_lines.append(f"{idx} {line}")
    new_content = "\n".join(formatted_lines) + "\n"

    mode = "a" if os.path.exists(file_path) else "w"
    with open(file_path, mode, encoding="utf-8") as f:
        if mode == "a" and os.path.getsize(file_path) > 0:
            f.write("\n")
        f.write(new_content)


if __name__ == "__main__":
    main()
