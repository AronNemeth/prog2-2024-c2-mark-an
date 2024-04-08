# 2024-04-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.657936 |       1.00902  |   0.065948 |
| solution-aron-mark |     0.658623 |       0.109283 |   0.165474 |
| solution-pl        |     5.76298  |       0.111448 |   0.166094 |
| solution-1-flask   |     1.30766  |       1.19271  |   0.260302 |
| solution-1         |     7.89468  |       1e-06    |   0.861331 |
| solution-2         |     0.678945 |       0.419824 |   1.31784  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.664737 |       1.00897  |   0.173969 |
| solution-aron-mark |     0.663721 |       0.116096 |   0.256875 |
| solution-pl        |     0.663937 |       0.115903 |   0.260757 |
| solution-1-flask   |     0.66934  |       1.00902  |   0.78256  |
| solution-2         |     0.657829 |       0.431296 |   2.58737  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.661555 |       0.121433 |   0.814168 |
| solution-pl        |     0.66627  |       0.122386 |   0.820251 |
| solution-flask     |     0.66284  |       1.00893  |   0.924034 |
| solution-1-flask   |     0.677298 |       1.00905  |   5.59065  |
| solution-2         |     0.682499 |       0.487905 | 311.909    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.663434 |       0.15779  |    3.26113 |
| solution-pl        |     0.662662 |       0.156876 |    3.32966 |
| solution-flask     |     0.662843 |       1.00941  |    5.32735 |