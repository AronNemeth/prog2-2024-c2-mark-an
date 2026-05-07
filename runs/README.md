# 2026-05-07

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.18572  |       1.04581  |   0.096845 |
| solution-aron-mark |     5.71955  |       0.147628 |   0.224017 |
| solution-pl        |     0.415536 |       0.147867 |   0.225253 |
| solution-1-flask   |     0.416955 |       1.00852  |   0.233742 |
| solution-1         |     8.18871  |       1e-06    |   0.587971 |
| solution-2         |     0.408894 |       0.619673 |   0.884095 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.415268 |       0.147815 |   0.340218 |
| solution-aron-mark |     0.40973  |       0.147721 |   0.347519 |
| solution-flask     |     0.411952 |       1.00879  |   0.383719 |
| solution-1-flask   |     0.422268 |       1.00859  |   0.718002 |
| solution-2         |     0.406151 |       0.49586  |   3.12183  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.412141 |       0.154031 |   0.999106 |
| solution-pl        |     0.407033 |       0.154829 |   1.00334  |
| solution-flask     |     0.407689 |       1.00876  |   1.60425  |
| solution-1-flask   |     0.411739 |       1.00869  |   5.50961  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.413662 |       0.179164 |    3.58869 |
| solution-pl        |     0.411328 |       0.179376 |    3.61687 |
| solution-flask     |     0.410813 |       1.00875  |    5.1036  |