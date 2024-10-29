# 2024-10-29

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.30235  |       1.16074  |   0.11027  |
| solution-aron-mark |     0.562815 |       0.111099 |   0.17853  |
| solution-pl        |     5.89414  |       0.112535 |   0.182929 |
| solution-1-flask   |     0.582302 |       1.0092   |   0.256631 |
| solution-1         |     7.76213  |       1e-06    |   0.604635 |
| solution-2         |     0.574803 |       0.557961 |   0.946174 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.57238  |       0.110178 |   0.300449 |
| solution-aron-mark |     0.567732 |       0.110304 |   0.318394 |
| solution-flask     |     0.579651 |       1.00942  |   0.47031  |
| solution-1-flask   |     0.577076 |       1.00903  |   0.77     |
| solution-2         |     0.569498 |       0.493297 |   6.71071  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.569855 |       0.117644 |    1.01831 |
| solution-pl        |     0.595045 |       0.117451 |    1.02248 |
| solution-flask     |     0.584735 |       1.00894  |    2.12356 |
| solution-1-flask   |     0.579142 |       1.00918  |    5.4409  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.564613 |       0.147449 |    4.4841  |
| solution-pl        |     0.575762 |       0.151804 |    4.48464 |
| solution-flask     |     0.572938 |       1.00927  |    8.77922 |