# 2024-10-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.30317  |       1.0431   |   0.1038   |
| solution-aron-mark |     0.568903 |       0.110294 |   0.180048 |
| solution-pl        |     5.75946  |       0.108735 |   0.194945 |
| solution-1-flask   |     0.583408 |       1.00891  |   0.260017 |
| solution-1         |     7.90355  |       1e-06    |   0.608575 |
| solution-2         |     0.584608 |       0.557189 |   0.758515 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.571537 |       0.108732 |   0.301118 |
| solution-aron-mark |     0.592955 |       0.112793 |   0.338327 |
| solution-flask     |     0.595622 |       1.00899  |   0.477285 |
| solution-1-flask   |     0.567511 |       1.009    |   0.770684 |
| solution-2         |     0.564874 |       0.481885 |   3.09948  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.565607 |       0.118299 |    1.02073 |
| solution-pl        |     0.573734 |       0.115721 |    1.04244 |
| solution-flask     |     0.570758 |       1.0092   |    2.12859 |
| solution-1-flask   |     0.583589 |       1.00907  |    5.37829 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.566414 |       0.144934 |    4.29258 |
| solution-pl        |     0.568468 |       0.147026 |    4.47242 |
| solution-flask     |     0.574363 |       1.00951  |    8.672   |