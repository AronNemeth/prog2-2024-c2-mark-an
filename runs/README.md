# 2025-07-11

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.50015  |       1.0592   |   0.10402  |
| solution-pl        |     0.956476 |       0.153243 |   0.241528 |
| solution-aron-mark |     6.33416  |       0.196982 |   0.244532 |
| solution-1-flask   |     0.537177 |       1.00835  |   0.272022 |
| solution-1         |     8.52239  |       1e-06    |   0.715148 |
| solution-2         |     0.519466 |       0.6678   |   0.999928 |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.511    |       0.156787 |   0.364984 |
| solution-pl        |     0.514952 |       0.153882 |   0.368734 |
| solution-flask     |     0.504327 |       1.00838  |   0.384913 |
| solution-1-flask   |     0.532824 |       1.00867  |   0.807894 |
| solution-2         |     0.50437  |       0.516886 |   2.45567  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.519887 |       0.162797 |    1.07882 |
| solution-pl        |     0.507914 |       0.159687 |    1.09328 |
| solution-flask     |     0.505891 |       1.00861  |    1.61257 |
| solution-1-flask   |     0.53067  |       1.00864  |    5.84695 |
| solution-2         |     0.507837 |       0.598941 |   25.8021  |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.514744 |       0.193622 |    3.41944 |
| solution-aron-mark |     0.520297 |       0.193397 |    3.46633 |
| solution-flask     |     0.511357 |       1.00844  |    5.34479 |