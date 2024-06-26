# 2024-06-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.67476  |       1.00862  |   0.076285 |
| solution-aron-mark |     6.06965  |       0.10255  |   0.161047 |
| solution-pl        |     0.661144 |       0.104518 |   0.162894 |
| solution-1-flask   |     1.42365  |       1.01177  |   0.254536 |
| solution-1         |     7.9848   |       1e-06    |   0.584136 |
| solution-2         |     0.662092 |       0.4931   |   1.19548  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.672906 |       1.00904  |   0.161475 |
| solution-aron-mark |     0.671935 |       0.106494 |   0.255567 |
| solution-pl        |     0.669793 |       0.10588  |   0.257846 |
| solution-1-flask   |     0.687871 |       1.00879  |   0.77786  |
| solution-2         |     0.675431 |       0.471434 |   2.26408  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.674078 |       1.0089   |   0.703208 |
| solution-aron-mark |     0.673926 |       0.113086 |   0.800373 |
| solution-pl        |     0.669682 |       0.113105 |   0.803035 |
| solution-1-flask   |     0.686394 |       1.0086   |   5.45944  |
| solution-2         |     0.671382 |       0.545248 |  36.3908   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.671405 |       1.00927  |    2.51748 |
| solution-aron-mark |     0.6729   |       0.151903 |    2.6067  |
| solution-pl        |     0.678451 |       0.150171 |    2.61814 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.672039 |       1.00909  |    16.2608 |
| solution-pl        |     0.669653 |       0.283853 |    20.9748 |
| solution-aron-mark |     0.6743   |       0.28109  |    21.4274 |