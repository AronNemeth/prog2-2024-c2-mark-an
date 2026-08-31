# 2026-08-31

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     4.63623  |       1.04843  |   0.07763  |
| solution-1-flask   |     0.826241 |       1.00742  |   0.176319 |
| solution-pl        |     0.468192 |       0.123865 |   0.1828   |
| solution-aron-mark |     4.85861  |       0.177019 |   0.189068 |
| solution-1         |     8.18717  |       1e-06    |   0.522672 |
| solution-2         |     0.333771 |       0.511975 |   0.875342 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.336788 |       0.141873 |   0.281122 |
| solution-aron-mark |     0.34334  |       0.141801 |   0.287504 |
| solution-flask     |     0.334415 |       1.00734  |   0.302623 |
| solution-1-flask   |     0.345265 |       1.00751  |   0.554277 |
| solution-2         |     0.33279  |       0.40176  |   3.5918   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.333315 |       0.128844 |   0.814716 |
| solution-aron-mark |     0.337573 |       0.158902 |   0.8224   |
| solution-flask     |     0.335353 |       1.00763  |   1.28347  |
| solution-1-flask   |     0.345245 |       1.01008  |   4.4107   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.35434  |       0.158408 |    2.79789 |
| solution-aron-mark |     0.341907 |       0.184213 |    2.8606  |
| solution-flask     |     0.331478 |       1.00762  |    4.08322 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.337728 |       0.286108 |    15.8723 |
| solution-pl        |     0.335324 |       0.279369 |    15.9516 |