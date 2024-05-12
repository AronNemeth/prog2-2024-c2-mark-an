# 2024-05-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.661106 |       1.00868  |   0.073784 |
| solution-pl        |     5.84952  |       0.13651  |   0.174288 |
| solution-aron-mark |     0.685006 |       0.118767 |   0.176143 |
| solution-1-flask   |     1.45576  |       1.06601  |   0.26706  |
| solution-1         |     8.08204  |       1e-06    |   0.709972 |
| solution-2         |     0.655665 |       0.430731 |   1.08645  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.663899 |       1.0089   |   0.159617 |
| solution-pl        |     0.678946 |       0.128745 |   0.271107 |
| solution-aron-mark |     0.69737  |       0.132126 |   0.274276 |
| solution-1-flask   |     0.68465  |       1.00909  |   0.802305 |
| solution-2         |     0.66999  |       0.439545 |   3.27796  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.678021 |       1.00892  |   0.690229 |
| solution-aron-mark |     0.67116  |       0.133408 |   0.819807 |
| solution-pl        |     0.670951 |       0.135724 |   0.823709 |
| solution-1-flask   |     0.680192 |       1.009    |   5.60899  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.668005 |       1.00925  |    2.46531 |
| solution-aron-mark |     0.659976 |       0.168246 |    2.61445 |
| solution-pl        |     0.672419 |       0.172032 |    2.62092 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.661606 |       1.00969  |    15.7982 |
| solution-aron-mark |     0.675761 |       0.291842 |    16.0771 |
| solution-pl        |     0.670351 |       0.287977 |    16.1427 |