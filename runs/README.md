# 2024-10-03

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.24551  |       1.09179  |   0.085944 |
| solution-aron-mark |     1.83295  |       0.103493 |   0.178352 |
| solution-pl        |     0.576862 |       0.1039   |   0.182095 |
| solution-1-flask   |     0.57998  |       1.00809  |   0.265753 |
| solution-1         |     7.62204  |       1e-06    |   0.601128 |
| solution-2         |     4.43788  |       0.513322 |   1.16274  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.570836 |       1.00851  |   0.20787  |
| solution-aron-mark |     0.564153 |       0.104837 |   0.3069   |
| solution-pl        |     0.580362 |       0.104639 |   0.307636 |
| solution-1-flask   |     0.571724 |       1.00822  |   0.798878 |
| solution-2         |     0.57829  |       0.483118 |  13.5738   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.566715 |       1.00842  |   0.946013 |
| solution-aron-mark |     0.573249 |       0.112079 |   1.04363  |
| solution-pl        |     0.5742   |       0.111186 |   1.05493  |
| solution-1-flask   |     0.584561 |       1.00825  |   5.53943  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.569116 |       0.138195 |    4.53842 |
| solution-flask     |     0.566964 |       1.00861  |    4.56818 |
| solution-aron-mark |     0.576798 |       0.141985 |    4.65172 |