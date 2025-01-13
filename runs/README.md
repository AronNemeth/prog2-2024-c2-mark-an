# 2025-01-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.8018   |       1.00889  |   0.105304 |
| solution-aron-mark |     0.531783 |       0.112234 |   0.188088 |
| solution-pl        |     0.528233 |       0.109876 |   0.188969 |
| solution-1-flask   |     5.01648  |       1.14694  |   0.270064 |
| solution-1         |     7.39389  |       1e-06    |   0.596536 |
| solution-2         |     0.525075 |       0.538014 |   1.18524  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.527667 |       0.112086 |   0.320986 |
| solution-aron-mark |     0.526141 |       0.112693 |   0.321313 |
| solution-flask     |     0.529132 |       1.00877  |   0.497868 |
| solution-1-flask   |     0.532269 |       1.00873  |   0.808522 |
| solution-2         |     0.525297 |       0.486172 |   3.99027  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.527169 |       0.118406 |    1.09081 |
| solution-aron-mark |     0.528423 |       0.119644 |    1.0914  |
| solution-flask     |     0.529382 |       1.00897  |    2.19673 |
| solution-1-flask   |     0.535185 |       1.00935  |    5.74629 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.530188 |       0.145209 |    4.35621 |
| solution-pl        |     0.526187 |       0.146837 |    4.36477 |
| solution-flask     |     0.528763 |       1.00893  |    8.50538 |