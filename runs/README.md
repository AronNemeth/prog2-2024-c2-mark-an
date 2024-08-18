# 2024-08-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.553228 |       1.00916  |   0.075577 |
| solution-pl        |     0.558884 |       0.104131 |   0.171318 |
| solution-aron-mark |     1.87658  |       0.102412 |   0.172396 |
| solution-1-flask   |     1.23621  |       1.06245  |   0.256995 |
| solution-1         |     7.7353   |       1e-06    |   0.576935 |
| solution-2         |     4.45247  |       0.494078 |   1.41002  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.554011 |       1.00896  |   0.221446 |
| solution-aron-mark |     0.554375 |       0.104664 |   0.296608 |
| solution-pl        |     0.550173 |       0.10397  |   0.297452 |
| solution-1-flask   |     0.561497 |       1.00909  |   0.775121 |
| solution-2         |     0.554774 |       0.471349 |   5.70138  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.552743 |       1.00882  |   0.905609 |
| solution-pl        |     0.55295  |       0.113051 |   1.02756  |
| solution-aron-mark |     0.554407 |       0.110898 |   1.03707  |
| solution-1-flask   |     0.572565 |       1.00911  |   5.54371  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.553037 |       1.00913  |    4.16205 |
| solution-aron-mark |     0.554778 |       0.142316 |    4.24383 |
| solution-pl        |     0.553796 |       0.143354 |    4.31107 |