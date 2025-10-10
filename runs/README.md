# 2025-10-10

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.41292  |       1.11718  |   0.101335 |
| solution-pl        |     0.477518 |       0.157362 |   0.235718 |
| solution-aron-mark |     0.482693 |       0.152379 |   0.239008 |
| solution-1-flask   |     0.486254 |       1.00831  |   0.265164 |
| solution-2         |     4.30192  |       0.917766 |   0.897982 |
| solution-1         |     7.23392  |       1e-06    |   0.928601 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.481411 |       0.15588  |   0.365872 |
| solution-pl        |     0.479808 |       0.154465 |   0.366343 |
| solution-flask     |     0.483019 |       1.00835  |   0.372182 |
| solution-1-flask   |     0.482495 |       1.00827  |   0.791583 |
| solution-2         |     0.479677 |       0.508192 |   3.98887  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.479679 |       0.163051 |    1.07289 |
| solution-pl        |     0.476909 |       0.162158 |    1.07941 |
| solution-flask     |     0.481766 |       1.00815  |    1.55946 |
| solution-1-flask   |     0.484007 |       1.00815  |    5.58528 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.478598 |       0.192363 |    3.20042 |
| solution-pl        |     0.480688 |       0.193404 |    3.21363 |
| solution-flask     |     0.477085 |       1.00849  |    5.0621  |