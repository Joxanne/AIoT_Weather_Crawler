# Change Proposal: Add CLI Support

## Summary
Add command-line interface (CLI) support to the weather crawler script to allow users to specify the output database file and toggle verbose logging.

## Motivation
Currently, the database name is hardcoded, and logging is always on. Users need flexibility to run the crawler with different configurations without modifying the code.

## Proposed Changes
- Use `argparse` to handle command-line arguments.
- Add `--db` argument to specify database path.
- Add `--verbose` argument to control output verbosity.
