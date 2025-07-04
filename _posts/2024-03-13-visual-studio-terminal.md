
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
