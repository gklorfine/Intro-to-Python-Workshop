# GK notes on statsmodels slides

- For consistency with earlier sections, each level 2 heading (`##`) should be a subset of a level 1 heading (`#`)
    + E.g., for statsmodels, all level 2 headings should be "statsmodels"

- Also for consistency: format package names (e.g., **statsmodels**) as bold instead of as `code`

- A lot of the slides have text cut off both width-wise and length-wise. Happy to help if you run into issues w/ formatting

- For the slide on group summaries, the tuples extend what I cover in the pandas section. For consistency (and for lower cognitive load), can you use the `.describe()` method here instead?

- What do you think about renaming `scores_df` to just `df`? I think it might make things a bit easier to read.
    + Maybe should rename to `data` to avoid confusion with df = DataFrame = degrees of freedom

- For slide on $t$-test interpretation, if we are touching on $p$-value definition we should just give the precise one

- Stats slides should surround all statistics (e.g, $p$ and $t$) with dollar signs (`$`) for italicization

- The first correlation scatterplot is not shown

- Looks good otherwise!

# General notes

- I will have to practice+time things but I think:
    + Day 1 (GK) can end with `for` loops
    + Day 2 (GK) can start w/ importing packages, defining functions; end with pandas
    + Day 3 (DL) starts with matplotlib.pyplot

# Day 1 --- Initial housekeeping

- Introduce selves
- Briefly show repository
- Show where to find final project, explain that this is meant to be done in parts after each session
- Tell everyone that after each session they should spend a bit of time looking the slides over, copy pasting the code, and playing around with it
- Take like 15 minutes max for installation issues before delving into content
    + Bora can help out 1-on-1 in a breakout room or through Zoom DMs for people with issues taking longer than this
- Stop at defining variables to see if people have issues printing `x` (verify installation)

