import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 32)

extracted_colors_rgb = []
for x in range(len(colors)):
    rgb_tuple = (colors[x].rgb.r, colors[x].rgb.g, colors[x].rgb.b)
    extracted_colors_rgb.append(rgb_tuple)

print(extracted_colors_rgb)
