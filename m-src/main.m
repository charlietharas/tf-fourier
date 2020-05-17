# NOTE MUST USE SAMPLING RATE
# somethings wrong but ill get to it
fileName = 'allthistime_1s.wav';
step=1;
[Y, FS] = audioread(fileName);
FS
twentymstime = FS/50
for step=1:audioinfo(fileName).TotalSamples
    step += twentymstime;
    audiowrite('allthistime_cut.wav', Y(step-twentymstime:step), FS);
    [data, bitrateFFS] = audioread('allthistime_cut.wav');
    dataFFT = fftshift(data);
    plot(abs(dataFFT(:,1)));
    step
endfor;

#[data, fs] = audioread(fileName);
#data_fft = fftshift(data);
#plot(abs(data_fft(:,1)));

clf()
