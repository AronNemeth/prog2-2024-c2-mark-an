# 2026-01-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.12149  |       1.07171  |   0.093318 |
| solution-pl        |     0.453814 |       0.148122 |   0.218626 |
| solution-aron-mark |     0.422024 |       0.149218 |   0.221487 |
| solution-1-flask   |     0.436461 |       1.00637  |   0.236414 |
| solution-1         |     7.86198  |       1e-06    |   0.688589 |
| solution-2         |     7.06807  |       0.621561 |   0.864813 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.430805 |       0.148016 |   0.331562 |
| solution-pl        |     0.429128 |       0.147919 |   0.334661 |
| solution-flask     |     0.424678 |       1.0071   |   0.407789 |
| solution-1-flask   |     0.435797 |       1.00657  |   0.722224 |
| solution-2         |     0.423596 |       0.474907 |   4.49067  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.422785 |       0.155385 |   0.957665 |
| solution-aron-mark |     0.42779  |       0.157627 |   0.973196 |
| solution-flask     |     0.425731 |       1.00655  |   1.76325  |
| solution-1-flask   |     0.427612 |       1.00657  |   5.3129   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.43533  |       0.183671 |    4.2127  |
| solution-aron-mark |     0.429269 |       0.182719 |    4.21671 |
| solution-flask     |     0.425286 |       1.00682  |    5.63419 |