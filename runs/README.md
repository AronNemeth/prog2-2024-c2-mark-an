# 2026-11-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.336167 |       1.00742  |   0.071393 |
| solution-1-flask   |     1.08272  |       1.05514  |   0.178429 |
| solution-pl        |     0.328075 |       0.130565 |   0.19056  |
| solution-aron-mark |     1.87693  |       0.13382  |   0.192622 |
| solution-1         |     6.09238  |       1e-06    |   0.433731 |
| solution-2         |     4.23842  |       0.454949 |   0.813747 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.332503 |       1.00744  |   0.165964 |
| solution-pl        |     0.326569 |       0.131376 |   0.28443  |
| solution-aron-mark |     0.326657 |       0.135046 |   0.289062 |
| solution-1-flask   |     0.347664 |       1.00788  |   0.54233  |
| solution-2         |     0.340037 |       0.41491  |   1.68255  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.336124 |       1.00758  |   0.727834 |
| solution-aron-mark |     0.356977 |       0.142803 |   0.818678 |
| solution-pl        |     0.330677 |       0.141689 |   0.826953 |
| solution-1-flask   |     0.335919 |       1.00778  |   4.17168  |
| solution-2         |     0.330064 |       0.449176 | 124.653    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.350777 |       0.170945 |    2.75622 |
| solution-aron-mark |     0.339208 |       0.175025 |    2.79465 |
| solution-flask     |     0.341325 |       1.00784  |    3.34748 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.344786 |       0.243752 |     16.277 |
| solution-aron-mark |     0.34173  |       0.314731 |     16.308 |