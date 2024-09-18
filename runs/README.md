# 2024-09-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.72818  |       1.08531  |   0.082786 |
| solution-aron-mark |     1.86572  |       0.101666 |   0.174768 |
| solution-pl        |     0.542814 |       0.102174 |   0.175084 |
| solution-1-flask   |     0.551765 |       1.00799  |   0.263188 |
| solution-1         |     7.55882  |       1e-06    |   0.58278  |
| solution-2         |     4.49162  |       0.500371 |   1.0198   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.548851 |       1.00817  |   0.22069  |
| solution-pl        |     0.551522 |       0.103412 |   0.302085 |
| solution-aron-mark |     0.549156 |       0.102301 |   0.302366 |
| solution-1-flask   |     0.579435 |       1.00834  |   0.776134 |
| solution-2         |     0.545593 |       0.473143 |   3.59407  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.545799 |       1.00822  |   0.911897 |
| solution-pl        |     0.551731 |       0.148528 |   1.01655  |
| solution-aron-mark |     0.544318 |       0.108961 |   1.02621  |
| solution-1-flask   |     0.554718 |       1.00834  |   5.43407  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.55632  |       1.00829  |    4.10322 |
| solution-pl        |     0.554621 |       0.139252 |    4.2156  |
| solution-aron-mark |     0.562836 |       0.136143 |    4.23677 |