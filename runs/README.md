# 2025-07-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.50228  |       1.06441  |   0.118665 |
| solution-aron-mark |     6.17603  |       0.165324 |   0.241446 |
| solution-pl        |     0.51776  |       0.156627 |   0.242365 |
| solution-1-flask   |     0.529442 |       1.009    |   0.26655  |
| solution-1         |     8.29956  |       2e-06    |   0.695744 |
| solution-2         |     0.554539 |       0.644052 |   1.42932  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.54972  |       0.158547 |   0.381027 |
| solution-flask     |     0.523236 |       1.00841  |   0.382305 |
| solution-aron-mark |     0.519908 |       0.158037 |   0.396999 |
| solution-1-flask   |     0.517617 |       1.00831  |   0.815998 |
| solution-2         |     0.52319  |       0.543492 |   8.15296  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.49592  |       0.159087 |    1.08008 |
| solution-aron-mark |     0.49837  |       0.156287 |    1.09054 |
| solution-flask     |     0.499027 |       1.00864  |    1.58564 |
| solution-1-flask   |     0.512378 |       1.00849  |    5.9192  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.515337 |       0.186221 |    3.3165  |
| solution-aron-mark |     0.526534 |       0.195956 |    3.36705 |
| solution-flask     |     0.504493 |       1.00854  |    5.12829 |