# Python projects and exercises

## References

- [Python roadmap](https://github.com/iBrokeTheCode/python-projects)

## List of Projects

1. [Text File Analyzer Tool](./projects/text_file_analysis/README.md)

## Poetry

### Installation

- Install Poetry. Follow [doc instructions](https://python-poetry.org/docs/#installing-with-the-official-installer)

```shell
# Install
curl -sSL https://install.python-poetry.org | python3 -

# Add to PATH
export PATH="$HOME/.local/bin:$PATH"

echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Verify installation
poetry --version

# Enable completions
mkdir $ZSH_CUSTOM/plugins/poetry
poetry completions zsh > $ZSH_CUSTOM/plugins/poetry/_poetry

# Add to plugins
plugins(
	poetry
	...
	)
```

- If you want to create virtualenvs inside projects:

```shell
poetry config virtualenvs.in-project true
```

- Some Poetry's basics commands

```shell
# Initialize a new Poetry project (creates pyproject.toml)
poetry init

# Install all dependencies defined in pyproject.toml
poetry install

# Add a package to the project (default adds to main dependencies)
poetry add <package-name>

# Add a package as a development dependency (e.g., testing tools)
poetry add <package-name> --dev

# Remove a package from the project
poetry remove <package-name>

# Update all dependencies to their latest versions according to pyproject.toml
poetry update

# Create a virtual environment for the project
poetry shell

# Run a command within the virtual environment without activating it
poetry run <command>

# Show the status of installed dependencies
poetry show

# Display information about the project and its dependencies
poetry show --tree

# Display the dependency tree for the project
poetry show --dev

# Lock the dependencies (regenerate poetry.lock)
poetry lock

# Check if dependencies are up-to-date with their version constraints
poetry check

# Publish the project to a repository (e.g., PyPI)
poetry publish --build
```
