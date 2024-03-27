# 2024-03-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.39036  |       1.06138  |   0.066028 |
| solution-pl        |     0.637748 |       0.11037  |   0.161391 |
| solution-aron-mark |     0.636011 |       0.108447 |   0.162757 |
| solution-1-flask   |     0.649969 |       1.00843  |   0.262403 |
| solution-1         |     8.06723  |       1e-06    |   0.783402 |
| solution-2         |     4.54905  |       0.459955 |   1.07847  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.647754 |       1.00842  |   0.168786 |
| solution-aron-mark |     0.640672 |       0.114185 |   0.254146 |
| solution-pl        |     0.640889 |       0.114683 |   0.255834 |
| solution-1-flask   |     0.648139 |       1.00868  |   0.809274 |
| solution-2         |     0.638643 |       0.448852 |   4.83118  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.641902 |       0.120764 |   0.816632 |
| solution-aron-mark |     0.641673 |       0.121814 |   0.820015 |
| solution-flask     |     0.632365 |       1.00868  |   0.918007 |
| solution-1-flask   |     0.652162 |       1.00848  |   5.58995  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.635641 |       0.153957 |    3.28993 |
| solution-aron-mark |     0.63225  |       0.153822 |    3.29536 |
| solution-flask     |     0.632696 |       1.00862  |    5.45969 |