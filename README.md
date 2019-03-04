# Olive

A simple Python parser for task lists.

## Grammar

Task lists are written in plain text. A task list includes one task per line:

```txt
Go to the grocery #errand #personal >m !!
Call Bob re: installation >s !!! #work
Plan menu for dinner party >l
```

### Description

Tasks must begin with a description. Descriptions may include Markdown-style links:

```txt
Read the article on [example website](https://www.example.com)
```

The description may be followed by one or more optional attributes: priority, size, or tags. Attributes may appear in any order.

### Priority

Priorities are indicated by exclamation points:

- ! => low
- !! => medium
- !!! => high
- !!!! => highest

```txt
This task is important !!!
```

### Size

Sizes are indicated by a right angle bracket and a size code:

- \>s => small
- \>m => medium
- \>l => large
- \>xl => extra large

```txt
This task will take a while >l
```

### Tags

Tags are indicated by a hash character:

```txt
This task is tagged #tag #anothertag
```

## Installation

```bash
make pip-compile
make pip-sync
```

## Usage

```bash
python3 olive.py sample.txt
```

## Testing

### Unit Tests

```bash
make pytest
```

### Style

```bash
make flake8
```
