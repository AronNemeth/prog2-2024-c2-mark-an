# 2025-09-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.474028 |       1.00805  |   0.098921 |
| solution-pl        |     5.65785  |       0.416225 |   0.234198 |
| solution-aron-mark |     0.467846 |       0.149534 |   0.23842  |
| solution-1-flask   |     1.05261  |       1.05604  |   0.270573 |
| solution-1         |     7.75841  |       1e-06    |   0.727753 |
| solution-2         |     0.476768 |       0.675448 |   0.813654 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.476822 |       0.154554 |   0.358719 |
| solution-aron-mark |     0.476798 |       0.152284 |   0.359278 |
| solution-flask     |     0.476111 |       1.0082   |   0.380984 |
| solution-1-flask   |     0.483425 |       1.00823  |   0.804068 |
| solution-2         |     0.475954 |       0.494538 |  17.0019   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.476293 |       0.158644 |    1.05991 |
| solution-pl        |     0.475539 |       0.159898 |    1.06062 |
| solution-flask     |     0.473926 |       1.00814  |    1.55169 |
| solution-1-flask   |     0.484116 |       1.00826  |    5.62498 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.475354 |       0.188834 |    3.18493 |
| solution-pl        |     0.474683 |       0.189656 |    3.1881  |
| solution-flask     |     0.481017 |       1.00805  |    5.0257  |