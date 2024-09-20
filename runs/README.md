# 2024-09-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.17073  |       1.15393  |   0.081059 |
| solution-pl        |     0.551136 |       0.100397 |   0.176036 |
| solution-aron-mark |     1.7911   |       0.100608 |   0.18227  |
| solution-1-flask   |     0.562455 |       1.00828  |   0.268426 |
| solution-1         |     7.47403  |       1e-06    |   0.581647 |
| solution-2         |     4.3493   |       0.494192 |   0.747527 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.551004 |       1.00809  |   0.203774 |
| solution-pl        |     0.553746 |       0.101778 |   0.301151 |
| solution-aron-mark |     0.551665 |       0.103375 |   0.309909 |
| solution-1-flask   |     0.559096 |       1.00787  |   0.802813 |
| solution-2         |     0.563471 |       0.477044 |   7.59298  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.550506 |       1.00828  |   0.928555 |
| solution-aron-mark |     0.554357 |       0.110293 |   1.0359   |
| solution-pl        |     0.551246 |       0.109751 |   1.04376  |
| solution-1-flask   |     0.554939 |       1.01406  |   5.45179  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.563789 |       1.00858  |    3.98534 |
| solution-aron-mark |     0.550378 |       0.137845 |    4.10858 |
| solution-pl        |     0.552328 |       0.137138 |    4.23064 |