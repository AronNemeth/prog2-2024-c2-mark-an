# 2026-04-30

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.59389  |       1.04958  |   0.102136 |
| solution-pl        |     0.415207 |       0.143998 |   0.228852 |
| solution-aron-mark |     4.42712  |       0.145465 |   0.230367 |
| solution-1-flask   |     0.420512 |       1.00815  |   0.261524 |
| solution-1         |     7.5379   |       1e-06    |   0.729624 |
| solution-2         |     0.410364 |       0.627028 |   1.67864  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.412212 |       0.145499 |   0.363356 |
| solution-aron-mark |     0.42174  |       0.149455 |   0.364075 |
| solution-flask     |     0.419154 |       1.00837  |   0.398118 |
| solution-1-flask   |     0.417356 |       1.00824  |   0.80482  |
| solution-2         |     0.414766 |       0.527058 |   3.45934  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.416004 |       0.152078 |    1.10446 |
| solution-aron-mark |     0.412354 |       0.153578 |    1.12376 |
| solution-flask     |     0.420581 |       1.0081   |    1.66187 |
| solution-1-flask   |     0.416651 |       1.00839  |    5.65532 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.416221 |       0.176616 |    3.71292 |
| solution-pl        |     0.413939 |       0.176621 |    3.78685 |
| solution-flask     |     0.411273 |       1.00903  |    5.4356  |