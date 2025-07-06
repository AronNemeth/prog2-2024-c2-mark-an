# 2025-07-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.26154  |       1.03728  |   0.118683 |
| solution-pl        |     0.530216 |       0.155258 |   0.241155 |
| solution-aron-mark |     6.22417  |       0.156507 |   0.24649  |
| solution-1-flask   |     0.537603 |       1.00843  |   0.267417 |
| solution-1         |     8.04641  |       2e-06    |   0.677268 |
| solution-2         |     0.521005 |       0.660145 |   1.01422  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.514864 |       0.160435 |   0.367877 |
| solution-flask     |     0.518636 |       1.00868  |   0.381389 |
| solution-aron-mark |     0.5269   |       0.158085 |   0.435028 |
| solution-1-flask   |     0.540063 |       1.00837  |   0.803199 |
| solution-2         |     0.523524 |       0.557565 |   4.83557  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.529965 |       0.158341 |    1.08598 |
| solution-aron-mark |     0.519903 |       0.161661 |    1.08636 |
| solution-flask     |     0.516157 |       1.00856  |    1.60783 |
| solution-1-flask   |     0.53461  |       1.0087   |    5.88141 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.514613 |       0.192634 |    3.37753 |
| solution-aron-mark |     0.522647 |       0.194774 |    3.38895 |
| solution-flask     |     0.511528 |       1.00831  |    5.06068 |