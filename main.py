"""DNS Flush Tool — Flush the Windows DNS cache and show the resolver list."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='dns_flush_tool',
        description='Flush the Windows DNS cache and show the resolver list.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('DNS Flush Tool')
    print('ipconfig /flushdns with a before/after peek.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
