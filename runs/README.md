# 2026-03-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.4925   |       1.0541   |   0.101814 |
| solution-aron-mark |     0.415973 |       0.146673 |   0.23236  |
| solution-pl        |     4.40126  |       0.14604  |   0.24052  |
| solution-1-flask   |     0.418049 |       1.00795  |   0.260097 |
| solution-1         |     9.2097   |       1e-06    |   0.739351 |
| solution-2         |     0.411394 |       0.668647 |   1.45898  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.418551 |       0.148794 |   0.3686   |
| solution-aron-mark |     0.419876 |       0.153465 |   0.372862 |
| solution-flask     |     0.41431  |       1.00828  |   0.390012 |
| solution-1-flask   |     0.432127 |       1.00843  |   0.801582 |
| solution-2         |     0.418001 |       0.510158 |   3.34481  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.420777 |       0.167691 |    1.12793 |
| solution-pl        |     0.418586 |       0.155217 |    1.13471 |
| solution-flask     |     0.435265 |       1.00914  |    1.61678 |
| solution-1-flask   |     0.421029 |       1.00865  |    5.68564 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.419979 |       0.195296 |    3.95563 |
| solution-aron-mark |     0.415557 |       0.17829  |    4.02299 |
| solution-flask     |     0.419461 |       1.00898  |    5.25821 |