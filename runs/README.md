# 2024-06-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.67006  |       1.00943  |   0.076277 |
| solution-pl        |     0.671936 |       0.106235 |   0.165584 |
| solution-aron-mark |     6.30786  |       0.1052   |   0.166003 |
| solution-1-flask   |     1.54598  |       1.05633  |   0.265954 |
| solution-1         |     8.10189  |       1e-06    |   0.620521 |
| solution-2         |     0.669178 |       0.526218 |   0.896791 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.663517 |       1.00915  |   0.163554 |
| solution-pl        |     0.670285 |       0.106278 |   0.262793 |
| solution-aron-mark |     0.681519 |       0.107312 |   0.273375 |
| solution-1-flask   |     0.681531 |       1.00908  |   0.781172 |
| solution-2         |     0.683814 |       0.486801 |   2.70173  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.667362 |       1.00895  |   0.711891 |
| solution-pl        |     0.676372 |       0.114471 |   0.803584 |
| solution-aron-mark |     0.686077 |       0.114059 |   0.805155 |
| solution-1-flask   |     0.687483 |       1.00893  |   5.43593  |
| solution-2         |     0.675859 |       0.525388 |  35.8668   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.669435 |       1.00899  |    2.52525 |
| solution-pl        |     0.680305 |       0.149585 |    2.62954 |
| solution-aron-mark |     0.669645 |       0.14924  |    2.63431 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.663943 |       1.00902  |    16.0255 |
| solution-pl        |     0.667663 |       0.27629  |    22.2141 |
| solution-aron-mark |     0.67594  |       0.281331 |    22.4703 |