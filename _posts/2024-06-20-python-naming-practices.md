---
layout: post
title: Python naming best practices
categories: tutorial
---

## Motivation

Automation tools such as MyPy
([tutorial](https://bobleesj.github.io/python/2024/06/04/python-static-type-checking.html))
and Black
([tutorial](https://bobleesj.github.io/tutorial/2024/03/11/python-styling-guide.html))
may help with formatting, but naming is created by us. It is in our best
interest to apply the clear, descriptive, and concise (CDC) principle and use
community practices.

### Project-level

- A pip package should be a single word, all lowercase, e.g., `numpy`, `pandas`,
  `cifkit`.

### Folder level

- Overall, names should be specific as well as concise, e.g., `auth` for
  authentication modules, `admin` for administration.

- For folders containing countable similar functions, use plural forms and
  `lowercase_with_underscore`, e.g., `models`, `utils`, `image_utils`.

### File level

- Use `lowercase_with_underscore` for file names. If the file is contained
  within a folder such as `user`, use `profile_handler.py` instead of
  `user_profile_handler.py`.

### Script-level

- For classes, use `CamelCase`, e.g., `MyClass`.
- For functions and variables, use `lowercase_with_underscore`, e.g.,
  `get_atom_label`.
- For constants, use `UPPERCASE`,e.g., `PI`, `INVALID_TYPE_ERROR`.

### Naming dabate

Software for science often contains names that are long. In my code, I have a
set of variables that compute the minimum, maximum, and average coordination
numbers within a class. These variables are primarily used by the end-users.

```
# Naming method 1
CN_min, CN_max, CN_avg

# Naming method 2
max_CN, min_CN, avg_CN
```

I choose Method 2. The first method starts with `CN_`, which allows the user to
identify that this is related to the coordination number. In practice, when we
speak, we say "maximum coordination number" instead of "coordination number
maximum". Therefore, it is more natural from a behavioral point of view.

### Common mistakes

- Using non-standardized abbreviations: One might choose to write `min` for
  `minimum` and `std` for `standard deviation`.
- Using words that conflict with Python keywords: Avoid names like `list`,
  `str`, `dict`.
- Using long words without purpose: For example, `users_with_access_to_database`
  can be `authorized_users`, and `number_of_items` can be `item_count`.
- Using general names: Names such as `data`, `info`, or `my_string` do not
  provide context.

### Last remarks

Software is developed using the English language. Writing is an art that
requires both skills and intuition. Just like learning to ride a bicycle for the
first time, we need to learn from experience, as it is not possible to gain the
same insights solely from books and knowledge.

### References

- https://peps.python.org/pep-0008/#naming-conventions
- https://github.com/pandas-dev/pandas/tree/main/pandas/core
