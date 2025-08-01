#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""

import sys


def print_stats(total_size, status_codes):
    """Print the statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.strip().split()
            # Process any line that has content
            if parts:
                try:
                    # Try to get file size from the last element
                    file_size = int(parts[-1])
                    total_size += file_size

                    # Try to get status code from second-to-last element
                    if len(parts) >= 2:
                        status_code = int(parts[-2])
                        if status_code in status_codes:
                            status_codes[status_code] += 1

                    line_count += 1

                    # Print stats every 10 lines
                    if line_count % 10 == 0:
                        print_stats(total_size, status_codes)
                except (ValueError, IndexError):
                    # Skip malformed lines
                    continue

        # Print final stats when input ends
        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        # Print final stats on Ctrl+C
        print_stats(total_size, status_codes)
        raise
