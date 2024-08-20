# 2024-08-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.543545 |       1.00914  |   0.089415 |
| solution-pl        |     0.545833 |       0.102494 |   0.169209 |
| solution-aron-mark |     1.8045   |       0.103386 |   0.177985 |
| solution-1-flask   |     1.18714  |       1.01155  |   0.254142 |
| solution-1         |     7.49817  |       1e-06    |   0.571642 |
| solution-2         |     4.35644  |       0.492887 |   1.17458  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.543899 |       1.00866  |   0.226878 |
| solution-pl        |     0.542836 |       0.104667 |   0.291735 |
| solution-aron-mark |     0.55027  |       0.103868 |   0.292144 |
| solution-1-flask   |     0.550142 |       1.00887  |   0.76864  |
| solution-2         |     0.553621 |       0.471966 |   2.52883  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.548414 |       1.00895  |    0.90395 |
| solution-pl        |     0.545139 |       0.111364 |    1.0168  |
| solution-aron-mark |     0.555888 |       0.110519 |    1.01774 |
| solution-1-flask   |     0.55286  |       1.00912  |    5.48051 |
| solution-2         |     0.543585 |       0.517873 |   21.4092  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.548188 |       1.00906  |    3.93804 |
| solution-pl        |     0.549213 |       0.146514 |    4.14755 |
| solution-aron-mark |     0.54922  |       0.142792 |    4.17369 |