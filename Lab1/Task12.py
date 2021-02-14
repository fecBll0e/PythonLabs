def get_frames(size, overlap):
    signal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    size = size * overlap
    start = 0
    end = int(size)

    while end <= len(signal):
        frame = signal[start:end]
        yield frame
        start += int(size)
        end += int(size)
        
for frame in get_frames (size=10, overlap=0.5):
        print(frame)