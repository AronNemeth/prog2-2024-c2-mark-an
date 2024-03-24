# 2024-03-24

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.61485  |       1.04909  |   0.065078 |
| solution-aron-mark |     0.640922 |       0.106912 |   0.159412 |
| solution-pl        |     0.643363 |       0.107313 |   0.159429 |
| solution-1-flask   |     0.653034 |       1.00835  |   0.289095 |
| solution-1         |     8.14399  |       1e-06    |   0.587048 |
| solution-2         |     4.80048  |       0.458492 |   1.09519  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.652008 |       1.00867  |   0.171624 |
| solution-aron-mark |     0.644159 |       0.114577 |   0.251028 |
| solution-pl        |     0.638709 |       0.112742 |   0.25226  |
| solution-1-flask   |     0.656577 |       1.0084   |   0.785591 |
| solution-2         |     0.639086 |       0.439563 |   5.88986  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.65899  |       0.118721 |   0.793072 |
| solution-aron-mark |     0.65454  |       0.118593 |   0.800702 |
| solution-flask     |     0.646019 |       1.00877  |   0.914585 |
| solution-1-flask   |     0.654666 |       1.00868  |   5.44343  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |      0.64538 |       0.153084 |    3.22598 |
| solution-pl        |      0.64536 |       0.151795 |    3.29256 |
| solution-flask     |      0.64889 |       1.00867  |    5.17127 |