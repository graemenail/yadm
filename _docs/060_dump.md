---
title: "Dump"
permalink: /docs/dump
---
There are components in some setups that do not have a dotfile. They instead offer a method to reproduce their state. In this workflow, this process is a complementary operation to bootstrapping. For example, Homebrew users may wish to write their installed formulas into a `.Brewfile`.

yadm provides a standard command to perform these operations.

```bash
yadm dump
```

This command will execute the program named `$HOME/.config/yadm/dump`. You should
provide this program yourself, and it must be made executable. After running this command, you should add the affected files to your repository in the usual way.


## Examples

### Dump installed [Homebrew](https://brew.sh/) formulas

```bash
#!/bin/sh
brew bundle dump -f --file=.Brewfile
```

### Track installed [Atom](https://atom.io/) packages

```bash
#!/bin/sh
apm list --installed --bare > .atom_packages
```
