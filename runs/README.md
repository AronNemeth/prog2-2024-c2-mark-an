# 2026-07-15

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.07953  |       1.07606  |   0.105632 |
| solution-pl        |     5.51814  |       0.168935 |   0.218677 |
| solution-aron-mark |     0.42615  |       0.147055 |   0.220701 |
| solution-1-flask   |     0.423443 |       1.00712  |   0.235223 |
| solution-1         |     6.75397  |       1e-06    |   0.618615 |
| solution-2         |     0.398117 |       0.636337 |   1.41907  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.416614 |       0.146199 |   0.335895 |
| solution-pl        |     0.425028 |       0.148653 |   0.346146 |
| solution-flask     |     0.409485 |       1.00744  |   0.436604 |
| solution-1-flask   |     0.414503 |       1.00713  |   0.744242 |
| solution-2         |     0.413823 |       0.507005 |   4.48621  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.405406 |       0.147698 |    1.02089 |
| solution-pl        |     0.411794 |       0.151772 |    1.02688 |
| solution-flask     |     0.409277 |       1.00677  |    1.86702 |
| solution-1-flask   |     0.412993 |       1.00675  |    5.52013 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.405719 |       0.176287 |    5.02438 |
| solution-aron-mark |     0.403864 |       0.176376 |    5.17753 |
| solution-flask     |     0.400893 |       1.00737  |    6.22911 |