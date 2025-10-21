# 2025-10-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.54326  |       1.12678  |   0.101337 |
| solution-aron-mark |     0.486998 |       0.156893 |   0.239738 |
| solution-pl        |     0.487132 |       0.154169 |   0.248094 |
| solution-1-flask   |     0.486018 |       1.00827  |   0.266667 |
| solution-1         |     7.95244  |       1e-06    |   0.704268 |
| solution-2         |     4.81142  |       0.718349 |   0.838805 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.489489 |       0.158943 |   0.365815 |
| solution-pl        |     0.483555 |       0.156748 |   0.368172 |
| solution-flask     |     0.506905 |       1.00817  |   0.375594 |
| solution-1-flask   |     0.486923 |       1.00828  |   0.795258 |
| solution-2         |     0.48598  |       0.506075 |   2.29906  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.484371 |       0.175332 |    1.06089 |
| solution-pl        |     0.497378 |       0.164364 |    1.07359 |
| solution-flask     |     0.484766 |       1.00875  |    1.56471 |
| solution-1-flask   |     0.492576 |       1.0086   |    5.62004 |
| solution-2         |     0.48408  |       0.560587 |  159.435   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.489811 |       0.195435 |    3.30412 |
| solution-pl        |     0.498647 |       0.195101 |    3.31153 |
| solution-flask     |     0.492006 |       1.00843  |    5.1409  |