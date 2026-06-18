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