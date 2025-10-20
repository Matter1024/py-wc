import argparse

def main() -> None:
    parser = argparse.ArgumentParser(
        description="""A Python implementation of the Unix wc utility.
                This tool counts the number of lines, words, bytes,
                and characters in the specified files.""",
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
