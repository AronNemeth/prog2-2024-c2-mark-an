# 2025-03-01

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.531983 |       1.00841  |   0.07933  |
| solution-aron-mark |     1.74705  |       0.146916 |   0.201564 |
| solution-pl        |     0.532153 |       0.141827 |   0.202615 |
| solution-1-flask   |     4.94613  |       1.06131  |   0.261474 |
| solution-1         |     7.03094  |       1e-06    |   0.631437 |
| solution-2         |     0.533264 |       0.543153 |   1.14475  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.530738 |       1.00917  |   0.293572 |
| solution-pl        |     0.530305 |       0.14177  |   0.306042 |
| solution-aron-mark |     0.526242 |       0.141766 |   0.310412 |
| solution-1-flask   |     0.532775 |       1.0091   |   0.802611 |
| solution-2         |     0.532717 |       0.507991 |   3.0728   |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.547349 |       0.148495 |   0.901103 |
| solution-pl        |     0.529466 |       0.149278 |   0.906025 |
| solution-flask     |     0.529447 |       1.00877  |   1.23825  |
| solution-1-flask   |     0.532212 |       1.00861  |   5.68335  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.525978 |       0.176032 |    2.82972 |
| solution-aron-mark |     0.533376 |       0.176162 |    2.84408 |
| solution-flask     |     0.529307 |       1.00869  |    4.24783 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.526335 |       0.274737 |    16.2206 |
| solution-aron-mark |     0.529001 |       0.275337 |    16.2764 |