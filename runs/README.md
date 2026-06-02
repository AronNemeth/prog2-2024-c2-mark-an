# 2026-06-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.45896  |       1.04645  |   0.078076 |
| solution-pl        |     0.337088 |       0.118991 |   0.178348 |
| solution-1-flask   |     0.33274  |       1.00713  |   0.178836 |
| solution-aron-mark |     0.336556 |       0.140141 |   0.187745 |
| solution-1         |     7.02153  |       1e-06    |   0.463629 |
| solution-2         |     4.53585  |       0.588273 |   0.61849  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.337091 |       0.118529 |   0.271654 |
| solution-pl        |     0.346834 |       0.120656 |   0.28696  |
| solution-flask     |     0.331656 |       1.00713  |   0.312666 |
| solution-1-flask   |     0.349058 |       1.00723  |   0.545214 |
| solution-2         |     0.333711 |       0.404867 |   3.44563  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.335619 |       0.12351  |   0.797908 |
| solution-pl        |     0.334707 |       0.123013 |   0.800809 |
| solution-flask     |     0.333157 |       1.00717  |   1.26395  |
| solution-1-flask   |     0.33914  |       1.00727  |   4.2839   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.329685 |       0.144488 |    2.95546 |
| solution-aron-mark |     0.330131 |       0.143338 |    2.96044 |
| solution-flask     |     0.333962 |       1.00731  |    4.04381 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.334843 |       0.204715 |    15.521  |
| solution-pl        |     0.329544 |       0.206118 |    15.5543 |