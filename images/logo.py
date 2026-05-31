# A script to generate the logo for the project, as displayed in the README.md file at the project's root.
# Along with documentation, I (GK) used these videos as resources: 
    # https://www.youtube.com/watch?v=kmA6P4vjuaI
    # https://www.youtube.com/watch?v=T8RXMRlRoRg&t=60s

import matplotlib.pyplot as plt
import matplotlib.patches as patches # For drawing shapes in matplotlib
import numpy as np

# Define figure, figure size
plt.figure(figsize = (8, 8))

# Create 'patch' (draw shape)
hex = patches.RegularPolygon(
    (0, 0), # Position (x, y)
    numVertices = 14, 
    radius = 1, 
    facecolor = '#1c3b24', edgecolor = 'white',
    linewidth = 6
)

# Add text
plt.annotate(
    "QMWS\nIntro to Python", (0, -.41), ha = "center", va = "center",
    color = "white", 
    fontsize = 54, fontfamily='signpainter'
)
plt.annotate(
    "Spring 2026", (0, -.83), ha = "center", va = "center",
    color = "white", 
    fontsize = 22, fontfamily='signpainter'
)

# gcf = 'get current figure'; gca = 'get current axes'
fig = plt.gcf()
ax = fig.gca()

ax.axis('off') # Turn off default matplotlib border

# Create an 'inset' plot (a plot within a plot) for a logo. 
# Use basic simulated data to make a basic line / scatterplot
np.random.seed(67) # Set random seed for reproducibility
point_n = 10
point_x = np.linspace(1, 10, point_n)
point_error = np.random.normal(0, 3, point_n)
point_y = point_x + point_error

line_n = 100
line_x = np.linspace(1, 10, line_n)
line_y = line_x

axin = ax.inset_axes([.3446, .5109, 0.3261, 0.3261]) # This creates the inset graph; args: [x, y, width, height]
axin.plot(point_x, point_y, 'wo', markersize = 5.4) # Plot points
axin.plot(line_x, line_y, '-', color = "turquoise", linewidth = 4.3) # Plot line
axin.tick_params(bottom = False, left = False, labelbottom = False, labelleft = False) # Remove ticks
axin.spines[['top', 'right']].set_visible(False) # Remove top and right spines (borders)
axin.spines[['bottom', 'left']].set_color('white') # Colour bottom and left spines to white
axin.spines[['bottom', 'left']].set_linewidth(2.15) # Set bottom and left spine linewidth

# Add 'patch' to figure
ax.add_patch(hex)

# Set figure limits
plt.xlim([-1.15,1.15])
plt.ylim([-1.15,1.15])

# Save figure w/ transparent background
plt.savefig('images/logo.png', dpi = 300, transparent = True, bbox_inches = 'tight', pad_inches = 0.05)

plt.show()