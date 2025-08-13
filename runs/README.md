# 2025-08-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.17662  |       1.05513  |   0.098833 |
| solution-aron-mark |     4.87773  |       0.150063 |   0.238914 |
| solution-pl        |     0.480492 |       0.153386 |   0.242565 |
| solution-1-flask   |     0.484271 |       1.00818  |   0.265285 |
| solution-1         |     8.25254  |       1e-06    |   0.721455 |
| solution-2         |     0.479229 |       0.704206 |   1.42562  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.477107 |       0.151642 |   0.367086 |
| solution-aron-mark |     0.477537 |       0.153876 |   0.369877 |
| solution-flask     |     0.482649 |       1.00828  |   0.419935 |
| solution-1-flask   |     0.484842 |       1.00836  |   0.807567 |
| solution-2         |     0.481297 |       0.50579  |   4.02602  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.477557 |       0.162368 |    1.08379 |
| solution-pl        |     0.477393 |       0.162025 |    1.09728 |
| solution-flask     |     0.473016 |       1.00855  |    1.59764 |
| solution-1-flask   |     0.48403  |       1.00856  |    5.61069 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.475737 |       0.191075 |    3.25287 |
| solution-pl        |     0.476503 |       0.188271 |    3.26507 |
| solution-flask     |     0.491527 |       1.0086   |    5.12795 |