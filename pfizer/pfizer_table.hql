create database if not exists pfizerdatabase;
use pfizerdatabase;
create external table if not exists pfizer (
  username string,
  date_and_time string,
  tweet string,
  hashtags string,
  link string
)

row format delimited
fields terminated by ','
lines terminated by '\n'
stored as textfile location 'hdfs://namenode:8020/user/hive/warehouse/pfizerdatabase.db/pfizer';