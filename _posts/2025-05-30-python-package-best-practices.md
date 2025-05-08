---
layout: post
title: Python package distribution best practices and writing guide
categories: cheatsheet
---

## Motivation

We write software by writing lines of code. Software development requires unique
algorithms and brainstorming. In the end, those mere ideas and dreams are
materialized through the keyboards and alphabets we press on the keyboard. We
want to express the algorithms, ideas, and unique points through the alphabetics
that we use.

### 1. Write commands

> This code counts the number of atoms in a supercell. (Ok)

> Counts the number of atoms in a supercell. (Better)

> Count the number of atoms in a supercell. (Best)

A source code documentation is as an instruction manual, not an encyclopedia.
Users want clear action steps.

### 2. Every word matters

Use the minimum number of words without losing information. It means choosing
the correct and precious nouns and verbs. Always avoid ambigous and
colloquaislism.

> Find the number of atoms in a formula. (Ok)

> Count unique atoms in a formula. (Better)

> Count unique elements in a formula. (Best)

Replace "find the number" with "count". While "atoms" could be interpreted as
individual particles, "elements" refers to the types of atoms.

Language matters. Precision and clarity save time, the most important resource.

```text
"Find the distance between two atoms"
"Compute the bond distance between two atoms"
"Compute the Euclidean distance between two Cartesian coordinates"
```

### 3. Use dependency control

### 4. Include paths
