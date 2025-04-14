# 2025-04-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |      1.03005 |       1.00894  |   0.084704 |
| solution-aron-mark |      2.55584 |       0.11904  |   0.189305 |
| solution-pl        |      0.59761 |       0.123533 |   0.190052 |
| solution-1-flask   |      5.51167 |       1.05321  |   0.271125 |
| solution-1         |      7.98244 |       1e-06    |   0.682577 |
| solution-2         |      1.0168  |       0.654211 |   1.16607  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.515739 |       0.122765 |   0.295497 |
| solution-aron-mark |     0.51751  |       0.122529 |   0.297975 |
| solution-flask     |     0.513491 |       1.00885  |   0.325245 |
| solution-1-flask   |     0.521865 |       1.01     |   0.804185 |
| solution-2         |     0.525438 |       0.520704 |   3.30824  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.513467 |       0.128482 |   0.913112 |
| solution-aron-mark |     0.514846 |       0.131788 |   0.929637 |
| solution-flask     |     0.511842 |       1.00945  |   1.25216  |
| solution-1-flask   |     0.52245  |       1.00916  |   5.71228  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.53177  |       0.157526 |    2.91608 |
| solution-aron-mark |     0.536215 |       0.158581 |    2.93126 |
| solution-flask     |     0.516696 |       1.00943  |    4.22752 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.516716 |       0.270713 |    18.0664 |
| solution-aron-mark |     0.519354 |       0.273421 |    18.4382 |