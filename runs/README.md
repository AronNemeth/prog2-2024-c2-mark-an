# 2024-03-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.59078  |       1.03599  |   0.066969 |
| solution-aron-mark |     0.662181 |       0.108225 |   0.164537 |
| solution-pl        |     0.668581 |       0.110508 |   0.164893 |
| solution-1-flask   |     0.674013 |       1.00854  |   0.265199 |
| solution-1         |     8.40059  |       1e-06    |   0.822701 |
| solution-2         |     4.66392  |       0.552811 |   0.847221 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.6532   |       1.00861  |   0.170975 |
| solution-pl        |     0.667857 |       0.11506  |   0.25521  |
| solution-aron-mark |     0.67138  |       0.115605 |   0.256572 |
| solution-1-flask   |     0.686925 |       1.00846  |   0.794507 |
| solution-2         |     0.658748 |       0.460335 |   2.98026  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.66804  |       0.122456 |   0.806378 |
| solution-aron-mark |     0.663569 |       0.124545 |   0.807705 |
| solution-flask     |     0.664369 |       1.00938  |   0.920461 |
| solution-1-flask   |     0.685042 |       1.00888  |   5.4804   |
| solution-2         |     0.684324 |       0.526801 | 274.342    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.671216 |       0.155462 |    3.28377 |
| solution-aron-mark |     0.666112 |       0.154925 |    3.29027 |
| solution-flask     |     0.681994 |       1.00896  |    5.48764 |