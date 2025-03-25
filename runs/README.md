# 2025-03-25

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.547209 |       1.00902  |   0.086419 |
| solution-pl        |     0.556634 |       0.12716  |   0.192728 |
| solution-aron-mark |     1.79181  |       0.126504 |   0.193721 |
| solution-1-flask   |     4.98085  |       1.05319  |   0.292511 |
| solution-1         |     7.7529   |       1e-06    |   0.755579 |
| solution-2         |     0.546053 |       0.640934 |   1.07953  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.535086 |       0.125326 |   0.301247 |
| solution-aron-mark |     0.568131 |       0.126683 |   0.306685 |
| solution-flask     |     0.527215 |       1.00921  |   0.310576 |
| solution-1-flask   |     0.549146 |       1.00951  |   0.824337 |
| solution-2         |     0.554942 |       0.550714 |   2.9029   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.523589 |       0.131076 |   0.917605 |
| solution-pl        |     0.561882 |       0.133449 |   0.928856 |
| solution-flask     |     0.565676 |       1.00945  |   1.30267  |
| solution-1-flask   |     0.538298 |       1.00879  |   5.86829  |
| solution-2         |     0.545307 |       0.557281 |  46.3143   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.521704 |       0.162238 |    2.874   |
| solution-aron-mark |     0.538906 |       0.167339 |    2.95399 |
| solution-flask     |     0.531579 |       1.00892  |    4.28367 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.584093 |       0.276342 |    17.5918 |
| solution-aron-mark |     0.533284 |       0.271169 |    18.339  |