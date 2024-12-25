# 2024-12-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.93748  |       1.00855  |   0.10236  |
| solution-aron-mark |     0.532618 |       0.109748 |   0.185231 |
| solution-pl        |     0.524221 |       0.110098 |   0.186461 |
| solution-1-flask   |     4.90704  |       1.05702  |   0.261501 |
| solution-1         |     7.53366  |       1e-06    |   0.579861 |
| solution-2         |     0.527894 |       0.485863 |   1.19529  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.534789 |       0.111819 |   0.314433 |
| solution-pl        |     0.527784 |       0.111298 |   0.316825 |
| solution-flask     |     0.527539 |       1.00885  |   0.477946 |
| solution-1-flask   |     0.529416 |       1.00852  |   0.811085 |
| solution-2         |     0.525639 |       0.496828 |   3.75944  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.529547 |       0.1171   |    1.0698  |
| solution-aron-mark |     0.533196 |       0.117247 |    1.11965 |
| solution-flask     |     0.529888 |       1.00907  |    2.16517 |
| solution-1-flask   |     0.535177 |       1.00912  |    5.85039 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.531874 |       0.146968 |    4.30489 |
| solution-aron-mark |     0.527025 |       0.144813 |    4.31184 |
| solution-flask     |     0.524456 |       1.0093   |    8.42909 |