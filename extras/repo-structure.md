# Repository Structure

As the [`README.md`](../README.md) (the "landing page" document) was becoming rather long, I (GK) thought less important information regarding the repository structure (e.g., what the different files are for, what folders they are under, etc.) was better placed into a separate file (this one!).

Below is a **directory tree** of this repository:

<!-- GK: Will need to update this -->

``` text
.
├── extras
│   ├── fun
│   │   ├── assets
│   │   │   ├── controller.png
│   │   │   ├── game-bg.png
│   │   │   ├── jump.wav
│   │   │   ├── player.png
│   │   │   ├── py-logo.png
│   │   │   ├── win-img.png
│   │   │   └── win-sound.wav
│   │   ├── game.py
│   │   └── README.md
│   ├── pip-install.md
│   └── repo-structure.md
├── images
│   ├── condaMac.png
│   ├── condaWindows.png
│   ├── df-csv.png
│   ├── extensions.png
│   ├── logo.png
│   ├── logo.py
|   └── paste-1.png
├── optional-exercises
│   ├── solutions
│   │   ├── day1-solutions.ipynb
|   |   ├── day2-solutions.ipynb
│   │   └── day3-solutions.ipynb
│   ├── day1-exercises.ipynb
│   ├── day2-exercises.ipynb
│   └── day3-exercises.ipynb
├── pandas
│   └── df.csv
├── project
│   ├── itp-project.ipynb
|   └── stroke-data.csv
├── q-and-a
│   ├── day1-attendee-q-and-a.ipynb
│   ├── day2-attendee-q-and-a.ipynb
|   └── day3-attendee-q-and-a.ipynb
├── _quarto.yml
├── .gitignore
├── day1-slides.pdf
├── day1-slides.qmd
├── day2-slides.pdf
├── day2-slides.qmd
├── day3-slides.pdf
├── day3-slides.qmd
├── LICENSE
└── README.md
```

With the exception of the [`LICENSE`](../LICENSE) file, items without a file extension (e.g., `.py`, `.md`, etc.) are folders. Indented branches off a folder indicate that folder's contents.

## Root

Starting at the **root** of the repository (i.e., the top-level/outermost folder; in this case, the place where the slides are contained), we have:

- The slide files, `day*-slides.*`
    + "`*`" is shorthand for "everything" (or "all possible combinations" in this case)
- The [`README.md`](../README.md) file, which is the document you see at the "homepage" of the repository
- The [`_quarto.yml`](../_quarto.yml) file is a configuration file for Quarto (the software used to create the slides)
- The [`.gitignore`](../.gitignore) file tells our computers (mine (GK) and Bora's) which files not to upload when we update the repository
- The [`LICENSE`](../LICENSE) file for legal stuff (explains how others are allowed to use/copy/modify/share the workshop)
    + Fairly standard on GitHub

## Folders

### [`q-and-a/`](../q-and-a)

- Contains answers to attendee questions that were particularly insightful and/or beyond the scope of this workshop.
    + Day 1 Q&A: [`day1-attendee-q-and-a.ipynb`](../q-and-a/day1-attendee-q-and-a.ipynb)
    + Day 2 Q&A: [`day2-attendee-q-and-a.ipynb`](../q-and-a/day2-attendee-q-and-a.ipynb)
    + Day 3 Q&A: [`day3-attendee-q-and-a.ipynb`](../q-and-a/day3-attendee-q-and-a.ipynb)

### [`project/`](../project)

- Contains the project to be completed for a digital credential ([`itp-project.ipynb`](../project/itp-project.ipynb))
- Also contains the dataset for the project ([`stroke-data.csv`](../project/stroke-data.csv))

### [`pandas/`](../pandas)

- Contains a dataset created during the day 2 slideshow ([`df.csv`](../pandas/df.csv))
    + See [`day2-slides.pdf`](../day2-slides.pdf) for context

### [`optional-exercises/`](../optional-exercises)

- Contains optional exercises for each day's content that should be used for practice. If we have time at the end of a given session, we can go over some of these together.
    + [`day1-exercises.ipynb`](../optional-exercises/day1-exercises.ipynb)
    + [`day2-exercises.ipynb`](../optional-exercises/day2-exercises.ipynb)
    + [`day3-exercises.ipynb`](../optional-exercises/day3-exercises.ipynb)

#### [`optional-exercises/solutions/`](../optional-exercises/solutions)

- Contains solutions to the optional exercises
    + [`day1-solutions.ipynb`](../optional-exercises/solutions/day1-solutions.ipynb)
    + [`day2-solutions.ipynb`](../optional-exercises/solutions/day2-solutions.ipynb)
    + [`day3-solutions.ipynb`](../optional-exercises/solutions/day3-solutions.ipynb)

### [`images/`](../images)

- Contains images used in the slides and optional exercises (e.g., [`df-csv.png`](../images/df-csv.png))
    + See [`day2-slides.pdf`](../day2-slides.pdf) for context
- Also contains the code and image for the logo used in the [`README.md`](../README.md) file
    + See [`logo.py`](../images/logo.py) for the code 
    + See [`logo.png`](../images/logo.png) for the image

### [`extras/`](../extras)

- The folder you are in now!
- Contains supplementary materials/resources for the workshop and beyond
    + [`pip-install.md`](../extras/pip-install.md) contains instructions for installing Python packages using `pip` (a package manager for Python)
    + This file!

#### [`extras/fun/`](../extras/fun)

- Contains a game I (GK) created using the package ***pygame-ce*** ([`game.py`](../extras/fun/game.py))
- See the [`extras/fun/README.md`](../extras/fun/README.md) file for instructions on how to run the game

##### [`extras/fun/assets/`](../extras/fun/assets)

- Assets for [`game.py`](../extras/fun/game.py) (i.e., images and sounds used)