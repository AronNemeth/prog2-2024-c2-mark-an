# 2025-11-13

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.69355  |       1.04179  |   0.098597 |
| solution-pl        |     0.471879 |       0.157895 |   0.238665 |
| solution-aron-mark |     0.479431 |       0.15909  |   0.245899 |
| solution-1-flask   |     0.476133 |       1.00833  |   0.264567 |
| solution-1         |     8.07551  |       1e-06    |   0.699261 |
| solution-2         |     4.94547  |       0.616737 |   1.30056  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.476226 |       0.1617   |   0.370588 |
| solution-aron-mark |     0.474453 |       0.161101 |   0.370703 |
| solution-flask     |     0.488188 |       1.00839  |   0.376345 |
| solution-1-flask   |     0.477441 |       1.0085   |   0.801555 |
| solution-2         |     0.473703 |       0.554865 |   3.60942  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.484416 |       0.164976 |    1.06688 |
| solution-pl        |     0.472552 |       0.169371 |    1.07086 |
| solution-flask     |     0.48196  |       1.00852  |    1.58267 |
| solution-1-flask   |     0.490773 |       1.00848  |    5.73786 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.47364  |       0.194935 |    3.21954 |
| solution-pl        |     0.481705 |       0.194201 |    3.26424 |
| solution-flask     |     0.470757 |       1.00868  |    5.08142 |