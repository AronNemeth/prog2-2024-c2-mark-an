# 2024-11-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.24468  |       1.0679   |   0.108876 |
| solution-aron-mark |     0.549811 |       0.106477 |   0.195465 |
| solution-pl        |     5.71134  |       0.108792 |   0.199498 |
| solution-1-flask   |     0.56108  |       1.00865  |   0.262148 |
| solution-1         |     7.83453  |       1e-06    |   0.616023 |
| solution-2         |     0.546648 |       0.517102 |   0.663506 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.554558 |       0.108959 |   0.297665 |
| solution-pl        |     0.551953 |       0.109019 |   0.302712 |
| solution-flask     |     0.547089 |       1.00889  |   0.481588 |
| solution-1-flask   |     0.555989 |       1.00879  |   0.776488 |
| solution-2         |     0.553689 |       0.469969 |   2.2619   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.587029 |       0.115762 |    1.01313 |
| solution-aron-mark |     0.555644 |       0.115923 |    1.01829 |
| solution-flask     |     0.561032 |       1.00907  |    2.11489 |
| solution-1-flask   |     0.573709 |       1.00928  |    5.46873 |
| solution-2         |     0.558703 |       0.516673 |   41.882   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.577027 |       0.151467 |    4.5532  |
| solution-pl        |     0.612756 |       0.154911 |    4.82781 |
| solution-flask     |     0.569841 |       1.00955  |    8.53164 |