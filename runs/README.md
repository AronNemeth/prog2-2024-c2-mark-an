# 2025-08-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.62446  |       1.05507  |   0.099871 |
| solution-pl        |     0.476204 |       0.153341 |   0.237096 |
| solution-aron-mark |     4.50128  |       0.149673 |   0.241144 |
| solution-1-flask   |     0.478892 |       1.00828  |   0.262325 |
| solution-1         |     7.4868   |       1e-06    |   0.627778 |
| solution-2         |     0.471079 |       0.600986 |   0.954293 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.478667 |       0.153682 |   0.370315 |
| solution-aron-mark |     0.477928 |       0.152044 |   0.371291 |
| solution-flask     |     0.477829 |       1.00839  |   0.374135 |
| solution-1-flask   |     0.483996 |       1.0083   |   0.78333  |
| solution-2         |     0.474896 |       0.496968 |   4.41535  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.474382 |       0.158672 |    1.08927 |
| solution-pl        |     0.479221 |       0.162345 |    1.10674 |
| solution-flask     |     0.475047 |       1.00842  |    1.57518 |
| solution-1-flask   |     0.494282 |       1.00848  |    5.73631 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.478775 |       0.190618 |    3.23225 |
| solution-aron-mark |     0.487367 |       0.19402  |    3.33115 |
| solution-flask     |     0.499471 |       1.00874  |    5.16691 |