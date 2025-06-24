# 2025-06-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.531834 |       1.00894  |   0.105317 |
| solution-pl        |     0.962158 |       0.156833 |   0.238007 |
| solution-aron-mark |     6.43943  |       0.172382 |   0.240083 |
| solution-1-flask   |     1.58523  |       1.11268  |   0.266733 |
| solution-1         |     8.29846  |       1e-06    |   0.839561 |
| solution-2         |     0.584231 |       0.7055   |   1.24493  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.529697 |       0.158521 |   0.369724 |
| solution-aron-mark |     0.522038 |       0.15551  |   0.373168 |
| solution-flask     |     0.559973 |       1.00916  |   0.422813 |
| solution-1-flask   |     0.534924 |       1.00877  |   0.804729 |
| solution-2         |     0.549858 |       0.517556 |   5.81025  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.520139 |       0.163902 |    1.08697 |
| solution-aron-mark |     0.537022 |       0.16675  |    1.10221 |
| solution-flask     |     0.514822 |       1.00872  |    1.634   |
| solution-1-flask   |     0.52585  |       1.00899  |    5.5714  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.520178 |       0.197363 |    3.4055  |
| solution-pl        |     0.529319 |       0.190752 |    3.41439 |
| solution-flask     |     0.528816 |       1.00912  |    5.33087 |