# 2026-04-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.84203  |       1.09708  |   0.0994   |
| solution-aron-mark |     4.43335  |       0.152062 |   0.226146 |
| solution-pl        |     0.41577  |       0.15033  |   0.226344 |
| solution-1-flask   |     0.413727 |       1.00806  |   0.258832 |
| solution-1         |     8.5137   |       2e-06    |   0.699858 |
| solution-2         |     0.414852 |       0.721942 |   1.8033   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.418672 |       0.151708 |   0.35757  |
| solution-pl        |     0.414434 |       0.149233 |   0.359241 |
| solution-flask     |     0.412988 |       1.00817  |   0.390715 |
| solution-1-flask   |     0.419097 |       1.00803  |   0.812049 |
| solution-2         |     0.43031  |       0.515154 |   7.28137  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.422086 |       0.156616 |    1.08042 |
| solution-pl        |     0.41681  |       0.156432 |    1.0916  |
| solution-flask     |     0.410847 |       1.0084   |    1.64104 |
| solution-1-flask   |     0.416276 |       1.00851  |    5.6578  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.420264 |        0.1774  |    3.83127 |
| solution-aron-mark |     0.425461 |        0.17883 |    3.8522  |
| solution-flask     |     0.416106 |        1.00846 |    5.323   |