# 2026-03-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.88507  |       1.04035  |   0.110535 |
| solution-aron-mark |     0.458884 |       0.148883 |   0.239781 |
| solution-pl        |     4.88901  |       0.155518 |   0.24229  |
| solution-1-flask   |     0.469159 |       1.00899  |   0.277452 |
| solution-1         |     7.98427  |       1e-06    |   0.896736 |
| solution-2         |     0.457189 |       0.773801 |   1.17864  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.463348 |       0.150396 |   0.37178  |
| solution-pl        |     0.474011 |       0.152552 |   0.372891 |
| solution-flask     |     0.470125 |       1.00903  |   0.395169 |
| solution-1-flask   |     0.464447 |       1.00913  |   0.807136 |
| solution-2         |     0.45301  |       0.531439 |   2.9881   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.465171 |       0.163988 |    1.13387 |
| solution-aron-mark |     0.477179 |       0.157533 |    1.17539 |
| solution-flask     |     0.46615  |       1.00899  |    1.64385 |
| solution-1-flask   |     0.471066 |       1.00908  |    5.68035 |
| solution-2         |     0.460832 |       0.585001 |  159.261   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.459813 |       0.187989 |    4.12908 |
| solution-aron-mark |     0.463972 |       0.183332 |    4.13747 |
| solution-flask     |     0.469033 |       1.01012  |    5.45777 |