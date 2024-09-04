# 2024-09-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.29377  |       1.11502  |   0.092635 |
| solution-pl        |     0.549384 |       0.103831 |   0.170852 |
| solution-aron-mark |     5.99391  |       0.103158 |   0.189317 |
| solution-1-flask   |     0.553882 |       1.00918  |   0.255445 |
| solution-1         |     7.88499  |       1e-06    |   0.724571 |
| solution-2         |     0.542253 |       0.623981 |   1.11631  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.556631 |       1.00888  |   0.220104 |
| solution-pl        |     0.551583 |       0.103613 |   0.287958 |
| solution-aron-mark |     0.550348 |       0.10373  |   0.298059 |
| solution-1-flask   |     0.553944 |       1.00898  |   0.770945 |
| solution-2         |     0.556912 |       0.476714 |   8.12486  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.557189 |       1.00939  |   0.95686  |
| solution-pl        |     0.562836 |       0.111844 |   0.981873 |
| solution-aron-mark |     0.551877 |       0.11422  |   0.986558 |
| solution-1-flask   |     0.592753 |       1.00883  |   5.64599  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.567791 |       1.00988  |    4.16047 |
| solution-pl        |     0.552585 |       0.144449 |    4.22026 |
| solution-aron-mark |     0.560253 |       0.144899 |    4.36533 |