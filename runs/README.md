# 2024-07-28

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.501691 |       1.00886  |   0.07559  |
| solution-pl        |     5.84425  |       0.102882 |   0.171873 |
| solution-aron-mark |     0.502579 |       0.123594 |   0.190022 |
| solution-1-flask   |     1.35012  |       1.04644  |   0.262116 |
| solution-1         |     8.10396  |       1e-06    |   0.603803 |
| solution-2         |     0.497168 |       0.525055 |   0.973105 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.49415  |       1.00933  |   0.223114 |
| solution-pl        |     0.499534 |       0.103927 |   0.281625 |
| solution-aron-mark |     0.501002 |       0.103961 |   0.289192 |
| solution-1-flask   |     0.505302 |       1.00907  |   0.769608 |
| solution-2         |     0.498682 |       0.473935 |  13.8263   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.506766 |       1.00919  |   0.956684 |
| solution-aron-mark |     0.506799 |       0.112014 |   0.994305 |
| solution-pl        |     0.496467 |       0.112565 |   1.0426   |
| solution-1-flask   |     0.503398 |       1.00923  |   5.5216   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.497284 |       1.00923  |    4.17587 |
| solution-aron-mark |     0.517926 |       0.147689 |    4.27395 |
| solution-pl        |     0.501065 |       0.147011 |    4.28348 |