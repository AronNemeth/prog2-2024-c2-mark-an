# 2025-05-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.455142 |       1.0089   |   0.079378 |
| solution-aron-mark |     2.00071  |       0.120957 |   0.189847 |
| solution-pl        |     0.461073 |       0.119771 |   0.193946 |
| solution-1-flask   |     1.13158  |       1.22348  |   0.266483 |
| solution-1         |     7.68453  |       1e-06    |   0.666695 |
| solution-2         |     4.37326  |       0.700598 |   1.4557   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.461841 |       0.120869 |   0.290359 |
| solution-flask     |     0.456566 |       1.0089   |   0.291801 |
| solution-aron-mark |     0.461224 |       0.122307 |   0.291942 |
| solution-1-flask   |     0.466036 |       1.00866  |   0.769197 |
| solution-2         |     0.458774 |       0.512996 |   9.21612  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.45864  |       0.128309 |   0.881665 |
| solution-aron-mark |     0.464756 |       0.128459 |   0.889653 |
| solution-flask     |     0.456765 |       1.0086   |   1.22516  |
| solution-1-flask   |     0.466794 |       1.00872  |   5.4056   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.460619 |       0.158475 |    2.78511 |
| solution-aron-mark |     0.462428 |       0.159002 |    2.8595  |
| solution-flask     |     0.455929 |       1.00862  |    4.15521 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.45975  |       0.266057 |    15.575  |
| solution-pl        |     0.462126 |       0.267057 |    15.6229 |