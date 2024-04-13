# 2024-04-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.728183 |       1.0094   |   0.066389 |
| solution-aron-mark |     0.688553 |       0.117283 |   0.173985 |
| solution-pl        |     5.9606   |       0.117156 |   0.177408 |
| solution-1-flask   |     1.4058   |       1.09064  |   0.271445 |
| solution-1         |     8.64071  |       1e-06    |   0.765561 |
| solution-2         |     0.691569 |       0.43832  |   0.809664 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.70003  |       1.00926  |   0.165214 |
| solution-pl        |     0.709607 |       0.125544 |   0.266092 |
| solution-aron-mark |     0.715455 |       0.125427 |   0.266797 |
| solution-1-flask   |     0.733003 |       1.00962  |   0.798772 |
| solution-2         |     0.717674 |       0.453592 |   3.24457  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.724586 |       1.00931  |   0.705095 |
| solution-pl        |     0.705595 |       0.132104 |   0.836542 |
| solution-aron-mark |     0.719737 |       0.131104 |   0.844657 |
| solution-1-flask   |     0.6999   |       1.0096   |   5.791    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.692389 |       1.00979  |    2.55761 |
| solution-aron-mark |     0.706775 |       0.16775  |    3.41339 |
| solution-pl        |     0.691536 |       0.169991 |    3.41923 |

## Inputs: 1000000, Queries 1000

| solution       |   setup_time |   preproc_time |   run_time |
|:---------------|-------------:|---------------:|-----------:|
| solution-flask |     0.702662 |        1.00941 |     18.366 |