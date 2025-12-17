# 2025-12-17

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.71131  |       1.1118   |   0.097746 |
| solution-aron-mark |     0.492284 |       0.164703 |   0.248491 |
| solution-pl        |     0.48277  |       0.17011  |   0.257087 |
| solution-1-flask   |     0.484748 |       1.00836  |   0.266784 |
| solution-1         |     8.26712  |       1e-06    |   0.871997 |
| solution-2         |     5.14142  |       0.693173 |   1.83463  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.491631 |       1.00858  |   0.377266 |
| solution-pl        |     0.482732 |       0.165634 |   0.377303 |
| solution-aron-mark |     0.479623 |       0.166453 |   0.379104 |
| solution-1-flask   |     0.498832 |       1.00853  |   0.813593 |
| solution-2         |     0.479552 |       0.541539 |   2.14147  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.489238 |       0.176455 |    1.08579 |
| solution-pl        |     0.493136 |       0.173097 |    1.08633 |
| solution-flask     |     0.492195 |       1.00872  |    1.56538 |
| solution-1-flask   |     0.497842 |       1.00858  |    5.61475 |
| solution-2         |     0.485057 |       0.602723 |  303.24    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.511261 |       0.197838 |    3.65756 |
| solution-pl        |     0.480191 |       0.200408 |    3.73941 |
| solution-flask     |     0.49519  |       1.00863  |    5.26637 |