---
layout: post
title: Visual Studio and Terminal cheatsheet
categories: cheatsheet
---

## Motivation

I am noticing physical strain on my right pinky finger. Navigating lines of code
is not ergonomic. I am discovering ways to distribute the amount of work done by
my pinky to the left hand.

Hence, I rely on shortcuts to accomplish efficiency and reduce pain. I have
listed both default and customized shortcuts that I am trying to master and
become embedded in my subconscious brain.

### VS Code customization

One may add customized keyboard shortcuts via `cmd-K`.

| Category         | Action                               | Shortcut               |
| ---------------- | ------------------------------------ | ---------------------- |
| **Practicing**   | Move Line Up/Down                    | `ctrl-opt-n/p`         |
|                  | Delete Word Right                    | `opt-d`, `ctrl-opt-h`  |
|                  | Cursor Page Up/Down                  | `ctrl-cmd-n/p`         |
|                  | Cursor Down Select                   | `ctrl-shift-n/p`       |
|                  | Delete Right                         | `opt-K`                |
|                  | Cursor Word End Right                | `opt-b`                |
|                  | Cursor Word End Left                 | `opt-h`                |
|                  | Delete All Left                      | `ctrl-shift-h`         |
|                  | Highlight Multiple Lines with Mouse  | `shift-opt-mouse-drag` |
|                  | Duplicate a Line                     | `opt-shift-↑/↓`        |
|                  | Highlight a Line                     | `cmd-l`                |
|                  | Remove Line Space Below              | `ctrl-j`               |
|                  | Copy a Line(s) Without Highlighting  | `cmd-c`                |
|                  | Multiple Cursors via Mouse           | `opt-mouse-click`      |
|                  | Move to the Previous Cursor Position | `cmd-u`                |
|                  | Multiple Lines Edit                  | `opt-shift-i`          |
| **Code Editing** | Navigate to Line Ends                | `ctrl-a`, `e`          |
|                  | Switch Lines                         | `opt-↑/↓`              |
|                  | Modify Identical Words               | `cmd-shift-l`          |
|                  | Remove Characters Left/Right         | `ctrl-h`, `ctrl-d`     |
|                  | Delete Line                          | `cmd-shift-K`          |
| **Running Code** | Execute Python Code                  | `fn-ctrl-5`            |
| **Navigation**   | Delete Text to the Right             | `ctrl-k`               |
|                  | Move Cursor by One Line              | `ctrl-p/n`             |
|                  | Browse Files                         | `cmd-p`                |
|                  | Browse Plugins                       | `cmd-shift-p`          |
|                  | Create New Panels                    | `cmd-1/2/3/4`          |
|                  | Duplicate Current Panel              | `ctrl-\`               |
|                  | Switch Panel Focus                   | `cmd-k-(→ or ←)`       |
|                  | Toggle Explorer                      | `cmd-b`                |
|                  | Find Across All Files                | `cmd-shift-f`          |
|                  | Navigate Tabs                        | `cmd-shift-]/[`        |
|                  | Go to a Specific Line                | `ctrl-G`               |
|                  | Word Wrap                            | `opt-Z`                |
| **Terminal**     | Toggle Terminal                      | `cmd-j`                |
| **Global**       | Replace Globally                     | `cmd-F12`              |

## Terminal

### Zip

`zip` combines files with compression. Use `zip` for cross-platform
compatibility.

```bash
`zipinfo directory.zip`
`zip -r directory.zip directory`
```

### Tar

`tar` combines files without compression. `tar` is primarily used in Unix/Linux
environments. It provides incremental backups.

To tar:

```bash
$ tar -cvf born-only.tar /jet/home/sleem/projects/20240218-AlOOH-BORN
$ tar -cvf born-only.tar
```

To untar:

```bash
$ tar -xvf born-only.tar
```

For `-cvf` `-c` instructs `tar` to create a new archive, `-v` enables the
verbose mode which displays the progress in the terminal, showing the files
being archived, and `-f` indicates the filename of the archive, which directly
follows this option.

`-xvf` extracts files from a tar archive using `-x` instead of `-c`.

### HPC

The following may not be useful for those who are not using the following HPC
platform.

#### Bridges

To make an interative session:

```bash
interact -n 64 -t 8:00:00
```

#### Module

```bash
module avail mkl
```

### Unix-like OS commands

####

```bash
which twine
```

#### Get folders size

```bash
du -h --max-depth=1 | sort -rh
```

The command `du -h --max-depth=1 | sort -rh` is used in Unix-like operating
systems to list directories and their sizes within the current directory.

- `du`: dist usage
- `-h`: human redable
- `--max-depth=1`: report one level below the current directory
- `sort`: sorts lines of tet
- `-r`: reverse order: largest items first
- `-h`: Sorts numbers with size suffixes (`K`, `M`, `G`)

#### Find file location

```bash
find /jet/home/sleem -name Snakefile
```

#### Use Grep to list files

To list files by searching for text patterns using regular expressions:

```bash
ls /opt/packages/oneapi/v2023.2.0/mkl/2023.2.0/lib/intel64 | grep libmkl_intel_lp64
libmkl_intel_lp64.a
libmkl_intel_lp64.so
libmkl_intel_lp64.so.2
```
