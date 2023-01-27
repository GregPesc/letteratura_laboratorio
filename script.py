from text_analyzer import analyze
from text_parser import parse_file

file_name = "sonetti.txt"
json_name = "parsed_file.json"


def main() -> None:
    """
    Runs the script
    """
    parse_file(file_name=file_name)
    analyze(file_name=json_name)


if __name__ == "__main__":
    main()
