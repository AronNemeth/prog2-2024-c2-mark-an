# 2025-08-02

## Inputs: 1000, Queries 20

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-flask     |     2.89452  |       1.1053   |   0.098867 |
| solution-aron-mark |     4.44104  |       0.148089 |   0.234066 |
| solution-pl        |     0.492677 |       0.150314 |   0.235234 |
| solution-1-flask   |     0.503719 |       1.00891  |   0.263075 |
| solution-1         |     7.87777  |       1e-06    |   0.925308 |
| solution-2         |     0.485456 |       0.932909 |   1.0224   |

## Inputs: 10000, Queries 50

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-aron-mark |     0.496685 |       0.153209 |   0.356978 |
| solution-pl        |     0.496711 |       0.151757 |   0.365109 |
| solution-flask     |     0.495091 |       1.00843  |   0.373106 |
| solution-1-flask   |     0.500128 |       1.00815  |   0.807217 |
| solution-2         |     0.490559 |       0.494889 |   3.10818  |

## Inputs: 50000, Queries 200

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.494374 |       0.158431 |    1.06225 |
| solution-aron-mark |     0.500649 |       0.158162 |    1.08011 |
| solution-flask     |     0.514373 |       1.00832  |    1.58938 |
| solution-1-flask   |     0.509643 |       1.00791  |    5.62683 |

## Inputs: 250000, Queries 500

| solution           |   setup_time |   preproc_time |   run_time |
|:-------------------|-------------:|---------------:|-----------:|
| solution-pl        |     0.489486 |       0.190696 |    3.18867 |
| solution-aron-mark |     0.495455 |       0.188881 |    3.19472 |
| solution-flask     |     0.491823 |       1.00803  |    5.0532  |