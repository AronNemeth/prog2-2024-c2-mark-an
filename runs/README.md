# 2025-06-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.961023 |       1.00829  |   0.098332 |
| solution-aron-mark |     6.17949  |       0.197347 |   0.2276   |
| solution-pl        |     0.937469 |       0.144362 |   0.230851 |
| solution-1-flask   |     1.52822  |       1.10665  |   0.269563 |
| solution-2         |     0.946727 |       0.729515 |   0.813864 |
| solution-1         |     8.03806  |       1e-06    |   0.9458   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.949604 |       0.145729 |   0.352676 |
| solution-pl        |     0.949356 |       0.145546 |   0.353863 |
| solution-flask     |     0.627097 |       1.00825  |   0.375782 |
| solution-1-flask   |     0.955137 |       1.00813  |   0.78251  |
| solution-2         |     0.947718 |       0.493137 |   2.34375  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.49025  |       0.153622 |    1.04338 |
| solution-pl        |     0.489094 |       0.152865 |    1.04554 |
| solution-flask     |     0.491739 |       1.00831  |    1.53508 |
| solution-1-flask   |     0.498424 |       1.00832  |    5.39608 |
| solution-2         |     0.488882 |       0.547192 |  289.563   |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.494797 |       0.183089 |    3.14819 |
| solution-pl        |     0.491402 |       0.186439 |    3.15475 |
| solution-flask     |     0.487792 |       1.00836  |    4.95056 |