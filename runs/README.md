# 2024-12-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.78968  |       1.00872  |   0.103738 |
| solution-pl        |     0.52871  |       0.110449 |   0.186418 |
| solution-aron-mark |     0.537032 |       0.110696 |   0.189372 |
| solution-1-flask   |     5.16276  |       1.10598  |   0.266929 |
| solution-1         |     7.5442   |       1e-06    |   0.591769 |
| solution-2         |     0.534114 |       0.545693 |   0.829411 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.533627 |       0.110476 |   0.318289 |
| solution-pl        |     0.543453 |       0.112327 |   0.31941  |
| solution-flask     |     0.531339 |       1.00891  |   0.483081 |
| solution-1-flask   |     0.542237 |       1.00904  |   0.81264  |
| solution-2         |     0.539226 |       0.507229 |   5.20511  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.538929 |       0.117304 |    1.08368 |
| solution-pl        |     0.541587 |       0.11909  |    1.10307 |
| solution-flask     |     0.541441 |       1.00887  |    2.14441 |
| solution-1-flask   |     0.54543  |       1.00883  |    5.91002 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.536001 |       0.14483  |    4.55393 |
| solution-pl        |     0.555727 |       0.148421 |    4.64563 |
| solution-flask     |     0.53826  |       1.00865  |    8.63615 |