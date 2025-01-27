# 2025-01-27

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.94769  |       1.06059  |   0.083198 |
| solution-aron-mark |     0.738267 |       0.137858 |   0.2025   |
| solution-pl        |     5.36398  |       0.142154 |   0.202824 |
| solution-1-flask   |     1.00431  |       1.00883  |   0.268851 |
| solution-1         |     8.44893  |       1e-06    |   0.778453 |
| solution-2         |     1.00232  |       0.686982 |   1.0944   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.543235 |       1.0089   |   0.297646 |
| solution-pl        |     0.537104 |       0.140665 |   0.304923 |
| solution-aron-mark |     0.539521 |       0.138962 |   0.306443 |
| solution-1-flask   |     0.555994 |       1.00908  |   0.814161 |
| solution-2         |     0.533076 |       0.499966 |  14.402    |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.572873 |       0.149537 |   0.911513 |
| solution-pl        |     0.535673 |       0.149536 |   0.946192 |
| solution-flask     |     0.544963 |       1.0091   |   1.25145  |
| solution-1-flask   |     0.552228 |       1.00878  |   5.80763  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.544967 |       0.177803 |    2.84945 |
| solution-aron-mark |     0.538174 |       0.177854 |    2.86063 |
| solution-flask     |     0.546479 |       1.00896  |    4.27637 |

## Inputs: 1000000, Queries 1000

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.541142 |       0.279923 |    17.3869 |
| solution-aron-mark |     0.548772 |       0.278489 |    17.5459 |