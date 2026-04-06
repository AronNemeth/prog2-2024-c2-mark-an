# 2026-04-06

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.54093  |       1.0754   |   0.107297 |
| solution-aron-mark |     0.435898 |       0.152686 |   0.236422 |
| solution-pl        |     4.34905  |       0.149229 |   0.236677 |
| solution-1-flask   |     0.425838 |       1.00809  |   0.266323 |
| solution-1         |     7.65463  |       1e-06    |   0.739225 |
| solution-2         |     0.421059 |       1.15724  |   0.811927 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.420943 |       0.150113 |   0.373325 |
| solution-aron-mark |     0.421933 |       0.150094 |   0.3763   |
| solution-flask     |     0.420608 |       1.00846  |   0.38617  |
| solution-1-flask   |     0.424266 |       1.00835  |   0.811462 |
| solution-2         |     0.416982 |       0.51981  |   3.45305  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.42306  |       0.155929 |    1.14124 |
| solution-pl        |     0.421667 |       0.154817 |    1.14406 |
| solution-flask     |     0.422724 |       1.00856  |    1.65575 |
| solution-1-flask   |     0.436267 |       1.00841  |    5.62504 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.431415 |       0.181759 |    4.0861  |
| solution-pl        |     0.427407 |       0.181848 |    4.13425 |
| solution-flask     |     0.425872 |       1.00845  |    5.28211 |