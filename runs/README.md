# 2025-10-16

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.11336  |       1.10491  |   0.106922 |
| solution-aron-mark |     0.985369 |       0.158703 |   0.246091 |
| solution-pl        |     4.96943  |       0.161404 |   0.248141 |
| solution-1-flask   |     0.960286 |       1.00813  |   0.266384 |
| solution-2         |     0.955199 |       0.936196 |   0.852659 |
| solution-1         |     8.39109  |       1e-06    |   0.987257 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.502489 |       0.167319 |   0.374949 |
| solution-flask     |     0.588367 |       1.00836  |   0.381707 |
| solution-aron-mark |     0.500118 |       0.164242 |   0.382972 |
| solution-1-flask   |     0.522925 |       1.00852  |   0.785472 |
| solution-2         |     0.512676 |       0.523474 |  12.0795   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.530692 |       0.175895 |    1.10921 |
| solution-pl        |     0.509496 |       0.168766 |    1.11478 |
| solution-flask     |     0.522718 |       1.00852  |    1.62127 |
| solution-1-flask   |     0.514698 |       1.00841  |    5.66716 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.49469  |       0.195071 |    3.40302 |
| solution-aron-mark |     0.513907 |       0.197403 |    3.4254  |
| solution-flask     |     0.517699 |       1.00861  |    5.27309 |