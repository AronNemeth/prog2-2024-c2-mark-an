# 2026-03-23

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     3.63153  |       1.04241  |   0.113849 |
| solution-pl        |     5.91681  |       0.151585 |   0.239365 |
| solution-aron-mark |     0.445108 |       0.149791 |   0.24228  |
| solution-1-flask   |     0.450765 |       1.00859  |   0.268677 |
| solution-1         |     9.73474  |       1e-06    |   0.725031 |
| solution-2         |     0.45078  |       0.657992 |   0.861929 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.449517 |       0.15182  |   0.377133 |
| solution-pl        |     0.456694 |       0.15161  |   0.379763 |
| solution-flask     |     0.466754 |       1.00911  |   0.395616 |
| solution-1-flask   |     0.455915 |       1.00857  |   0.811318 |
| solution-2         |     0.44947  |       0.503531 |   1.89742  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.447195 |       0.15624  |    1.1354  |
| solution-aron-mark |     0.450708 |       0.157266 |    1.14347 |
| solution-flask     |     0.465692 |       1.00872  |    1.61757 |
| solution-1-flask   |     0.46059  |       1.00912  |    5.66854 |
| solution-2         |     0.457081 |       0.563235 |  299.46    |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.460339 |       0.186456 |    4.00746 |
| solution-pl        |     0.475978 |       0.181556 |    4.04073 |
| solution-flask     |     0.455255 |       1.00937  |    5.2455  |