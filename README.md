
# Doccano Inter-Annotator Agreement

In short, it connects automatically to a Doccano server - also accepts json files as input -, to checks Data Quality before training a Machine Learning model.

## How to use

```
git clone https://github.com/vwoloszyn/diaa/
pip install requirements.txt
python main.py  -u http://doccano_host [user] [password] [project_number]



* Instance-based F1 agreement

## Project Setup

* 2 annotators: 4, 5
* 24 agreement documents
* 5 labels

## Agreement per Document

| Document   |   Mean F1 |   SD F1 |
|------------|-----------|---------|
| 17.ann     |     0.000 |   0.000 |
| 5.ann      |     0.000 |   0.000 |
| 0.ann      |     0.400 |   0.000 |
| 18.ann     |     0.345 |   0.000 |
| 8.ann      |     0.400 |   0.000 |


## Agreement per Label

|   Label |   Mean F1 |   SD F1 |
|---------|-----------|---------|
|      22 |     0.625 |   0.000 |
|      19 |     0.000 |   0.000 |
|      20 |     0.111 |   0.000 |
|      21 |     0.204 |   0.000 |
|      23 |     0.260 |   0.000 |

## Overall Agreement

* Mean F1: 0.233, SD F1: 0.000

```
