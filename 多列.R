library(tidyverse)
library(stringr)
df <- read.csv('~/PycharmProjects/datascience/data/911.csv')

#将1列拆分成多列
df3 <- df %>% separate(title,c('a','b'),sep=': ')
table(df3$a)


df <- read.csv('~/PycharmProjects/datascience/data/911.csv',header = T)
df2 <- as.tibble(do.call(rbind, str_split(df$title, ': ')))
table(df2$V1)