---
layout: post
title: Best practices for mathematical typesetting (Ft. MathJax and LaTeX)
categories: cheatsheet
---

## Motivation

MathJax is used to write mathematical equations on the current website with simple commands within a Markdown file. It renders LaTeX code as a PNG file.

I will primarily use the following content as a reference to aid my writing and setup. Since MathJax and LaTeX keywords can be found online, I will focus on best practices and example snippets.

## Installation

Add the following script tag to your `head.html`. See my `head.html` file [here](https://github.com/bobleesj/bobleesj.github.io/blob/main/_includes/head.html).

```js
<script
  type="text/javascript"
  id="MathJax-script"
  async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"
></script>
```

## General tips

### 1. Start with `\begin` to number automatically

Start with `\begin{align}` for aligning multiple equations or `\begin{equation}` for a single equation to provide a number for each equation. Examples are in the the following section.

### 2. Indentation

It is generally a good practice to indent at the `&=` sign and also to indent after `\begin`.

MathJax code:

```md
\begin{align}
a &= b + c \\
&= d + e
\end{align}
```

MathJax code:

```md
\begin{equation}
[\sigma] =
\begin{bmatrix}
\sigma*{11} & \sigma*{12} & \sigma*{13} \\ % Row 1
\sigma*{21} & \sigma*{22} & \sigma*{23} \\ % Row 2
\sigma*{31} & \sigma*{32} & \sigma\_{33} % Row 3
\end{bmatrix}
\end{equation}
```

### 3. Add comments using `%`

We have a preview for both LaTeX and Markdown files. Comments are not needed if the documentation itself provides enough context for the equation. However, they can be useful for two reasons.

First, we may add remarks without making them explicitly available in the output, especially when the document is in draft form. Second, we may use `%` to strategically navigate and modify the equations.

To help navigate within the equation:

```md
\begin{bmatrix}
\sigma*{11} & \sigma*{12} & \sigma*{13} \\ % Row 1
\sigma*{21} & \sigma*{22} & \sigma*{23} \\ % Row 2
\sigma*{31} & \sigma*{32} & \sigma\_{33} % Row 3
\end{bmatrix}
```

To comment out parts of the document:

```md
% The following will be restored once we have...
% \begin{equation}
% ...
% \end{equation}
```

### 4.Avoid using fixed `()` or `[]` without `\left` or `\right` modifiers

We do not want to used a fixed `()` or `[]` without using `left` or `\right` comments.

Using `\left` and `\right`

$$
\begin{align}
  c &= \left(\frac{a}{b}\right) \quad \text{} \\
  c &= (\frac{a}{b}) \quad \text{:(}
\end{align}
$$

MathJax code:

```md
\begin{align}
c &= \left(\frac{a}{b}\right) \\
c &= (\frac{a}{b})
\end{align}
```

### 5. Use proper notation

$$
\begin{align}
  & \sin(x) \quad \log(y) \quad \ln(x)  \\
  & sin(x) \quad log(y) \quad ln(x) \quad \text{:(}
\end{align}
$$

Notice that function names are not italicized if properly formatted.

MathJax code:

```md
\begin{align}
& \sin(x) \quad \log(y) \quad \ln(x) \\
& sin(x) \quad log(y) \quad ln(x)
\end{align}
```

### 6. Distinguish between vectors and matrices

Generally, a bold lowercase letter is used for vectors, while a capitalized non-bold letter is used for matrices.

$$
\begin{align}
  \mathbf{v} &= \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix} \\
  M &= \begin{bmatrix}
    m_{11} & m_{12} \\
    m_{21} & m_{22}
  \end{bmatrix}
\end{align}
$$

### 7. Use correct `\begin` setup

| Environment | Description                                                                                                                                                        |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `align`     | align multiple equations at the `&` symbol. Each line is numbered by default.                                                                                      |
| `align*`    | same as `align`, no line numbering.                                                                                                                                |
| `aligned`   | This is a sub-environment used within another environment like `equation` to align multiple lines, similar to `align`, but without creating a new equation number. |
| `equation*` | same as `equation`, no line numbering.                                                                                                                             |
| `gather`    | center multiple equations without aligning them to a particular symbol. Each line is numbered.                                                                     |
| `gather*`   | same as `gather` but with no line numbering.                                                                                                                       |
| `gathered`  | a sub-environment used within another environment, like `equation`, to center multiple lines                                                                       |
| `alignat`   | Allows for the alignment of multiple equations, similar to `align`, but gives you control over the spacing between the columns of alignment.                       |
| `alignat*`  | Same as `alignat` but without equation numbering.                                                                                                                  |

#### Example 1. `aligned` within `equation`

Align with a single line number.

$$
\begin{equation}
  \begin{aligned}
    a + b + c &= d \\
    a + c &= h
  \end{aligned}
\end{equation}
$$

MathJax code:

```md
\begin{equation}
\begin{aligned}
a + b + c &= d \\
e + f + g &= h
\end{aligned}
\end{equation}
```

#### Example 2. `gather*`

Center without line numbering.

$$
\begin{gather*}
  x^2 + y^2 = r^2 \\
  e^{i\pi} + 1 = 0 \\
  y = mx + c
\end{gather*}
$$

MathJax code:

```md
\begin{gather*}
x^2 + y^2 = r^2 \\
e^{i\pi} + 1 = 0 \\
y = mx + c
\end{gather*}
```

#### Example 3. `gather`

Center with line numbering for each equation.

MathJax code:

$$
\begin{gather}
  x^2 + y^2 = r^2 \\
  e^{i\pi} + 1 = 0 \\
  y = mx + c
\end{gather}
$$

MathJax code:

```md
\begin{gather}
x^2 + y^2 = r^2 \\
e^{i\pi} + 1 = 0 \\
y = mx + c
\end{gather}
```

#### Example 4. `equation` with `gathered`

Center with only one line numbering.

$$
\begin{equation}
  \begin{gathered}
    x^2 + y^2 = r^2 \\
    e^{i\pi} + 1 = 0 \\
    y = mx + c
  \end{gathered}
\end{equation}
$$

MathJax code:

```md
\begin{equation}
\begin{gathered}
x^2 + y^2 = r^2 \\
e^{i\pi} + 1 = 0 \\
y = mx + c
\end{gathered}
\end{equation}
```

## Final remarks

I will update the document with templates and best practices.
