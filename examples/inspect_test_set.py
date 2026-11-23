"""Inspect the released PalmLeaf-VQA test set without extracting the ZIP."""

import argparse
from collections import Counter
import json
from pathlib import Path
from zipfile import BadZipFile, ZipFile


def load_test_records(archive_path):
    """Return the released annotation rows with answers unchanged."""
    with ZipFile(archive_path) as archive, archive.open("data/test.jsonl") as rows:
        return [json.loads(line) for line in rows if line.strip()]


def print_summary(records):
    images = {row["image_id"]: row["script_name"] for row in records}
    image_counts = Counter(images.values())
    qa_counts = Counter(row["script_name"] for row in records)

    print(f"Test split: {len(images):,} image records, {len(records):,} QA pairs")
    for collection, count in sorted(image_counts.items()):
        print(f"  {collection}: {count:,} image records, {qa_counts[collection]:,} QA pairs")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path, help="Path to the released test-set ZIP")
    parser.add_argument("--image", help="Image filename or ID, e.g. Khmer_0009.jpg")
    args = parser.parse_args()

    try:
        records = load_test_records(args.archive)
    except (OSError, BadZipFile, KeyError, ValueError) as exc:
        parser.error(f"could not read test annotations from {args.archive}: {exc}")

    if not args.image:
        print_summary(records)
        return

    matches = [
        row for row in records if args.image in (row["image_name"], row["image_id"])
    ]
    if not matches:
        parser.error(f"image not found in the test set: {args.image}")

    print(f"Image in ZIP: {matches[0]['image_path']}")
    for row in sorted(matches, key=lambda row: row["question_id"]):
        print(f"\n{row['question_id']}. [{row['category']}] {row['question_en']}")
        print(f"   Answer: {row['answer']}")


if __name__ == "__main__":
    main()
