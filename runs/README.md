# 2026-11-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.297358 |       1.00818  |   0.047107 |
| solution-aron-mark |     2.94131  |       0.117583 |   0.160777 |
| solution-pl        |     0.791721 |       0.11632  |   0.161486 |
| solution-1-flask   |     2.40307  |       1.04573  |   0.163841 |
| solution-1         |     7.21905  |       1e-06    |   0.394793 |
| solution-2         |     4.62991  |       0.378508 |   0.505868 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.298024 |       1.00792  |   0.127394 |
| solution-aron-mark |     0.302602 |       0.117364 |   0.219901 |
| solution-pl        |     0.300596 |       0.119058 |   0.227091 |
| solution-1-flask   |     0.302923 |       1.00813  |   0.519789 |
| solution-2         |     0.293994 |       0.361085 |   1.6471   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.301142 |       1.00811  |   0.676419 |
| solution-pl        |     0.305294 |       0.125936 |   0.712662 |
| solution-aron-mark |     0.301271 |       0.127298 |   0.726279 |
| solution-1-flask   |     0.301986 |       1.00842  |   3.99548  |
| solution-2         |     0.300981 |       0.405244 | 127.219    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.300404 |       0.150636 |    3.2057  |
| solution-pl        |     0.301342 |       0.150907 |    3.22444 |
| solution-flask     |     0.300122 |       1.00819  |    3.4244  |