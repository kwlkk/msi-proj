# msi-proj

**datasets.zip** - zbiory danych do nauki modelu (train.csv) oraz testowania(test.csv)  

**/imgs** - folder z przykładowo stworzonymi cyframi o rozmiarze 28 x 28 pikseli  

**metsi.py** - służy do wygenerowania modelu na podstawnie zadanego wzoru uczącego. Zapisany jest w formacie .joblib  

**main.py** - skrypt obsługiwany z linii komend poprzez argumenty  
arg1 - single/many  
arg2 - ścieżka do modelu  
arg2 - ścieżka do obrazu(dla single) lub pliku csv (dla many)  

Przykładowe użycie:  
> python main.py single model.joblib 8.png  
