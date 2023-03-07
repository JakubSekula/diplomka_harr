import os 

def augment():
    images = os.listdir('positive/img')
    for img in images:
        os.system("/opt/homebrew/opt/opencv@3/bin/opencv_createsamples -img positive/img/" + img + " -h 24 -w 24 -bg negative_scale_down_24_24/bg.txt -info positive/info.dat -num 10 -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -bgcolor 255 -vec positive/" + img + ".vec -te")

if __name__ == "__main__":
    augment()