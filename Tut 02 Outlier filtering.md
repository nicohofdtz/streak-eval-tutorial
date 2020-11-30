## Outlier filtering

The outlier iterates over all cells of the data. The value of each cell is compared to its environment. The environment is defined as the *window_size* columns and rows around the cell. A *window_size*=2 (default) leads to an environment of 24 cells.
If the value of the cell deviates more than *stdev_factor* (default=4) from the mean of the environment, it is overwritten by the mean. Negative pixels are treated as outliers, too.
The filter function is designed to filter single pixel outliers but leave larger artifacts (like dead spots on CCD, see example) untouched.

Below is a comparison of uncorrected and corrected data. Here the deviating pixels were set to 5000 to make them stand out by their deep red color.
![Full image uncorrected]("https://github.com/nicohofdtz/streak-eval-tutorial/blob/uncorrected")
![Fullimage corrected]("https://github.com/nicohofdtz/streak-eval-tutorial/blob/corrected")

Here's a zoomed in image on a dead spot on a CCD. As desired, it is left untouched by the outlier filtering, except for two pixels in ST1 that were negative (white).
![Dead spot uncorrected]("https://github.com/nicohofdtz/streak-eval-tutorial/blob/zoom_uncorrected")
![Dead spot corrected]("https://github.com/nicohofdtz/streak-eval-tutorial/blob/zoom_corrected")