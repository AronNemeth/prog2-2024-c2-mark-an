# 2024-06-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.506595 |       1.00903  |   0.066939 |
| solution-aron-mark |     5.82089  |       0.100756 |   0.158422 |
| solution-pl        |     0.49561  |       0.104152 |   0.161949 |
| solution-1-flask   |     1.16914  |       1.1026   |   0.260142 |
| solution-1         |     7.93419  |       1e-06    |   0.592185 |
| solution-2         |     0.497492 |       0.53065  |   0.834877 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.515202 |       1.00893  |   0.165682 |
| solution-aron-mark |     0.50508  |       0.104964 |   0.26111  |
| solution-pl        |     0.499996 |       0.107092 |   0.261945 |
| solution-1-flask   |     0.519658 |       1.00924  |   0.796502 |
| solution-2         |     0.516721 |       0.486342 |   2.95335  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.501669 |       1.00908  |   0.703997 |
| solution-aron-mark |     0.506743 |       0.11182  |   0.806979 |
| solution-pl        |     0.514109 |       0.113585 |   0.813022 |
| solution-1-flask   |     0.515919 |       1.00909  |   5.53998  |
| solution-2         |     0.501496 |       0.556762 | 164.46     |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.499446 |       1.00941  |    2.56038 |
| solution-pl        |     0.507977 |       0.153328 |    2.65006 |
| solution-aron-mark |     0.499093 |       0.15291  |    2.68796 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.500494 |       1.00954  |    16.5619 |
| solution-aron-mark |     0.495046 |       0.285227 |    22.1876 |
| solution-pl        |     0.518914 |       0.279994 |    22.365  |