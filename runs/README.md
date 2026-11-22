# 2026-11-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.413857 |       1.01037  |   0.093642 |
| solution-pl        |     5.81449  |       0.163495 |   0.245466 |
| solution-aron-mark |     0.408294 |       0.161758 |   0.245744 |
| solution-1-flask   |     1.29092  |       1.05908  |   0.274079 |
| solution-1         |     7.55315  |       1e-06    |   0.587765 |
| solution-2         |     0.407947 |       0.518616 |   1.09495  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.416828 |       1.01042  |   0.224523 |
| solution-pl        |     0.416501 |       0.164078 |   0.379125 |
| solution-aron-mark |     0.4184   |       0.164398 |   0.379434 |
| solution-1-flask   |     0.422496 |       1.01049  |   0.791318 |
| solution-2         |     0.416095 |       0.499891 |   4.01098  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.41508  |       1.01073  |    1.104   |
| solution-pl        |     0.437015 |       0.173095 |    1.11061 |
| solution-aron-mark |     0.414907 |       0.175946 |    1.1285  |
| solution-1-flask   |     0.421096 |       1.01049  |    5.42587 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.414147 |       0.207273 |    3.45149 |
| solution-pl        |     0.437433 |       0.207344 |    3.46994 |
| solution-flask     |     0.419747 |       1.0107   |    4.21186 |