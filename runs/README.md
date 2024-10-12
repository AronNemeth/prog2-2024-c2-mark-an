# 2024-10-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.10504  |       1.04592  |   0.090876 |
| solution-pl        |     5.6849   |       0.103973 |   0.170561 |
| solution-aron-mark |     0.551986 |       0.10267  |   0.170626 |
| solution-1-flask   |     0.560299 |       1.0087   |   0.263236 |
| solution-1         |     7.55581  |       1e-06    |   0.583383 |
| solution-2         |     0.550589 |       0.522944 |   0.937931 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.571987 |       1.00896  |   0.19493  |
| solution-aron-mark |     0.56013  |       0.104166 |   0.288001 |
| solution-pl        |     0.563525 |       0.103913 |   0.324782 |
| solution-1-flask   |     0.565224 |       1.00883  |   0.794932 |
| solution-2         |     0.555494 |       0.470679 |   4.80843  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.567277 |       1.00897  |   0.894866 |
| solution-pl        |     0.568357 |       0.112551 |   0.993114 |
| solution-aron-mark |     0.551091 |       0.110866 |   0.998361 |
| solution-1-flask   |     0.562973 |       1.00889  |   5.43001  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.553081 |       1.00945  |    4.12145 |
| solution-aron-mark |     0.556983 |       0.146196 |    4.1457  |
| solution-pl        |     0.553362 |       0.143683 |    4.17234 |