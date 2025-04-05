# Python projects and exercises

## References

- [Python roadmap](https://github.com/iBrokeTheCode/python-projects)

## List of Projects

1. [Text File Analyzer Tool](./text_file_analysis/README.md)

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
