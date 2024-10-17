# 2024-10-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.56015  |       1.0786   |   0.095829 |
| solution-aron-mark |     0.55331  |       0.1022   |   0.171271 |
| solution-pl        |     5.83118  |       0.104035 |   0.186324 |
| solution-1-flask   |     0.576614 |       1.00962  |   0.257987 |
| solution-1         |     8.24093  |       1e-06    |   0.589006 |
| solution-2         |     0.551989 |       0.491879 |   1.14918  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.555761 |       1.00923  |   0.229377 |
| solution-pl        |     0.557309 |       0.104217 |   0.29107  |
| solution-aron-mark |     0.561089 |       0.103805 |   0.295434 |
| solution-1-flask   |     0.585001 |       1.00954  |   0.763405 |
| solution-2         |     0.55665  |       0.4732   |   5.45309  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.554733 |       1.00919  |   0.886874 |
| solution-aron-mark |     0.556108 |       0.112996 |   1.00012  |
| solution-pl        |     0.555163 |       0.112973 |   1.0329   |
| solution-1-flask   |     0.562029 |       1.00928  |   5.40858  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.557252 |       1.0095   |    4.22077 |
| solution-pl        |     0.558215 |       0.144952 |    4.32378 |
| solution-aron-mark |     0.563985 |       0.147083 |    4.3311  |