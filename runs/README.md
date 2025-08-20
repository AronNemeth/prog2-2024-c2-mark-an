# 2025-08-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.35512  |       1.16877  |   0.099095 |
| solution-pl        |     0.481118 |       0.152633 |   0.237634 |
| solution-aron-mark |     4.40665  |       0.151458 |   0.23806  |
| solution-1-flask   |     0.482737 |       1.00837  |   0.262522 |
| solution-1         |     7.80926  |       1e-06    |   0.706125 |
| solution-2         |     0.475886 |       0.60815  |   1.52452  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.488465 |       0.155046 |   0.363068 |
| solution-aron-mark |     0.486039 |       0.155142 |   0.365635 |
| solution-flask     |     0.47972  |       1.00853  |   0.374984 |
| solution-1-flask   |     0.488736 |       1.00833  |   0.805502 |
| solution-2         |     0.48049  |       0.50498  |   3.30408  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.482868 |       0.160444 |    1.06875 |
| solution-aron-mark |     0.482302 |       0.16018  |    1.0694  |
| solution-flask     |     0.481462 |       1.00886  |    1.57285 |
| solution-1-flask   |     0.488838 |       1.00861  |    5.71472 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.482983 |       0.191403 |    3.21479 |
| solution-aron-mark |     0.482709 |       0.193949 |    3.25226 |
| solution-flask     |     0.487107 |       1.00845  |    5.04442 |