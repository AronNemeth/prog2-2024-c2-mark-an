# 2025-10-08

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.56012  |       1.14701  |   0.099394 |
| solution-aron-mark |     0.480267 |       0.161369 |   0.234501 |
| solution-pl        |     0.487834 |       0.156919 |   0.244885 |
| solution-1-flask   |     0.486831 |       1.00828  |   0.26393  |
| solution-1         |     7.4531   |       1e-06    |   0.708528 |
| solution-2         |     4.40302  |       0.669508 |   1.41037  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.485425 |       0.157629 |   0.363036 |
| solution-pl        |     0.502966 |       0.164992 |   0.373608 |
| solution-flask     |     0.482023 |       1.00849  |   0.375408 |
| solution-1-flask   |     0.492321 |       1.00873  |   0.804764 |
| solution-2         |     0.4776   |       0.502883 |   3.14874  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.48268  |       0.163895 |    1.06041 |
| solution-aron-mark |     0.48513  |       0.169078 |    1.10136 |
| solution-flask     |     0.499181 |       1.00844  |    1.62277 |
| solution-1-flask   |     0.49008  |       1.0084   |    5.65583 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.484759 |       0.193392 |    3.2371  |
| solution-pl        |     0.486266 |       0.195985 |    3.28715 |
| solution-flask     |     0.48832  |       1.00824  |    5.04703 |