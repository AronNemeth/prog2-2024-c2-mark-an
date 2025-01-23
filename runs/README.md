# 2025-01-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.1033   |       1.07289  |   0.08277  |
| solution-pl        |     4.64543  |       0.109813 |   0.175849 |
| solution-aron-mark |     0.540557 |       0.112183 |   0.179553 |
| solution-1-flask   |     0.535727 |       1.00857  |   0.277466 |
| solution-1         |     7.71164  |       1e-06    |   0.717408 |
| solution-2         |     0.523943 |       0.557187 |   1.09673  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.530122 |       0.11285  |   0.275903 |
| solution-aron-mark |     0.548327 |       0.113005 |   0.277065 |
| solution-flask     |     0.531309 |       1.00915  |   0.29735  |
| solution-1-flask   |     0.541918 |       1.00885  |   0.793086 |
| solution-2         |     0.527442 |       0.494455 |   8.39529  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.549155 |       0.123834 |   0.871615 |
| solution-pl        |     0.527066 |       0.120081 |   0.88417  |
| solution-flask     |     0.533218 |       1.00898  |   1.23447  |
| solution-1-flask   |     0.541391 |       1.00888  |   5.7378   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.539576 |       0.150305 |    2.85639 |
| solution-pl        |     0.54452  |       0.148481 |    2.88953 |
| solution-flask     |     0.554657 |       1.00913  |    4.42445 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.543551 |       0.260484 |    17.3477 |
| solution-aron-mark |     0.54289  |       0.257188 |    17.4388 |