# 2025-11-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.59653  |       1.06293  |   0.090357 |
| solution-pl        |     0.413833 |       0.142073 |   0.214223 |
| solution-aron-mark |     0.418378 |       0.140739 |   0.217551 |
| solution-1-flask   |     0.418961 |       1.0061   |   0.235924 |
| solution-1         |     7.0163   |       1e-06    |   0.633213 |
| solution-2         |     4.39604  |       0.61868  |   0.969432 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.411416 |       0.144266 |   0.321209 |
| solution-aron-mark |     0.414332 |       0.144153 |   0.326691 |
| solution-flask     |     0.414381 |       1.00665  |   0.402768 |
| solution-1-flask   |     0.418976 |       1.00655  |   0.715098 |
| solution-2         |     0.414953 |       0.469229 |   2.32504  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.419926 |       0.149612 |   0.943911 |
| solution-aron-mark |     0.424746 |       0.15104  |   0.97049  |
| solution-flask     |     0.423179 |       1.00639  |   1.67764  |
| solution-1-flask   |     0.429271 |       1.00641  |   5.26356  |
| solution-2         |     0.414998 |       0.521206 | 187.073    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.416942 |       0.180471 |    3.75733 |
| solution-aron-mark |     0.416749 |       0.182891 |    3.78388 |
| solution-flask     |     0.417991 |       1.00694  |    5.39266 |