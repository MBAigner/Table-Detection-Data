# Table Detection Data
Provided scripts for deriving training and testing data for table detection tasks.

The data which was intially used can be requested under https://doc-analysis.github.io/.
The data has to be stored in the folder
/data/tablebank/Detection_data.

The following scripts are provided:

* ```TableBankGTParsing.py``` retrieves URLs stored in the TableBank data and converts them into CSV. Additionally, the ground-truth is re-formatted into a .csv.
* ```WordData.ipynb```  and  ```TableBankWord.py``` are checking the accessibility of World URLs.
* ```TableBankWord2PDF.ipynb``` converts retrieved Word files into PDF documents.
