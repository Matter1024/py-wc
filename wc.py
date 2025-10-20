import argparse

def main() -> None:
    parser = argparse.ArgumentParser(
        description="""A Python implementation of the Unix wc utility.
                This tool counts the number of lines, words, bytes,
                and characters in the specified files.""",
    )

    # --- Options ---
    parser.add_argument(
        "-c",
        "--bytes",
        action="store_true",
        help="Print the bytes count(s)"
    )
    parser.add_argument(
        "-m",
        "--chars",
        action="store_true",
        help="Print the character count(s)"
    )
    parser.add_argument(
        "-l",
        "--lines",
        action="store_true",
        help="Print the newline count(s)"
    )
    parser.add_argument(
        "-L",
        "--max-line-length",
        action="store_true",
        help="Print the maximum display width"
    )
    parser.add_argument(
        "-w",
        "--words",
        action="store_true",
        help="Print the word count(s)"
    )

    parser.add_argument(
        "files",
        nargs="*",
        default=["-"],
        help="Input file(s) to process. If no files are specified, or if \"-\" is provided, read from standard input."
    )

    args: argparse.Namespace = parser.parse_args()

if __name__ == "__main__":
    main()
