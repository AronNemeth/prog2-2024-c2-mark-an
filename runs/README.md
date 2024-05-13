# 2024-05-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.674023 |       1.00923  |   0.0686   |
| solution-pl        |     5.9218   |       0.134725 |   0.178342 |
| solution-aron-mark |     0.706352 |       0.123054 |   0.184799 |
| solution-1-flask   |     1.37226  |       1.08086  |   0.263312 |
| solution-1         |     8.09999  |       1e-06    |   0.671909 |
| solution-2         |     0.679706 |       0.446902 |   1.32868  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.688428 |       1.00917  |   0.161824 |
| solution-aron-mark |     0.683661 |       0.12806  |   0.272995 |
| solution-pl        |     0.696739 |       0.126989 |   0.276331 |
| solution-1-flask   |     0.69563  |       1.00921  |   0.776382 |
| solution-2         |     0.68012  |       0.452728 |  12.3467   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.681815 |       1.00925  |   0.700634 |
| solution-aron-mark |     0.674273 |       0.137635 |   0.826768 |
| solution-pl        |     0.679366 |       0.136071 |   0.844077 |
| solution-1-flask   |     0.687345 |       1.00927  |   5.53939  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.700587 |       1.00961  |    2.59323 |
| solution-aron-mark |     0.67922  |       0.17523  |    2.7693  |
| solution-pl        |     0.673958 |       0.175863 |    2.77914 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.710379 |       1.01006  |    17.6288 |
| solution-pl        |     0.705266 |       0.298068 |    18.3431 |
| solution-aron-mark |     0.680519 |       0.304639 |    18.3692 |