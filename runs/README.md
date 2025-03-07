# 2025-03-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.532624 |       1.00871  |   0.080125 |
| solution-pl        |     0.533641 |       0.141674 |   0.205468 |
| solution-aron-mark |     1.82565  |       0.152231 |   0.206666 |
| solution-1-flask   |     5.24227  |       1.08789  |   0.263073 |
| solution-1         |     7.70275  |       1e-06    |   0.640218 |
| solution-2         |     0.535177 |       0.62151  |   0.726435 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.532063 |       1.00953  |   0.303821 |
| solution-aron-mark |     0.537289 |       0.144349 |   0.307121 |
| solution-pl        |     0.547984 |       0.143996 |   0.308161 |
| solution-1-flask   |     0.58213  |       1.0094   |   0.80165  |
| solution-2         |     0.53451  |       0.504405 |   4.99961  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.542952 |       0.151799 |   0.900563 |
| solution-aron-mark |     0.537043 |       0.150631 |   0.918156 |
| solution-flask     |     0.54448  |       1.00882  |   1.23449  |
| solution-1-flask   |     0.545376 |       1.00872  |   5.63924  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.535106 |       0.180385 |    2.84488 |
| solution-aron-mark |     0.542789 |       0.182174 |    2.86514 |
| solution-flask     |     0.541146 |       1.0088   |    4.20773 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.536544 |       0.276029 |    16.6602 |
| solution-pl        |     0.537503 |       0.284666 |    17.1665 |