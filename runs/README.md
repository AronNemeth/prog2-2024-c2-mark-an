# 2025-10-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.86016  |       1.08488  |   0.104931 |
| solution-aron-mark |     0.550364 |       0.173007 |   0.258377 |
| solution-pl        |     0.541025 |       0.182112 |   0.266073 |
| solution-1-flask   |     0.536273 |       1.00924  |   0.282243 |
| solution-1         |     8.36389  |       2e-06    |   0.808688 |
| solution-2         |     5.51272  |       0.879694 |   1.17564  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.527777 |       0.179219 |   0.381843 |
| solution-pl        |     0.522117 |       0.171356 |   0.385138 |
| solution-flask     |     0.522089 |       1.00905  |   0.39558  |
| solution-1-flask   |     0.547623 |       1.00905  |   0.814307 |
| solution-2         |     0.541545 |       0.578798 |   3.06833  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.518283 |       0.183141 |    1.11418 |
| solution-pl        |     0.524029 |       0.186045 |    1.12694 |
| solution-flask     |     0.531292 |       1.0089   |    1.6407  |
| solution-1-flask   |     0.541701 |       1.00929  |    5.95884 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.539349 |       0.225472 |    3.63931 |
| solution-aron-mark |     0.556339 |       0.22072  |    3.68358 |
| solution-flask     |     0.53622  |       1.00923  |    5.64466 |