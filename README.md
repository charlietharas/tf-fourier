# tf-fourier
Using FFT algorithm to show frequency/amplitude distribution of wav files in a music-visualizer fashion.

## language reroll
Update to use Octave Matlab, versioning logs ditched, will be updating on full functional release.

Disregard below.

## plans for v0.3
- proper log system for console
- visualization of shorter files
- seamless continuous visualization (stream reading?)
- visualization of overall files using matplotlib's contour functions

## v0.2.1 10/4/19
Update so that all systems now use the same filepath string relative to the current directory. Not major code update but of great help for efficiency.

## v0.2 10/3/19
FFT application now works on visualization of clipped .wav files, but fails to work on /cut folder.
Proper unlabeled visualization is good (axis is long but can be easily fixed).

## v0.1 ORIGIN
Application only plots direct data from wav file, nonfunctional.
Transferred to all devices for increased productivity (new branches).
