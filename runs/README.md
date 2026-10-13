# 2026-10-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.53444  |       1.11151  |   0.111844 |
| solution-1-flask   |     0.360684 |       1.00681  |   0.11647  |
| solution-aron-mark |     4.97652  |       0.137975 |   0.140168 |
| solution-pl        |     0.745631 |       0.10176  |   0.141102 |
| solution-1         |     5.33282  |       0        |   0.440697 |
| solution-2         |     0.74767  |       0.539897 |   0.510535 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.247561 |       1.00665  |   0.099814 |
| solution-aron-mark |     0.249104 |       0.09963  |   0.193213 |
| solution-pl        |     0.250319 |       0.102782 |   0.195404 |
| solution-1-flask   |     0.253608 |       1.00664  |   0.355869 |
| solution-2         |     0.252529 |       0.311574 |   1.4649   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.259059 |       1.00675  |   0.441086 |
| solution-aron-mark |     0.24874  |       0.107094 |   0.521919 |
| solution-pl        |     0.250151 |       0.103612 |   0.522824 |
| solution-1-flask   |     0.247662 |       1.00657  |   2.76843  |
| solution-2         |     0.249202 |       0.349219 |  19.4928   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.247917 |       0.121913 |    1.74671 |
| solution-aron-mark |     0.249849 |       0.124193 |    1.753   |
| solution-flask     |     0.258919 |       1.00713  |    2.08915 |
| solution-1-flask   |     0.251339 |       1.00683  |   23.7688  |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.252972 |       0.170721 |    12.3903 |
| solution-aron-mark |     0.259026 |       0.170821 |    12.5726 |
| solution-flask     |     0.251967 |       1.00695  |    15.5086 |