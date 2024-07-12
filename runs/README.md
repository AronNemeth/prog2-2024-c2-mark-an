# 2024-07-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.7583   |       1.11777  |   0.094121 |
| solution-aron-mark |     0.978561 |       0.104358 |   0.170922 |
| solution-pl        |     6.3894   |       0.104932 |   0.1725   |
| solution-1-flask   |     0.532235 |       1.00938  |   0.269851 |
| solution-2         |     0.875104 |       0.871319 |   0.853479 |
| solution-1         |     8.7729   |       1e-06    |   0.946712 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.521797 |       1.00912  |   0.22367  |
| solution-aron-mark |     0.525388 |       0.108212 |   0.288066 |
| solution-pl        |     0.519298 |       0.10785  |   0.289448 |
| solution-1-flask   |     0.53271  |       1.00953  |   0.785883 |
| solution-2         |     0.527733 |       0.513564 |  13.4095   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.534568 |       1.00935  |   0.936569 |
| solution-aron-mark |     0.514102 |       0.116218 |   0.991005 |
| solution-pl        |     0.516037 |       0.113487 |   1.02543  |
| solution-1-flask   |     0.517479 |       1.00956  |   5.64528  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.514025 |       1.00962  |    4.46396 |
| solution-pl        |     0.527093 |       0.147391 |    4.49278 |
| solution-aron-mark |     0.532569 |       0.145973 |    4.52669 |