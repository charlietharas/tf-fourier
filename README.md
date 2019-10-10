# tf-fourier
Using FFT algorithm to show frequency/amplitude distribution of wav files in a music-visualizer fashion.

## plans for v0.4
- proper log system
- 3D graphing (just add lists to bigger list & then create beta compare function)
- improved visualization?

## v0.3.1 10/9/19
Channel in FFT switched and FFT_PlotCompare created to visualize the difference between different channels. This improves visualization greatly!

## v0.3 10/4/19 - MAJOR UPDATE
- stream reading: reads chunk of file placed in folder
- visibly real-time visualizes audio files on matplotlib
- significantly improved code structure

## v0.2.1 10/4/19
Update so that all systems now use the same filepath string relative to the current directory. Not major code update but of great help for efficiency.

## v0.2 10/3/19
FFT application now works on visualization of clipped .wav files, but fails to work on /cut folder.
Proper unlabeled visualization is good (axis is long but can be easily fixed).

## v0.1 ORIGIN
Application only plots direct data from wav file, nonfunctional.
Transferred to all devices for increased productivity (new branches).
