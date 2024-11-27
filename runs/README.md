# 2024-11-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.18988  |       1.05401  |   0.110922 |
| solution-aron-mark |     0.555761 |       0.108299 |   0.175876 |
| solution-pl        |     5.71226  |       0.109008 |   0.181378 |
| solution-1-flask   |     0.563847 |       1.00892  |   0.26434  |
| solution-1         |     7.56201  |       1e-06    |   0.59146  |
| solution-2         |     0.560948 |       0.506948 |   1.03496  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.562937 |       0.108238 |   0.299511 |
| solution-pl        |     0.56515  |       0.110721 |   0.308618 |
| solution-flask     |     0.557857 |       1.00916  |   0.495163 |
| solution-1-flask   |     0.559037 |       1.00912  |   0.768022 |
| solution-2         |     0.567256 |       0.474363 |   3.37261  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.569466 |       0.11894  |    1.02357 |
| solution-pl        |     0.562058 |       0.117702 |    1.02606 |
| solution-flask     |     0.553923 |       1.00898  |    2.22735 |
| solution-1-flask   |     0.565974 |       1.00902  |    5.31593 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.562742 |       0.146084 |    4.39832 |
| solution-aron-mark |     0.557109 |       0.147738 |    4.48559 |
| solution-flask     |     0.55616  |       1.00905  |    8.6408  |