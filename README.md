# msi-proj

**datasets.zip** - zbiory danych do nauki modelu (train.csv) oraz testowania(test.csv)  

**/imgs** - folder z przykładowo stworzonymi cyframi o rozmiarze 28 x 28 pikseli  

**metsi.py** - służy do wygenerowania modelu na podstawnie zadanego wzoru uczącego. Model zapisany jest w formacie .joblib  

Przed użyciem skryptu main.py należy wygenerować model wykozrystując metsi.py  

**main.py** - skrypt obsługiwany z linii komend poprzez argumenty  
arg1 - single/many  
arg2 - ścieżka do modelu  
arg2 - ścieżka do obrazu(dla single) lub pliku csv (dla many)  

Przykładowe użycie:  
> python main.py single model.joblib imgs/8.png  
> python main.py single model.joblib test.csv
