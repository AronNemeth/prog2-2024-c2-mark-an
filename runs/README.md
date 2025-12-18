# 2025-12-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.46645  |       1.04679  |   0.098886 |
| solution-aron-mark |     0.467131 |       0.159628 |   0.243531 |
| solution-pl        |     0.466087 |       0.160126 |   0.244771 |
| solution-1-flask   |     0.471012 |       1.00831  |   0.263793 |
| solution-1         |     7.43924  |       1e-06    |   0.60445  |
| solution-2         |     4.44706  |       0.570337 |   0.944448 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.465712 |       0.161692 |   0.363234 |
| solution-aron-mark |     0.472736 |       0.165196 |   0.365686 |
| solution-flask     |     0.470248 |       1.00837  |   0.369074 |
| solution-1-flask   |     0.469187 |       1.00818  |   0.790712 |
| solution-2         |     0.460373 |       0.502285 |   4.74503  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.466239 |       0.166963 |    1.066   |
| solution-aron-mark |     0.467442 |       0.16763  |    1.06967 |
| solution-flask     |     0.465291 |       1.00837  |    1.55221 |
| solution-1-flask   |     0.46863  |       1.0088   |    5.54205 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.481792 |       0.191032 |    3.46667 |
| solution-aron-mark |     0.471784 |       0.193295 |    3.46965 |
| solution-flask     |     0.464951 |       1.0083   |    5.06325 |