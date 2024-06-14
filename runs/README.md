# 2024-06-14

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.34502  |       1.08052  |   0.067997 |
| solution-pl        |     0.687804 |       0.106923 |   0.165131 |
| solution-aron-mark |     5.91961  |       0.107969 |   0.166314 |
| solution-1-flask   |     0.705744 |       1.00916  |   0.264022 |
| solution-1         |     8.12469  |       1e-06    |   0.601218 |
| solution-2         |     0.669292 |       0.429032 |   1.2694   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.679563 |       1.0092   |   0.159123 |
| solution-aron-mark |     0.671074 |       0.105659 |   0.2554   |
| solution-pl        |     0.67903  |       0.109743 |   0.261283 |
| solution-1-flask   |     0.685714 |       1.00924  |   0.784166 |
| solution-2         |     0.675279 |       0.465288 |  12.4759   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.689612 |       1.00913  |   0.707082 |
| solution-pl        |     0.676109 |       0.115142 |   0.801335 |
| solution-aron-mark |     0.671064 |       0.114606 |   0.808327 |
| solution-1-flask   |     0.683324 |       1.00934  |   5.59405  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.675803 |       1.00914  |    2.66045 |
| solution-aron-mark |     0.685331 |       0.151259 |    2.7476  |
| solution-pl        |     0.703415 |       0.152258 |    2.75454 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.667668 |       1.00888  |    16.2884 |
| solution-pl        |     0.689659 |       0.289451 |    22.7381 |
| solution-aron-mark |     0.670126 |       0.285526 |    23.602  |