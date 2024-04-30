# 2024-04-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.688302 |       1.00893  |   0.076596 |
| solution-aron-mark |     0.681218 |       0.118196 |   0.181358 |
| solution-pl        |     7.33384  |       0.138841 |   0.185866 |
| solution-1-flask   |     2.54602  |       1.0673   |   0.327577 |
| solution-2         |     0.684923 |       0.445007 |   0.740999 |
| solution-1         |     9.52776  |       1e-06    |   0.87046  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.675317 |       1.00887  |   0.167391 |
| solution-aron-mark |     0.711497 |       0.130919 |   0.276275 |
| solution-pl        |     0.696258 |       0.130358 |   0.27768  |
| solution-1-flask   |     0.692849 |       1.00903  |   0.803738 |
| solution-2         |     0.712083 |       0.448902 |   2.13158  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.664431 |       1.00928  |   0.711505 |
| solution-aron-mark |     0.689615 |       0.135249 |   0.840718 |
| solution-pl        |     0.677739 |       0.133625 |   0.855315 |
| solution-1-flask   |     0.702491 |       1.00907  |   5.59209  |
| solution-2         |     0.690304 |       0.505351 | 170.571    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.675003 |       1.00911  |    2.51275 |
| solution-pl        |     0.677641 |       0.171138 |    2.66129 |
| solution-aron-mark |     0.670799 |       0.167881 |    2.6757  |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.664539 |       0.295644 |    15.7657 |
| solution-flask     |     0.665719 |       1.009    |    15.9552 |
| solution-pl        |     0.667878 |       0.291824 |    16.5929 |