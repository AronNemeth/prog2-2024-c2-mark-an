# 2026-06-22

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.13723  |       1.07986  |   0.097465 |
| solution-pl        |     6.20716  |       0.173283 |   0.223112 |
| solution-1-flask   |     0.427212 |       1.00861  |   0.223631 |
| solution-aron-mark |     0.422167 |       0.151251 |   0.228264 |
| solution-1         |     7.40247  |       1e-06    |   0.607836 |
| solution-2         |     0.411239 |       0.642907 |   1.20396  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.420457 |       0.150402 |   0.347785 |
| solution-pl        |     0.421586 |       0.14998  |   0.354584 |
| solution-flask     |     0.421232 |       1.00874  |   0.390664 |
| solution-1-flask   |     0.425337 |       1.00882  |   0.731713 |
| solution-2         |     0.417974 |       0.492964 |   2.65882  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.423267 |       0.159031 |    1.02055 |
| solution-aron-mark |     0.420463 |       0.157321 |    1.02221 |
| solution-flask     |     0.421593 |       1.00906  |    1.61825 |
| solution-1-flask   |     0.42735  |       1.00881  |    5.46585 |
| solution-2         |     0.419704 |       0.548407 |   41.7215  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.422617 |       0.182356 |    3.69353 |
| solution-aron-mark |     0.423389 |       0.180704 |    3.72684 |
| solution-flask     |     0.419477 |       1.00872  |    5.10497 |