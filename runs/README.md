# 2026-09-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.29456  |       1.14329  |   0.110154 |
| solution-aron-mark |     6.19313  |       0.192451 |   0.243523 |
| solution-pl        |     0.447185 |       0.159584 |   0.252353 |
| solution-1-flask   |     0.453675 |       1.00853  |   0.269944 |
| solution-1         |     7.83991  |       1e-06    |   0.908997 |
| solution-2         |     0.45949  |       0.789501 |   1.06385  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.430839 |       0.157958 |   0.382754 |
| solution-pl        |     0.445039 |       0.164922 |   0.38415  |
| solution-flask     |     0.440272 |       1.00876  |   0.392996 |
| solution-1-flask   |     0.445176 |       1.00866  |   0.815476 |
| solution-2         |     0.432589 |       0.518896 |   5.27739  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.440354 |       0.164243 |    1.14716 |
| solution-aron-mark |     0.444659 |       0.161137 |    1.17442 |
| solution-flask     |     0.431052 |       1.00893  |    1.68455 |
| solution-1-flask   |     0.451178 |       1.0085   |    5.87463 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.433144 |       0.186672 |    3.57675 |
| solution-pl        |     0.432874 |       0.184415 |    3.60694 |
| solution-flask     |     0.423051 |       1.00862  |    5.44935 |