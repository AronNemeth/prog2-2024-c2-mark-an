# 2025-02-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.521714 |       1.00938  |   0.077918 |
| solution-pl        |     1.68065  |       0.149745 |   0.203671 |
| solution-aron-mark |     0.529691 |       0.138101 |   0.204404 |
| solution-1-flask   |     4.7999   |       1.06129  |   0.259664 |
| solution-1         |     7.00279  |       1e-06    |   0.587915 |
| solution-2         |     0.525716 |       0.525065 |   1.46747  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.532075 |       1.00896  |   0.291883 |
| solution-aron-mark |     0.524277 |       0.141932 |   0.307709 |
| solution-pl        |     0.537307 |       0.144307 |   0.308577 |
| solution-1-flask   |     0.53318  |       1.00883  |   0.803314 |
| solution-2         |     0.52613  |       0.496201 |   3.52575  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.525944 |       0.15097  |   0.905349 |
| solution-aron-mark |     0.526752 |       0.147243 |   0.922654 |
| solution-flask     |     0.523463 |       1.00903  |   1.23045  |
| solution-1-flask   |     0.535898 |       1.0091   |   5.76792  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.52827  |       0.176787 |    2.82255 |
| solution-pl        |     0.528022 |       0.190189 |    2.83834 |
| solution-flask     |     0.525702 |       1.00892  |    4.27946 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.525227 |       0.277972 |    16.5674 |
| solution-aron-mark |     0.528015 |       0.279494 |    16.5722 |