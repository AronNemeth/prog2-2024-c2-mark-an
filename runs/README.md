# 2025-07-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.63861  |       1.20993  |   0.102432 |
| solution-pl        |     0.497267 |       0.149103 |   0.234532 |
| solution-aron-mark |     4.44752  |       0.146979 |   0.235318 |
| solution-1-flask   |     0.498519 |       1.00845  |   0.263365 |
| solution-1         |     7.83116  |       1e-06    |   0.651453 |
| solution-2         |     0.49778  |       0.599771 |   0.93812  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.491446 |       0.149807 |   0.356385 |
| solution-aron-mark |     0.498932 |       0.150294 |   0.361662 |
| solution-flask     |     0.490796 |       1.00818  |   0.382278 |
| solution-1-flask   |     0.499369 |       1.00803  |   0.818863 |
| solution-2         |     0.493311 |       0.504483 |   2.3517   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.492657 |       0.155862 |    1.0698  |
| solution-aron-mark |     0.493837 |       0.15665  |    1.07726 |
| solution-flask     |     0.492357 |       1.00837  |    1.57563 |
| solution-1-flask   |     0.509373 |       1.00853  |    5.67858 |
| solution-2         |     0.494034 |       0.555939 |   39.0932  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.496129 |       0.190068 |    3.20226 |
| solution-pl        |     0.49844  |       0.186266 |    3.23323 |
| solution-flask     |     0.492625 |       1.00842  |    5.14129 |