import argparse
import os
from datetime import datetime


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="*", default=[])
    parser.add_argument("-f", default=None)
    args = parser.parse_args()

    target_dir = ""
    if args.d:
        target_dir = os.path.join(*args.d)
        os.makedirs(target_dir, exist_ok=True)

    if args.f:
        file_path = os.path.join(target_dir, args.f) if target_dir else args.f

        lines = []
        while True:
            try:
                line = input("Enter content line: ")
            except EOFError:
                break
            if line == "stop":
                break
            lines.append(line)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        formatted_lines = [f"{timestamp}"]
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
