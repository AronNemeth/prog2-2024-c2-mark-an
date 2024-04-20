# 2024-04-20

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.667821 |       1.00914  |   0.062086 |
| solution-aron-mark |     0.664237 |       0.11178  |   0.163366 |
| solution-pl        |     6.01345  |       0.112144 |   0.165765 |
| solution-1-flask   |     1.51175  |       1.01204  |   0.258307 |
| solution-1         |     8.13796  |       1e-06    |   0.608622 |
| solution-2         |     0.660594 |       0.411097 |   1.70829  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.662668 |       1.00889  |   0.165143 |
| solution-pl        |     0.666321 |       0.118737 |   0.259797 |
| solution-aron-mark |     0.672101 |       0.117556 |   0.265035 |
| solution-1-flask   |     0.6751   |       1.0089   |   0.788613 |
| solution-2         |     0.659774 |       0.430681 |   1.96548  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.66135  |       1.00879  |   0.712053 |
| solution-aron-mark |     0.6614   |       0.12553  |   0.810155 |
| solution-pl        |     0.664768 |       0.125793 |   0.816442 |
| solution-1-flask   |     0.674673 |       1.00901  |   5.53887  |
| solution-2         |     0.681363 |       0.479584 | 310.656    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.683627 |       1.00968  |    2.51119 |
| solution-aron-mark |     0.660696 |       0.163948 |    3.27817 |
| solution-pl        |     0.658259 |       0.163718 |    3.29152 |

## Inputs: 1000000, Queries 1000

| solution       |   setup_time |   preproc_time |   run_time |
|:---------------|-------------:|---------------:|-----------:|
| solution-flask |      0.66223 |        1.00912 |    15.2297 |