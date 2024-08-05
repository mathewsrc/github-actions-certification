#!/bin/bash
set -e

echo "Starting post-entrypoint steps..."

# Delete garbage.txt
rm -f garbage.txt

echo "Post-entrypoint steps completed successfully."