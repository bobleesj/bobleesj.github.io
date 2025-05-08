---
layout: post
title:
  How to generate elemental compositional features for compounds using CBFV for
  beginners
categories: tutorial
---

## Overview

By the end of this tutorial, you will be able to accomplish the following tasks

1. Generate features and save as `.csv` from compound chemical formulas
2. Use Code Editor to execute `.py`

## Motivation

Before we talk about how to run the code, it is important to understand the
philosophy of featurization projects. Each compound is made up of unique
elements, For example, LiO<sub>2</sub> is made up of Li and O atoms and each Li
and O has elemental properties such as radius, electronegativities, etc. How can
we, humans, characterize a.k.a featurize LiO<sub>2</sub>? We can attempt to add,
subtract, multiply these elemental properties to generate our unique “features”
or “descriptors” for the LiO<sub>2</sub> compound. This is illustrated with the
figure below.

![Image 1](/files/blog/2024-02-19-tutorial-CBFV/img/1.png)

One can write Python code to apply mathematical operations (combine, subtract,
multiply) to generate a set of features as a form of CSV files (the goal of this
tutorial) but we must first provide the database that contains the elemental
properties. Please see the Oliynyk database and Magpie below.

[Oliynyk](https://data.mendeley.com/datasets/bt6gv5z6yv/2)
[Magpie](https://github.com/Kaaiian/CBFV/blob/master/cbfv/element_properties/magpie.csv)

> Learn more about our paper on Oliynyk dataset here
> [https://doi.org/10.1016/j.dib.2024.110178](https://doi.org/10.1016/j.dib.2024.110178),
> a peer-reviewed dataset used in data-driven discovery since the mid-2010s.

## What is CBFV

CBFV is a Python script that garners various databases and we can choose one of
the databases to generate features for each compound. It does the mathematical
oeprations behind the scenes for us.

## Download code editor

![Image 4](/files/blog/2024-02-19-tutorial-CBFV/img/4.png)

We are now going to learn how to install and generate these features using CBFV.
For complete beginners, download Visual Studio, a "text" editor that helps read
and modify code easier. Download one here:
[https://code.visualstudio.com/](https://code.visualstudio.com/)

## Download CBFV

Download the Python CBFV folder from GitHub. Again, for complete beginners,
GitHub is analogous to Google Drive for programmers where you can easily track
file changes. Visit
[https://github.com/Kaaiian/CBFV](https://github.com/Kaaiian/CBFV), download the
ZIP file and unzip as shown below.

Drag the CBFV folder to the Visual Studio opening interface.
![Image 3](/files/blog/2024-02-19-tutorial-CBFV/img/3.png)

## Create `main.py`

Create a file called `main.py` or with a filename that ends with `.py` shown
below. Do not worry about other files that are scary looking at the moment. We
will not touch any of them.

<img src="/files/blog/2024-02-19-tutorial-CBFV/img/5.png"  style="max-width:40%; height:auto;">

## Find example compounds

In `main.py`, we are going to import a list of compounds that have been already
prepared by the developer. But where are the files?

Notice that if you go inside the “data” folder, there are many csv files. Try to
inspect them using Excel. I won’t cover why they are structured as
test/train/val but they are simply unique data divided into 3 categories. Each
CSV file contains compounds and “target values”. Think of the target value as a
number that represents a certain property. It could be a physical property, as
simple as melting point.

<img src="/files/blog/2024-02-19-tutorial-CBFV/img/6.png"  style="max-width:50%; height:auto;">

Each csv file contains compound formulas and the “target”. Using the compound
formula alone, we can generate features since we know their elements and we have
properties for each element from databases such as `magpie` and `oliynyk` as
discussed earlier.

<img src="/files/blog/2024-02-19-tutorial-CBFV/img/7.png"  style="max-width:40%; height:auto;">

In the main.py file, we are going to generate “features” for each compound. We
first need to import csv files. Let us use one provided in the data folder.

## Install Python libraries

One must install the following libraries to read csv files and use the CBFV
functions. Install those libraries in your command line tool with the following
command:

```python
pip install pandas CBFV
```

## Copy the following code to main.py

The code contains comments in which you can easily follow along. The code (1)
reads the CSV file, (2) prints the outputs, and (3) saves the files.

```python
from CBFV import composition
import pandas as pd

# Relative file path - go the data folder
csv_file = "data/ael_log10_debye_temperature/train.csv"

# Open up "Excel of Python" to read the CSV file.
dataframe = pd.read_csv(csv_file)

# Generate features
X, y, formulas, skipped = composition.generate_features(dataframe, elem_prop="magpie")

'''
X -> compositional features for each row (compound)
y -> target value (like melting point defined in csv_file)
'''

print("Features\n", X)
print("\nTarget/physical properties\n", y)
print("\nCompound formulas\n", formulas)
print("\nSkipped compounds\n", skipped)

# Save into CSV files to your local computer
X.to_csv("output_X_features.csv", index=False)
y.to_csv("output_y.csv", index=False)
formulas.to_csv("output_formulas.csv", index=False)
```

If you want to use other databases to generate features, you can simply do this!

```python
X, y, formulas, skipped = composition.generate_features(dataframe, elem_prop="oliynyk")
```

## Run main.py

To run the code, you can simply click on the play button.

![Image 8](/files/blog/2024-02-19-tutorial-CBFV/img/8.png)

If you do not see the play button, just go to “Extensions”, type “Python”, and
install Python.

![Image 9](/files/blog/2024-02-19-tutorial-CBFV/img/9.png)

## Check result

[output_formulas.csv](/files/blog/2024-02-19-tutorial-CBFV/source-code/output_formulas.csv)
|
[output_X_features.csv](/files/blog/2024-02-19-tutorial-CBFV/source-code/output_X_features.csv)

We are done. Take a look at `output_X_features.csv`. Notice features in the
columns are produced for each CIF compound found in `ouput_formulas.csv`.

![Image 10 - CVS ](/files/blog/2024-02-19-tutorial-CBFV/img/10.png)

## Source code

Here is the code that I used to generate CSV files. Simply run the `main.py`
script after you have installed all the dependencies mentioned earlier. Please
feel free to reach out if you have any questions or suggestions!

[Google Drive](https://drive.google.com/drive/folders/1QcMN87hN85iRwaGcS0N1UFtgCgkvieSs?usp=drive_link)
|
[Markdown](https://github.com/bobleesj/bobleesj.github.io/blob/main/_posts/2024-02-19-tutorial-CBFV.md)

### References

1. **CBFV:** S.K. Kauwe, J. Graser, A. Vazquez, T.D. Sparks (2024). Machine
   learning prediction of heat capacity for solid inorganics. _Integrating
   Materials and Manufacturing Innovation_ **7**, 43–51.
   [10.1007/s40192-018-0108-9](https://doi.org/10.1007/s40192-018-0108-9)

2. **Oliynyk dataset:** Lee, S., Chen, C., Garcia, G., Oliynyk, A. (2024).
   Machine learning descriptors in materials chemistry used in multiple
   experimentally validated studies: Oliynyk Elemental Property Dataset. _Data
   in Brief_, **53**, 110178.
   [https://doi.org/10.1016/j.dib.2024.110178](https://doi.org/10.1016/j.dib.2024.110178)

3. **Magpie dataset:** Ward, L., Agrawal, A., Choudhary, A., Wolverton, C.
   (2016). A general-purpose machine learning framework for predicting
   properties of inorganic materials. _npj Comput Mater_, **2**, 16028.
   [https://doi.org/10.1038/npjcompumats.2016.28](https://doi.org/10.1038/npjcompumats.2016.28)
