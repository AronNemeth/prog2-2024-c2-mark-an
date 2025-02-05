# 2025-02-05

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.2191   |       1.06377  |   0.083842 |
| solution-pl        |     4.77475  |       0.150834 |   0.212999 |
| solution-aron-mark |     0.576061 |       0.144628 |   0.216969 |
| solution-1-flask   |     0.578724 |       1.00905  |   0.278399 |
| solution-1         |     7.6217   |       1e-06    |   0.663256 |
| solution-2         |     0.595597 |       0.704842 |   0.916724 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.567802 |       1.00925  |   0.300265 |
| solution-aron-mark |     0.551884 |       0.148479 |   0.311718 |
| solution-pl        |     0.585396 |       0.141904 |   0.315564 |
| solution-1-flask   |     0.605813 |       1.00929  |   0.825291 |
| solution-2         |     0.566204 |       0.51516  |   7.05932  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.566782 |       0.162806 |   0.907041 |
| solution-aron-mark |     0.572569 |       0.146618 |   0.909883 |
| solution-flask     |     0.566356 |       1.00916  |   1.25871  |
| solution-1-flask   |     0.562477 |       1.00922  |   5.98139  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.553324 |       0.177939 |    2.99355 |
| solution-aron-mark |     0.584944 |       0.177799 |    3.04454 |
| solution-flask     |     0.565122 |       1.00916  |    4.41535 |

## Inputs: 1000000, Queries 1000

| solution    |   setup_time |   preproc_time |   run_time |
|:------------|-------------:|---------------:|-----------:|
| solution-pl |     0.561056 |        0.29529 |     21.656 |