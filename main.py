from pathlib import Path

TEXT = "Sorry — I got so invested in that climax I forgot I was supposed to deliver it, not blink along with you."


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT, encoding="utf-8")
    assert output_path.read_text(encoding="utf-8") == TEXT


if __name__ == "__main__":
    main()
