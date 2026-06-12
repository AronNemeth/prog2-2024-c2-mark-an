# 2026-06-12

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     1.10119  |       1.07607  |   0.099507 |
| solution-1-flask   |     0.441262 |       1.00877  |   0.228209 |
| solution-pl        |     5.94502  |       0.159062 |   0.229743 |
| solution-aron-mark |     0.434971 |       0.150702 |   0.232359 |
| solution-1         |     7.33436  |       1e-06    |   0.603877 |
| solution-2         |     0.42205  |       0.61269  |   0.91618  |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.44313  |       0.152252 |   0.350897 |
| solution-aron-mark |     0.424795 |       0.15066  |   0.351529 |
| solution-flask     |     0.439589 |       1.00867  |   0.392557 |
| solution-1-flask   |     0.427136 |       1.00878  |   0.712408 |
| solution-2         |     0.425972 |       0.500753 |   3.13841  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.419715 |       0.167546 |    1.02186 |
| solution-aron-mark |     0.422177 |       0.159523 |    1.03639 |
| solution-flask     |     0.426669 |       1.009    |    1.63626 |
| solution-1-flask   |     0.432329 |       1.0089   |    5.52118 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.419856 |       0.184021 |    3.93821 |
| solution-aron-mark |     0.435843 |       0.18415  |    3.94409 |
| solution-flask     |     0.43105  |       1.00901  |    5.23024 |