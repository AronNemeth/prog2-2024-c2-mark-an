# 2024-12-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.11332  |       1.04991  |   0.114883 |
| solution-aron-mark |     0.568678 |       0.114301 |   0.188552 |
| solution-pl        |     5.75721  |       0.109206 |   0.195217 |
| solution-1-flask   |     0.572876 |       1.00941  |   0.271015 |
| solution-1         |     7.57679  |       1e-06    |   0.679862 |
| solution-2         |     0.567354 |       0.551431 |   1.04269  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.576568 |       0.110478 |   0.306446 |
| solution-aron-mark |     0.574498 |       0.111033 |   0.331733 |
| solution-flask     |     0.569664 |       1.00907  |   0.508381 |
| solution-1-flask   |     0.57944  |       1.00966  |   0.770138 |
| solution-2         |     0.573574 |       0.484592 |   2.65751  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.567966 |       0.116787 |    1.03515 |
| solution-aron-mark |     0.571391 |       0.119403 |    1.0361  |
| solution-flask     |     0.570817 |       1.0093   |    2.25166 |
| solution-1-flask   |     0.573159 |       1.00879  |    5.44718 |
| solution-2         |     0.573779 |       0.584023 |   26.4631  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.562577 |       0.146295 |    4.39169 |
| solution-pl        |     0.563517 |       0.153051 |    4.42761 |
| solution-flask     |     0.568781 |       1.00898  |    8.74038 |