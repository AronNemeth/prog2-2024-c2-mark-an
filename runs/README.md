# 2026-04-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.63239  |       1.03289  |   0.105653 |
| solution-pl        |     0.427756 |       0.152189 |   0.237329 |
| solution-aron-mark |     4.55404  |       0.154639 |   0.239525 |
| solution-1-flask   |     0.42588  |       1.00828  |   0.264021 |
| solution-1         |     7.71037  |       2e-06    |   0.625777 |
| solution-2         |     0.423633 |       0.588274 |   1.4875   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.424932 |       0.154258 |   0.376763 |
| solution-pl        |     0.428809 |       0.150779 |   0.3916   |
| solution-flask     |     0.429673 |       1.00839  |   0.404408 |
| solution-1-flask   |     0.429702 |       1.00845  |   0.8241   |
| solution-2         |     0.441136 |       0.568907 |   5.32781  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.433388 |       0.160584 |    1.11958 |
| solution-pl        |     0.443686 |       0.159309 |    1.14996 |
| solution-flask     |     0.448605 |       1.00851  |    1.70796 |
| solution-1-flask   |     0.459611 |       1.00829  |    5.78706 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.433939 |       0.180577 |    4.02482 |
| solution-aron-mark |     0.433883 |       0.187408 |    4.14119 |
| solution-flask     |     0.43757  |       1.00891  |    5.62087 |