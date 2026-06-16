# A Brief Guide to Installing Packages Outside the Anaconda Navigator

- When following this guide, you might encounter errors specific to your system. It is recommended that you copy+paste these errors into an AI tool, along with a prompt such as "While trying to install package **x**, I used command **y** and got the following error: [error goes here!]"

1. Open up your terminal (MacOS, Linux) or command prompt / powershell (Windows)
1. Run `conda env list` to list your Conda environments
    + Let's say that there is one called `workshop` for the following examples
1. Run `conda activate workshop` to activate the `workshop` environment (replace `workshop` with the environment of your choosing)
1. Run `pip install packageName` to install a package into your environment
    + If `pip` itself is not installed (it might be by default, so skip this step if you did not get an error), run `conda install pip`