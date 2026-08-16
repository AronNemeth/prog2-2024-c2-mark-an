# 2026-08-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.82585  |       1.0904   |   0.106694 |
| solution-pl        |     0.433341 |       0.15447  |   0.239655 |
| solution-aron-mark |     5.10441  |       0.150371 |   0.243841 |
| solution-1-flask   |     0.635143 |       1.00831  |   0.272696 |
| solution-1         |     8.37159  |       1e-06    |   0.6797   |
| solution-2         |     0.427392 |       0.730739 |   1.19216  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.429401 |       0.152875 |   0.371254 |
| solution-aron-mark |     0.433564 |       0.152716 |   0.372937 |
| solution-flask     |     0.470101 |       1.00851  |   0.381926 |
| solution-1-flask   |     0.440999 |       1.00855  |   0.791109 |
| solution-2         |     0.432875 |       0.515443 |  25.0379   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.434684 |       0.158164 |    1.12287 |
| solution-aron-mark |     0.439969 |       0.162415 |    1.12956 |
| solution-flask     |     0.447337 |       1.00842  |    1.65646 |
| solution-1-flask   |     0.442986 |       1.00852  |    5.8423  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.438961 |       0.181819 |    3.6195  |
| solution-pl        |     0.434427 |       0.184504 |    3.66548 |
| solution-flask     |     0.43341  |       1.00911  |    5.43951 |