# 2025-12-04

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.75886  |       1.06739  |   0.100407 |
| solution-aron-mark |     0.471915 |       0.157836 |   0.240898 |
| solution-pl        |     0.47033  |       0.15871  |   0.245865 |
| solution-1-flask   |     0.473131 |       1.00817  |   0.269378 |
| solution-1         |    10.0147   |       1e-06    |   0.762304 |
| solution-2         |     4.6756   |       0.703011 |   1.11992  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.504425 |       1.0084   |   0.368373 |
| solution-aron-mark |     0.468259 |       0.159996 |   0.372243 |
| solution-pl        |     0.467459 |       0.163346 |   0.375362 |
| solution-1-flask   |     0.47493  |       1.00831  |   0.796354 |
| solution-2         |     0.471579 |       0.501199 |   6.79452  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.467994 |       0.16572  |    1.08516 |
| solution-aron-mark |     0.471276 |       0.165738 |    1.08706 |
| solution-flask     |     0.471857 |       1.0086   |    1.57174 |
| solution-1-flask   |     0.475208 |       1.0085   |    5.51239 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.475987 |       0.194458 |    3.24496 |
| solution-pl        |     0.488189 |       0.194203 |    3.27317 |
| solution-flask     |     0.488246 |       1.00845  |    5.04322 |