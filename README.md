# Virtual Operating System

A simple proof-of-concept (PoC) for a virtual operating system that provides a text-based shell interface to interact with a virtual file system. This is a minimal implementation and can be extended to include more complex features.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Virtual file system with directories and files
- Basic shell commands:
  - `ls`: List the contents of the current directory
  - `cd`: Change to a different directory
  - `mkdir`: Create a new directory
  - `touch`: Create a new file
  - `exit`: Exit the virtual shell

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository or download the ZIP file.
2. Navigate to the `src` directory.
3. Run `main.py` using Python 3.x.

## Usage

Once you run `main.py`, you will be presented with a shell prompt where you can use the available commands.

Example:

\`\`\`
/> ls
/> mkdir test_directory
/> cd test_directory
/test_directory> touch test_file
/test_directory> ls
test_file
\`\`\`

## Contributing

Feel free to fork the project, create a feature branch, and send us a pull request. For bugs and feature requests, please create an issue.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
