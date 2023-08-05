#!/bin/bash

# Create main directories
mkdir -p virtual-os/src
mkdir -p virtual-os/tests

# Create source files
touch virtual-os/src/__init__.py
touch virtual-os/src/file_system_node.py
touch virtual-os/src/virtual_shell.py
touch virtual-os/src/main.py

# Create test files
touch virtual-os/tests/__init__.py
touch virtual-os/tests/test_file_system_node.py
touch virtual-os/tests/test_virtual_shell.py

# Create README
touch virtual-os/README.md

echo "Project structure created successfully!"
