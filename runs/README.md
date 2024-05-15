# 2024-05-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.58139  |       1.20629  |   0.10431  |
| solution-pl        |     0.695995 |       0.125827 |   0.18499  |
| solution-aron-mark |     6.51948  |       0.129657 |   0.186703 |
| solution-1-flask   |     0.715679 |       1.00911  |   0.266251 |
| solution-2         |     0.689173 |       0.453497 |   0.971904 |
| solution-1         |     9.07239  |       1e-06    |   0.980978 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.706245 |       1.00962  |   0.156713 |
| solution-aron-mark |     0.70115  |       0.133408 |   0.274476 |
| solution-pl        |     0.726554 |       0.135524 |   0.285118 |
| solution-1-flask   |     0.717534 |       1.00924  |   0.82032  |
| solution-2         |     0.702721 |       0.467236 |   6.01129  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.693376 |       1.00927  |   0.716123 |
| solution-pl        |     0.708096 |       0.137066 |   0.813485 |
| solution-aron-mark |     0.724276 |       0.138572 |   0.815339 |
| solution-1-flask   |     0.725165 |       1.00989  |   5.7518   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.685382 |       1.00921  |    2.58301 |
| solution-pl        |     0.692307 |       0.171392 |    2.67907 |
| solution-aron-mark |     0.697619 |       0.175454 |    2.75895 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.711487 |       0.296441 |    16.6124 |
| solution-pl        |     0.683758 |       0.295661 |    16.8114 |
| solution-flask     |     0.675581 |       1.00921  |    16.9958 |