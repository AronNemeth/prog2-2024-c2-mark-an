# 2025-06-21

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     0.494821 |       1.00829  |   0.100711 |
| solution-pl        |     0.482431 |       0.147458 |   0.234406 |
| solution-aron-mark |     5.56749  |       0.204949 |   0.235746 |
| solution-1-flask   |     1.07698  |       1.11562  |   0.266849 |
| solution-1         |     7.33901  |       1e-06    |   0.865602 |
| solution-2         |     0.49398  |       1.06298  |   1.13314  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.503203 |       0.149251 |   0.356019 |
| solution-pl        |     0.501588 |       0.149991 |   0.362512 |
| solution-flask     |     0.496765 |       1.00832  |   0.377731 |
| solution-1-flask   |     0.504076 |       1.00814  |   0.78132  |
| solution-2         |     0.496111 |       0.497335 |   3.88828  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.510445 |       0.157287 |    1.07335 |
| solution-aron-mark |     0.500673 |       0.157661 |    1.07916 |
| solution-flask     |     0.496649 |       1.00858  |    1.58873 |
| solution-1-flask   |     0.501792 |       1.00832  |    5.40425 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.496479 |       0.185404 |    3.22214 |
| solution-aron-mark |     0.495387 |       0.186813 |    3.22687 |
| solution-flask     |     0.495921 |       1.00846  |    5.09216 |