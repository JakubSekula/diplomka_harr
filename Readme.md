# Co jsem zkousel ohledne harr classifier?

## Data
    Obrazky vzdy byly grayscale vyrezy uvnitr cervene oblasti

## Commandy
    /opt/homebrew/opt/opencv@3/bin/opencv_createsamples -vec positive_100/test.vec -info positive_100/info.txt -bgcolor 0 -num 100 -h 24 -w 24
    
    opencv_createsamples slouzi pro vytvoreni binarniho filu z pozitivnich obrazku

    /opt/homebrew/opt/opencv@3/bin/opencv_traincascade -h 24 -w 24 -data 100/ -vec positive_100/test.vec -bg negative_100/bg.txt -numPos 100 -numNeg 100

    opencv_traincascade slouzi pro samotny trenink

## Co vsechno bylo vyzkouseno?
Zkousel jsem ruzne kombinace vstupnich dat. Prvne jsem zkousel natrenovat klasifikator pro sikme strechy. Mel jsem 2500 obrazku sikmych strech a 150 negativnich (plochych strech) a 3000 negativnich obrazku z kaggle https://www.kaggle.com/datasets/muhammadkhalid/negative-images?resource=download. Natrenovany klasifikator nefungoval dobre, nektere pozitivni priklady nebyly detekovany a bylo detekovano neco i v negativnich (kde byly domy, nikoliv u tech z kaggle datasetu), ktere byly pouzity pri treninku. Parametry pro trenovani a create_samples jsem ruzne menil, pri -h 400 a -w 400 mi trenovani padalo. Pouzil jsem -h 24 -w 24 nicmene pri techto hodnotach klasifikator nefungoval nijak, respektive detekce probehla i v pozitivnich, ale taky v negativnich obrazcich strech. Zkousel jsem prokombinovat informace v pozitivnim filu, kde se specifikuje cesta k obrazku, pocet detekovanych objektu a jejich bounding box. Pri inferenci se ale delo to, ze se v obrazcich detekovalo vice objektu i presto, ze ve vsech pozitivnich byl prave jeden objekt pro detekci. Zkousel jsem upravovat taky parametr -bgcolor pri create_samples, nicmene pri vsech pokusech, ktere jsem provedl byl vysledek stejny a to, ze detekovane objekty byly nalezeny i v negativnich obrazcich pouzitych pri treninku. V pozitivnich souboru jsem se snazil menit velikost bounding boxu. A to bud 1 1 399 399, tedy plne velikosti obrazku, nebo 1 1 23 23.
I kdyz pri create_samples byly pouzity parametry -h 24 -w 24, tak ve vysledku to z obrazku vypadalo, ze se detekuje at uz v pozitivnich, nebo negativnich, oblast kolem budovy.


## Co je potreba jeste zkusit?
Data rucne oanotovat tak, aby velikost bounding boxu sedela presne kolem cerveneho vyrezu.

## Github
Pozor na cesty, v -bg souboru jsou vzdy moje lokalni absolutni cesty k obrazkum, je potreba zmenit. To same v notebooku.
https://github.com/JakubSekula/diplomka_harr
Obsahuje vsechna data a je mozne zde natrenovat klasifikator. Pozor ale, pri trenovani se specifikuje -data cesta k souboru, kde se uklada vysledek trenovani, tedy klasifikator.xml. Pri trenovani noveho je potreba mu dat novy soubor, pokud v souboru jsou jiz nejake starsi trenovaci data, tak nelze natrenovat.

## Jupyter notebook
Je zde notebook, pres ktery jsem zkousel vysledek natrenovani.
