# 2025-08-18

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.53105  |       1.04676  |   0.095878 |
| solution-pl        |     0.476213 |       0.151214 |   0.235102 |
| solution-aron-mark |     4.87559  |       0.155495 |   0.242994 |
| solution-1-flask   |     0.489623 |       1.00826  |   0.262887 |
| solution-1         |     7.96701  |       1e-06    |   0.683544 |
| solution-2         |     0.486998 |       0.611729 |   1.35978  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.497799 |       0.154653 |   0.364107 |
| solution-aron-mark |     0.486915 |       0.156379 |   0.365245 |
| solution-flask     |     0.482816 |       1.00837  |   0.377773 |
| solution-1-flask   |     0.49488  |       1.00827  |   0.788859 |
| solution-2         |     0.477972 |       0.502644 |   3.62331  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.488797 |       0.163532 |    1.06072 |
| solution-aron-mark |     0.491069 |       0.162568 |    1.06505 |
| solution-flask     |     0.487442 |       1.00829  |    1.58118 |
| solution-1-flask   |     0.518082 |       1.00864  |    5.66655 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.482853 |       0.193738 |    3.22419 |
| solution-aron-mark |     0.484755 |       0.197161 |    3.22997 |
| solution-flask     |     0.494282 |       1.00874  |    5.12034 |