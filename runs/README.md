# 2025-11-26

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.73526  |       1.06498  |   0.099821 |
| solution-pl        |     0.48389  |       0.159741 |   0.247146 |
| solution-aron-mark |     0.48973  |       0.163919 |   0.247378 |
| solution-1-flask   |     0.493408 |       1.00829  |   0.26813  |
| solution-1         |     8.56375  |       1e-06    |   0.693501 |
| solution-2         |     5.40611  |       0.63747  |   1.03723  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.485564 |       0.162051 |   0.366134 |
| solution-pl        |     0.487501 |       0.160879 |   0.366449 |
| solution-flask     |     0.485813 |       1.00852  |   0.379983 |
| solution-1-flask   |     0.486047 |       1.00854  |   0.796604 |
| solution-2         |     0.486478 |       0.543766 |   4.04926  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.486333 |       0.175937 |    1.06436 |
| solution-aron-mark |     0.480917 |       0.167643 |    1.07153 |
| solution-flask     |     0.479148 |       1.00864  |    1.61367 |
| solution-1-flask   |     0.487495 |       1.00854  |    5.66586 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.489152 |       0.20186  |    3.30069 |
| solution-pl        |     0.489041 |       0.202193 |    3.32698 |
| solution-flask     |     0.488397 |       1.00878  |    5.17013 |