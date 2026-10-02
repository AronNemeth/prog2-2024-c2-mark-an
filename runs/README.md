# 2026-10-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.18784  |       1.13714  |   0.109999 |
| solution-aron-mark |     6.30913  |       0.240811 |   0.245336 |
| solution-pl        |     0.440636 |       0.158809 |   0.246073 |
| solution-1-flask   |     0.470647 |       1.00879  |   0.268647 |
| solution-1         |    12.1773   |       1e-06    |   0.660213 |
| solution-2         |     0.43053  |       0.693648 |   1.28136  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.444946 |       0.161776 |   0.385797 |
| solution-aron-mark |     0.440369 |       0.158235 |   0.386122 |
| solution-flask     |     0.446133 |       1.00885  |   0.398202 |
| solution-1-flask   |     0.463522 |       1.00887  |   0.799409 |
| solution-2         |     0.438841 |       0.515962 |  14.5737   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.442956 |       0.166587 |    1.16322 |
| solution-pl        |     0.447269 |       0.169759 |    1.1705  |
| solution-flask     |     0.462538 |       1.00912  |    1.71199 |
| solution-1-flask   |     0.451467 |       1.00886  |    5.8339  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.445371 |       0.188066 |    3.71186 |
| solution-aron-mark |     0.458108 |       0.192585 |    3.73574 |
| solution-flask     |     0.441167 |       1.00901  |    5.48653 |