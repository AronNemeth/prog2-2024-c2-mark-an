# 2024-10-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.11543  |       1.05244  |   0.109819 |
| solution-aron-mark |     0.559599 |       0.108325 |   0.175554 |
| solution-pl        |     5.83889  |       0.108548 |   0.175924 |
| solution-1-flask   |     0.568153 |       1.00946  |   0.250106 |
| solution-1         |     7.56873  |       1e-06    |   0.588136 |
| solution-2         |     0.549475 |       0.54075  |   1.30441  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.588266 |       0.10841  |   0.296859 |
| solution-aron-mark |     0.571575 |       0.109649 |   0.297698 |
| solution-flask     |     0.557932 |       1.00948  |   0.473969 |
| solution-1-flask   |     0.561307 |       1.00893  |   0.762938 |
| solution-2         |     0.579709 |       0.478545 |   3.43412  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.55797  |       0.116109 |    1.01007 |
| solution-pl        |     0.578109 |       0.116213 |    1.01106 |
| solution-flask     |     0.552591 |       1.00926  |    2.11673 |
| solution-1-flask   |     0.564411 |       1.00903  |    5.42275 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.558531 |       0.150066 |    4.20912 |
| solution-pl        |     0.558148 |       0.144722 |    4.24426 |
| solution-flask     |     0.554627 |       1.00931  |    8.29465 |