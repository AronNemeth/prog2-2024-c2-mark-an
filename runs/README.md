# 2024-10-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.1551   |       1.05853  |   0.078992 |
| solution-aron-mark |     0.585695 |       0.103037 |   0.173719 |
| solution-pl        |     5.81153  |       0.105932 |   0.184757 |
| solution-1-flask   |     0.588757 |       1.00897  |   0.262375 |
| solution-1         |     7.85759  |       1e-06    |   0.679077 |
| solution-2         |     0.577488 |       0.605367 |   0.825482 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.580373 |       1.0089   |   0.19542  |
| solution-aron-mark |     0.582485 |       0.108803 |   0.293313 |
| solution-pl        |     0.575736 |       0.104512 |   0.295351 |
| solution-1-flask   |     0.586937 |       1.00911  |   0.799613 |
| solution-2         |     0.562787 |       0.48973  |   2.811    |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.58272  |       1.00916  |   0.889307 |
| solution-aron-mark |     0.583585 |       0.116638 |   0.988443 |
| solution-pl        |     0.584737 |       0.116064 |   1.01393  |
| solution-1-flask   |     0.606667 |       1.00921  |   5.59384  |
| solution-2         |     0.589846 |       0.565405 |  27.3598   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.59552  |       1.00924  |    4.56751 |
| solution-pl        |     0.564367 |       0.1471   |    4.76457 |
| solution-aron-mark |     0.60262  |       0.150542 |    4.90429 |